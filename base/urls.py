from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_photo/', add_photo, name='add_photo'),
    path('view_photo/<str:pk>/', view_photo, name='view_photo'),
    path('edit_page/<str:pk>/', edit_page, name='edit_page'),
    path('delete_page/<str:pk>/', delete_page, name='delete_page'),
]