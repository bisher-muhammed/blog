from django.urls import path
from . import views


    

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post, name='post'),
    path('make', views.make, name='make'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.login_required,name='login'),



]

