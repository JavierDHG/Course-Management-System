from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Pay_package, Status_pay, My_course_list, video_course_list
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone


# Create your views here.

@login_required
def create_course(request):
    categories = Course.objects.values_list('category', flat=True).distinct()
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            messages.error(request, 'No tienes permisos para crear cursos.')
            return redirect('index')
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            imagen = request.FILES.get('imagen')

            course = Course.objects.create(
                name=name,
                description=description,
                imagen=imagen,
            )
            course.save()
            return redirect('index')
    return render(request, 'courses/course_create.html', {
        'title': 'Creacion de Cursos',
        'categories': categories,
    })

def course_detail(request, course_id):
    user = request.user
    has_paid_package = False
    categories = Course.objects.values_list('category', flat=True).distinct()

    if user.is_authenticated:
        has_paid_package = user.status_pay.filter(pay_status=True).exists()

    course = Course.objects.get(id=course_id)
    return render(request, 'detail_course/details.html', {
        'course': course,
        'title': 'Detalles del Curso',
        'has_paid_package': has_paid_package,
        'categories': categories,
    })

@login_required
def pay_package_method(request, package_id):
    package = get_object_or_404(Pay_package, id=package_id)
    categories = Course.objects.values_list('category', flat=True).distinct()

    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para realizar un pago.')
        return redirect('login')
    else:
        if request.method == 'POST':
            user = request.user
            if user.is_authenticated:
                # Verifica si ya tiene un paquete activo (que no haya expirado)
                current_status = Status_pay.objects.filter(
                    user=user, expire_date__gt=timezone.now()).first()
                if current_status:
                    messages.error(
                        request, 'Ya tienes un paquete de pago activo. No puedes comprar otro hasta que expire el actual.')
                    return redirect('index')

                # Crea el nuevo estado de pago con la fecha de expiración calculada
                expire_date = timezone.now() + timedelta(days=package.duration_days)
                Status_pay.objects.create(
                    pay_package_id=package,
                    pay_status=True,
                    user=user,
                    expire_date=expire_date
                )
                messages.success(request, '¡Paquete activado correctamente!')
                return redirect('index')
            else:
                return redirect('login')
    return render(request, 'pay/pay_method.html', {
        'package': package,
        'title': 'Metodos de Pago',
        'categories': categories,
    })

@login_required
def view_package(request):
    categories = Course.objects.values_list('category', flat=True).distinct()
    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para ver los paquetes.')
        return redirect('login')
    else:
        user = request.user
        packages = Pay_package.objects.all().order_by('price')
        paid_packages_ids = Status_pay.objects.filter(
            user=user, pay_status=True).values_list('pay_package_id', flat=True)

    return render(request, 'pay/pay_package.html', {
        'packages': packages,
        'paid_packages_ids': paid_packages_ids,
        'title': 'Paquetes Disponibles',
        'categories': categories,
    })

@login_required
def add_to_my_course_list(request, course_id):
    user = request.user
    if user.is_authenticated:
        course = Course.objects.get(id=course_id)
        if not user.my_course_list.filter(course=course).exists():
            user.my_course_list.create(course=course)
            messages.success(request, 'Curso agregado a tu lista de cursos.')
        else:
            messages.warning(request, 'El curso ya está en tu lista de cursos.')
        return redirect('index')
    else:
        return redirect('login')


@login_required
def my_course_list(request):
    categories = Course.objects.values_list('category', flat=True).distinct()
    if request.user.is_authenticated:
        my_courses = My_course_list.objects.filter(
            user=request.user).select_related('course')
        return render(request, 'courses/my_courses.html', {
            'my_courses': my_courses,
            'title': 'Mis Cursos',
            'categories': categories,
        })
    else:
        messages.error(request, 'Debes iniciar sesión para ver tus cursos.')
        return redirect('login')

@login_required
def list_video_course(request, course_id):
    categories = Course.objects.values_list('category', flat=True).distinct()
    course = get_object_or_404(Course, id=course_id)
    videos = video_course_list.objects.filter(course=course)

    return render(request, 'study_areas/study_area.html', {
        'course': course,
        'videos': videos,
        'title': f'Videos del Curso: {course.name}',
        'categories': categories,
    })

@login_required
def mark_video_as_seen(request, video_id):
    if request.user.is_authenticated:
        video = get_object_or_404(video_course_list, id=video_id)
        if not request.user.video_seen.filter(video=video).exists():
            request.user.video_seen.create(video=video)
            messages.success(request, 'Video marcado como visto.')
        else:
            messages.warning(request, 'El video ya está marcado como visto.')
        return redirect('list_video_course', course_id=video.course.id)
    else:
        return redirect('login')