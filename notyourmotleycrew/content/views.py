# Create your views here.

from django.shortcuts import render_to_response
from notyourmotleycrew.content.models import NYMCImage

def home(request):
    template = "home.html"
    images = NYMCImage.objects.all().order_by('-timestamp')
    return render_to_response(template, {'images':images})

def about(request):
    template = "about.html"
    return render_to_response(template, {})

def contribute(request):
    template = "contribute.html"
    return render_to_response(template, {})
