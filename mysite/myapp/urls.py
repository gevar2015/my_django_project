from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data_page, name='data'),
    path('test/', views.test_page, name='test'),
]