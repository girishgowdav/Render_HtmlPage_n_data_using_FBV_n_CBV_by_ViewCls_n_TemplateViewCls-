from django.shortcuts import render
from app.forms import *
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class Data_render(View):
    def get(self,request):
        d={'name':'giri'}
        return render(request,'Data_render.html',d)

#insert_fbv

def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted')
    return render(request,'insert_fbv.html',d)


    
#Cbv_insert
class Cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Cbv_insert.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Cbv_insert')



class Temp(TemplateView):
    template_name='temp.html'