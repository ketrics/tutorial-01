from django.urls import path
from .views import HelloWorldApiView

urlpatterns = [
    path('helloworld/', HelloWorldApiView.as_view(), name='hello_world')
]