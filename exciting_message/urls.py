from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.aloha_python, name='aloha_python'),
]