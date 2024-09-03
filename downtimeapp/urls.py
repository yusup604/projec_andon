from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('leader/', views.leader, name='leader'),
    path('status_leader/', views.status_leader, name='status_leader'),
    path('update_status/', views.update_status, name='update_status'),
    path('reset_status/', views.reset_status, name='reset_status'),
    path('display/', views.display, name='display'),
    path('update_display_status/', views.update_display_status, name='update_display_status'),
    path('fetch_display_status/', views.fetch_display_status, name='fetch_display_status'),
    path('reset_display_status/', views.reset_display_status, name='reset_display_status'),  # New endpoint
    path('perbaikan/', views.perbaikan, name='perbaikan'),
]
