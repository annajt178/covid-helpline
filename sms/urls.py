from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sms_response, name="sms"),
    #path('broadcast/<str:number>', views.broadcast_sms, name="broadcast")
    path('broadcast/', views.broadcast_sms, name="broadcast"),
]