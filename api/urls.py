from django.urls import path

from . import views

urlpatterns = [
    path('file/', views.TempFileView.as_view(), name='get-one-file'),
    path('file/list/', views.ListTempFileView.as_view(), name='get-file-list'),
    path('file/add/', views.TempFileView.as_view(), name='add-file'),
]
