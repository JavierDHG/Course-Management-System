from django.contrib import admin
from . models import Course, Pay_package, Status_pay, My_course_list, video_course_list, VideoSeen
# Register your models here.

admin.site.register(Course)
admin.site.register(Pay_package)
admin.site.register(Status_pay)
admin.site.register(My_course_list)
admin.site.register(video_course_list)
admin.site.register(VideoSeen)
admin.site.site_header = "Sistema de Gestión de Cursos"
admin.site.site_title = "Sistema de Gestión de Cursos"
admin.site.index_title = "Bienvenido al sistema de gestión de cursos"