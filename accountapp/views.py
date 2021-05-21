from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request,"accountapp/hello_world.html",context={'hello_world_list': hello_world_list})

def start_world(request):
    return HttpResponse("SUCESS YOURSELF")
# 문자열을 반환 해주는 중

