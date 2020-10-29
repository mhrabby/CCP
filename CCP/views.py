from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"main.html")


def ielts(request):
    return render(request,"ielts.html")

def gre(request):
    return render(request,"gre.html")

def gmat(request):
    return render(request,"gmat.html")

def sat(request):
    return render(request,"sat.html")

def SpokenEnglish(request):
    return render(request,"SpokenEnglish.html")

def excel(request):
    return render(request,"excel.html")
