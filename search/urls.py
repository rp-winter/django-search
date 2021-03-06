from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='home'),
    path('search_institute/', views.search_institute, name = 'search_institute'),
    path('validate_password1/', views.validate_password1, name = 'validate_password1'),
    path('submit/', views.submit, name = 'submit'),
    path('print_form/', views.print_form, name = 'print_form'),
]