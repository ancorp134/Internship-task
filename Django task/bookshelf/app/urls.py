from django.urls import path
from . import views

urlpatterns = [
    path('new/',views.Add_Record),
    path('all/',views.BookShelf_Details),
    path('single/<int:pk>/',views.BookShelf_SingleRecord),
]