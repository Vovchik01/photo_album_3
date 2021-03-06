from django.shortcuts import render, redirect
from datetime import datetime
from .models import *

def index(request):
    category = request.GET.get('category')
    categories = Category.objects.all()

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    now = datetime.now()
    current_year = now.year
    

    context = {'categories': categories, 'photos': photos, 'current_year': current_year,}
    return render(request, 'base/index.html', context)

def add_photo(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('img_upload')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['add_category'] != '':
            category, created = Category.objects.get_or_create(name=data['add_category'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            image=image,
            description = data['description'],
        )

        return redirect('index')

    now = datetime.now()
    current_year = now.year

    context = {'categories': categories, 'current_year': current_year,}
    return render(request, 'base/add_photo.html', context)

def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)

    now = datetime.now()
    current_year = now.year

    context = {'photo': photo, 'current_year': current_year,}
    return render(request, 'base/view_photo.html', context)


def edit_page(request, pk):
    categories = Category.objects.all()
    photo = Photo.objects.get(id=pk)

    now = datetime.now()
    current_year = now.year

    if request.method == 'POST':
        data = request.POST

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['add_category'] != '':
            category, created = Category.objects.get_or_create(name=data['add_category'])
        else:
            category = None

        photo = Photo.objects.filter(id=pk).update(
                category=category,
                description = data['description'],
            )
        return redirect('index')

    context = {'photo': photo, 'categories': categories, 'current_year': current_year,}
    return render(request, 'base/edit_page.html', context)


def delete_page(request, pk):
    photo = Photo.objects.get(id=pk)

    now = datetime.now()
    current_year = now.year

    if request.method == 'POST':
        photo.delete()
        return redirect('index')
        
    context = {'photo': photo, 'current_year': current_year,}
    return render(request, 'base/delete_page.html', context)

