from django.http import HttpResponse
from django.shortcuts import render
import datetime
def HOME (request):
    isActive=True
    if request.method=='POST':
         check=request.POST.get("check")
         print(check)  
         if check is  None: isActive=False
         else: isActive=True

    date=datetime.datetime.now() 
    name="suman kumar das"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'LUCKNOW'
    }
    # return HttpResponse("<h1>Hello this is index page  </h1> "+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request, "Home.html",data)


def ABOUT (request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request, "About.html",{})

def SERVICE (request):
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request, "Services.html",{})