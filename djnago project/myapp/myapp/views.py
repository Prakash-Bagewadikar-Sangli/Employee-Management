from django.http import HttpResponse
from django.shortcuts import render

import datetime





def home(request):
    if request.method=='POST':
        check=request.POST['check']
        print(check)


    date=datetime.datetime.now()
    isActive=True
    name="Prakash Bagewadikar"
    list_of_Programs=[
        'WAP to check even or odd',
        'WAP to check even no',
        'WAP to print all prime number form 1 to 100',
        'WAP to printpascals traingel'
    ]
    student={
        'student_name':"Prakash",
        'student_college':"ashta highschool",
        'student_city':"ashta",
    }
    # return HttpResponse("<h1>Hello this is index page</h1>" +str(date))

    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_Programs':list_of_Programs,
        'student_data':student

    }
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1>this is about page</h1>")
    return render(request,"about.html",{})

    
def services(request):
    #return HttpResponse("<h1>this is servises page</h1>")
    return render(request,"services.html",{})


