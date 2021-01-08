from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('<slug:slug>', views.SingleGroup.as_view(), name='single'),
    path('<slug:slug>/join', views.JoinGroup.as_view(), name='join'),
    path('<slug:slug>/leave', views.LeaveGroup.as_view(), name='leave'),
]
