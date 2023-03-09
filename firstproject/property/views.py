from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from blog.models import Post
from property.forms import PropertyForm
from property.models import Property, REGION


def index_page(request):
    queryset = Property.objects.all()[:3]
    queryset_posts = Post.objects.all()[:4]
    context = {
        'title': 'Property',
        'property_all': queryset,
        'posts_all': queryset_posts,
    }
    return render(request, 'index.html', context)


def properties(request):
    queryset = Property.objects.all()

    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(region__icontains=query)
        )

    paginator = Paginator(queryset, 3)
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
        'title': 'Property',
        'property_all': queryset,
        'page_obj': page_obj,
        'page_request_var': page_request_var
    }
    return render(request, 'properties.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'about.html', context)


def agent(request):
    context = {
        'title': 'Agent',
    }
    return render(request, 'agent.html', context)


def services(request):
    context = {
        'title': 'Services',
    }
    return render(request, 'services.html', context)


def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context)


def for_staff(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'registration/for_staff.html', context)



def property_single(request, id=None):
    instance = get_object_or_404(Property, id=id)
    context = {
        'title': 'Property details',
        'object': instance
    }
    return render(request, 'properties-single.html', context)


def property_edit(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Property, id=id)
    form = PropertyForm(request.POST or None,
                        instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # messages.success(request,
        #                  'Info saved!',
        #                  extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_url_property())
    context = {
        'title': 'Property update',
        'form': form,
        'object': instance
    }
    return render(request, 'property-edit.html', context)


def property_create(request, id=None):
    # instance = get_object_or_404(Property, id=id)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PropertyForm(request.POST, request.FILES)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_url_property())
    context = {
        'title': 'Property create',
        'form': form,
    }
    return render(request, 'property-create.html', context)


def property_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Property, id=id)
    instance.delete()
    return redirect("/property/")
