from django.urls import path
# http://127.0.0.1:8000/blog/
from blog.views import post_detail, blog

app_name = 'blog'


urlpatterns = [
    path('', blog, name='post_list'), # http://127.0.0.1:8000/blog/
    path('detail/<int:id>/', post_detail, name='post_detail'),

]

