from django.contrib import admin
from django.urls import path


from uploads import views


urlpatterns = [
    path(r'', views.home, name='home'),
    path('uploads/', views.model_form_upload, name='upload'),
    
]


