from django.shortcuts import render,HttpResponse,redirect
from .models import*
def home(request):
    return render(request,"home.html")
def studreg(request):
     if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        e=request.POST['email']
        dob=request.POST['dob']
        Student.objects.create(name=name,email=e,dob=dob,age=age)
        return HttpResponse("Registered successfully...!")
     else:
        return render(request,"studreg.html")     

def view_stud(request):
   x=Student.objects.all()
   return render(request,"viewstud.html",{'view':x})                            

                           

def studupdate(request,id):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        em=request.POST['email']
        dob=request.POST['dob']
        data=Student.objects.filter(id=id)
        data.update(name=name,email=em,age=age,dob=dob)
        return redirect(view_stud)
    else:
      x=Student.objects.get(id=id)
    return render(request,"editstud.html",{'view':x})


def deletestud(request,id):
    x=Student.objects.get(id=id)
    x.delete()
    return HttpResponse("data deleted")