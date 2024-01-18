from django.shortcuts import render
import os

def my_view(request):
    return render(request, 'regalo/my_template.html')
