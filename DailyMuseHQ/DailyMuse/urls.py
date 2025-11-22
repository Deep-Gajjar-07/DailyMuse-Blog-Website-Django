from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='homepage'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('<int:blog_id>/edit-blog/', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete-blog/', views.delete_blog, name='delete_blog'),
    path('register/', views.register, name='user_register'),
]