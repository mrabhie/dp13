from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"dp13app/home.html")

def profile(request):
    name="akshay"
    return render(request,"dp13app/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"post_demo.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phoneno=request.POST.get("phone_no")
        pwd=request.POST.get("pwd")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=='1':
            gender="Female"
        else:
            gender="Male"
        send_mail("Thank you for registration","mr/ms.{} {}\n Thanks for registerinng with us".format(first_name,last_name),"abhidenim10@gmail.com",[email,],fail_silently=False)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,phoneno,date,month,year,gender))
    return render(request,"dp13app/register.html")