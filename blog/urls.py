from django.conf.urls import url
from . import views

urlpatterns = [
    url('qwerty', views.post_list, name='post_list'),
    url('something', views.sample_view, name='post_list'),
]