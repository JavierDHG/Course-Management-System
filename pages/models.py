from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='cursos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

class Pay_package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(default=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='paquetes/', blank=True, null=True)


    def __str__(self):
        return self.name

class Status_pay(models.Model):
    pay_package_id = models.ForeignKey(Pay_package, on_delete=models.CASCADE, related_name='status_pay')
    pay_status = models.BooleanField(default=False)
    pay_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('structure.Usuarios', on_delete=models.CASCADE, related_name='status_pay')
    expire_date = models.DateTimeField()
    
    def __str__(self):
        return f"Status for {self.user.username} - {'Paid' if self.pay_status else 'Unpaid'}"
    
    class Meta:
        verbose_name = 'Estado de Pago'
        verbose_name_plural = 'Estados de Pago'

class My_course_list(models.Model):
    user = models.ForeignKey('structure.Usuarios', on_delete=models.CASCADE, related_name='my_course_list')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='my_course_list')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"
    
    class Meta:
        verbose_name = 'Lista de Cursos del Usuario'
        verbose_name_plural = 'Listas de Cursos de Usuarios'
        unique_together = ('user', 'course')

class video_course_list(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course.name}"
    
    class Meta:
        verbose_name = 'Video del Curso'
        verbose_name_plural = 'Videos de Cursos'
        ordering = ['created_at']

class VideoSeen(models.Model):
    user = models.ForeignKey('structure.Usuarios', on_delete=models.CASCADE, related_name='video_seen')
    video = models.ForeignKey(video_course_list, on_delete=models.CASCADE, related_name='video_seen')
    seen_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"
    
    class Meta:
        verbose_name = 'Video Visto'
        verbose_name_plural = 'Videos Vistos'
        unique_together = ('user', 'video')