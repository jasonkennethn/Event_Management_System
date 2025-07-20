from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('<int:pk>/edit/', views.update_event, name='update_event'),
    path('<int:pk>/delete/', views.delete_event, name='delete_event'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
]