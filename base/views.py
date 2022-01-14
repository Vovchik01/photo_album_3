from django.shortcuts import render
from .models import *

def index(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos,}
    return render(request, 'base/index.html', context)

def add_photo(request):
    context = {}
    return render(request, 'base/add_photo.html', context)

def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, 'base/view_photo.html', context)
