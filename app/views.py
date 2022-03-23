from django.shortcuts import render
from app.forms import *
from django.views.generic import View,ListView,DetailView
from app.models import *
# Create your views here.
def registration(request):
    form=StudentProfileForm()
    if request.method=='POST':
        fd=StudentProfileForm(request.POST)
        if fd.is_valid():
            fd.save()
    return render(request,'register.html',context={'form':form})
def schoollistview(request):
    data=StudentProfile.objects.all()
    return render(request,'studentprofile_list.html',context={'data':data})
'''

class SchoolDetailView(DetailView):
    model=StudentProfile
    context_object_name='school'
'''