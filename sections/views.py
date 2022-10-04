from django.shortcuts import render
from .models import Sections

# Create your views here.

def sections_list(request):
    section = Sections.objects.all()
    context ={
        'section':section
        }
    return render(request, 'sections/sections-list.html', context)
