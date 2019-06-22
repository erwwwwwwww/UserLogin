from django.conf.urls import url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^register/$', views.user_register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
]
