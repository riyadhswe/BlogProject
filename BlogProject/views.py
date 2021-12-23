from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def Index(request):
    return HttpResponseRedirect(reverse('AppBlog:bloglist'))