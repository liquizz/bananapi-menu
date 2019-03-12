from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView),
    path('StartCapture/', views.StartCaptureView),
    path('StopCapture/', views.StopCaptureView),
    path('pppoe_config/', views.PPPoEView),
    path('static_config/', views.StaticView),
]