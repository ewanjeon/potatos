from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.devnews_list, name='devnews_list'),
]
