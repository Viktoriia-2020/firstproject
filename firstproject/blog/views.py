from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib import messages


# Create your views here.
def blog(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_request_var = 'page'

    try:
        queryset = paginator.page(page_number)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'title': 'Blog',
        'posts_all': queryset,
        'page_obj': page_obj,
        'page_request_var': page_request_var
    }

    return render(request, 'blog.html', context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Post details',
        'object': instance
    }
    return render(request, 'blog-single.html', context)




