from django.shortcuts import render

# Create your views here.

def bloglist(request):
    return render(request,'AppBlogTemplate/Bloglist.html',context={})
