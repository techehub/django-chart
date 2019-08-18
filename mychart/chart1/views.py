from django.shortcuts import render
from django.http.response import  JsonResponse

# Create your views here.

def mypage (request):
    return render(request, "mypage.html", {})


def mypage1 (request):
    return render(request, "mypage1.html", {})


def getdata(request):
    lables= ["India", "Pakistan", "China"]
    values= [100,30,150]
    data = {
        "labels": lables,
        "values": values
    }
    return JsonResponse(data)


import random
def getdata1(request):
    lables= list(range(1,30))
    values= [random.randint(50,100) for x in lables ]
    data = {
        "labels": lables,
        "values": values
    }
    return JsonResponse(data)