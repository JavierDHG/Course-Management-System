from django.urls import path
from . import views

urlpatterns = [
    path('create_course/', views.create_course, name='create_course'),
    path('course_detail/<int:course_id>/', views.course_detail, name='course_detail'),
    path('view_package/', views.view_package, name='view_package'),
    path('pay_package_method/<int:package_id>/', views.pay_package_method, name='pay_package_method'),
    path('my_courses/', views.my_course_list, name='my_courses'),
    path('add_to_my_course_list/<int:course_id>/', views.add_to_my_course_list, name='add_to_my_course_list'),
    path('list_video_course/<int:course_id>/', views.list_video_course, name='list_video_course'),
    path('video/<int:video_id>/seen/', views.mark_video_as_seen, name='mark_video_seen'),
]