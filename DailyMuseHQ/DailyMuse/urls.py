from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='homepage'),
    path('<int:blog_id>/detail-blog/', views.detail_blog, name='detail_blog'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('my-blogs/', views.my_blogs, name='my_blogs'),
    path('<int:blog_id>/edit-blog/', views.edit_blog, name='edit_blog'),
    path('<int:blog_id>/delete-blog/', views.delete_blog, name='delete_blog'),
    path('search_blogs/', views.search_blogs, name='search_blogs'),
    path('register/', views.register, name='user_register'),
]