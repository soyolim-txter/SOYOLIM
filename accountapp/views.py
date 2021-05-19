from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def hello_world(request):
    return render(request,"base.html")


def start_world(request):
    return HttpResponse("SUCESS YOURSELF")
# 문자열을 반환 해주는 중

