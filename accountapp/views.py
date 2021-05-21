from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        # DB관련
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        # DB 관련
        return render(request,"accountapp/hello_world.html",context={'hello_world_output': new_hello_world })
    else:
        return render(request,"accountapp/hello_world.html",context={'text':'GET METHOD!!!"'})

def start_world(request):
    return HttpResponse("SUCESS YOURSELF")
# 문자열을 반환 해주는 중

