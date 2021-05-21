from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def hello_world(request):

    if request.method == "POST":
        return render(request,"accountapp/hello_world.html",context={'text':'POST METHOD!!!"'})
    else:
        return render(request,"accountapp/hello_world.html",context={'text':'GET METHOD!!!"'})

def start_world(request):
    return HttpResponse("SUCESS YOURSELF")
# 문자열을 반환 해주는 중

