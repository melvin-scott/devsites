from django.urls import path

from . import views

app_name = 'CSVdata'

urlpatterns = [
    path('', views.csvList, name='Home'),
    path('<int:file_id>', views.CSVView, name='View'),
    path('<int:file_id>/dashboard', views.dashboard, name='Dashboard'),
    path('upload', views.upload, name='Upload'),
]