from django.http import HttpResponse
from django.shortcuts import render
def input(request):
    return render(request,'base.html')
def add(request):
   x=int(request.GET['t1'])
   y=int(request.GET['t2'])
   z=x+y
   request.session['z'] =z
   request.session.set_expiry(30)
   return HttpResponse('data submitted successfully')
def display(request):
    if request.session.has_key('z'):
        z = request.session['z']
        return HttpResponse(z)
    else:
        print("end")
        return render(request,'base.html')




