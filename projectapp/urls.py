from django.urls import path

from projectapp.views import ProjectCreateView

app_name = 'projectapp'

urlpatterns = [
    # path('',ProjectListView.as_view(),name='list'),
    path('craate/',ProjectCreateView.as_view(),name='create'),
    # path('detail/<int:pk>',ProjectDetailView.as_view(),name='detail')
]