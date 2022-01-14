from django.shortcuts import render, redirect
from .models import *

def index(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos,}
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


    context = {'categories': categories,}
    return render(request, 'base/add_photo.html', context)

def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'base/view_photo.html', context)
