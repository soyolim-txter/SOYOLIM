from django.urls import path
from accountapp.views import hello_world, start_world

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),
    path('start_world/',start_world, name = 'start_world')
]