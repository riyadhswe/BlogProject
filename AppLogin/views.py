from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def singup(request):
    form = UserCreationForm(data = request.POST)
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True


    dict = {'form':form, 'registered':registered }
    return render(request,'AppLoginTemplate/sign_up.html',context = dict)
