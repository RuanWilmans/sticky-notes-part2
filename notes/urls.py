from django.urls import path
from . import views
urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/<int:pk>/edit/', views.note_update, name='note_update'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/new/', views.author_create, name='author_create'),
]
