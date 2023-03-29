from django.urls import path
from .views import home, blog_category, category, blog_detail, add_blog, blog_update, blog_delete, user_list, my_blog, blog_tag
app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>', blog_category, name='blog_category'),
    path('my-blog/', my_blog, name='my_blog'),
    path('blog-detail/<slug:slug>', blog_detail, name='blog_detail'),
    path('category-list/', category, name='category-list'),
    path('add-blog/', add_blog, name='add_blog'),
    path('blog-update/<slug:slug>', blog_update, name='blog_update'),
    path('blog-delete/<slug:slug>', blog_delete, name='blog_delete'),
    path('user-list/', user_list, name='user_list'),
    path('blog_-ag/<slug:slug>', blog_tag, name='blog_tag'),

]