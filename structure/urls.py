from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.update_profile, name='update_profile'),
    path('category/<str:category>/', views.category_courses, name='category_courses'),
    
]
