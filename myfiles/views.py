from django.shortcuts import render
from .form import *
# Create your views here.

def User(request):
    if request.method == 'POST':
         fm = User_form(request.POST,request.FILES)
         if fm.is_valid():
             fm.save()
             return render(request,'thank.htm')
    else:
        fm = User_form()
        
    return render(request, 'files.htm' ,{'form':fm})