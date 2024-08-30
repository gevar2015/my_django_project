from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Привет, Django!")

def data_page(request):
    return render(request, 'data.html')  # Отображение шаблона data.html

def test_page(request):
    return render(request, 'test.html')  # Отображение шаблона test.html

