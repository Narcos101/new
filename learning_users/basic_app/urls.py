from django.urls import re_path
from django.conf.urls import url
from basic_app import views

appname = 'basic_app'

urlpatterns = [
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login')
]
