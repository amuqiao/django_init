# -*- coding: utf-8 -*-
# @Time    :2021/4/26 10:41 上午

# from django.conf.urls import url
from django.urls import path, include

from . import views

# urlpatterns = [
#     url(r'^$', views.hello),
# ]

urlpatterns = [
    path(r'insert/', views.insert),
    path(r'show/', views.show),
    path(r'insert_json/', views.insert_json),

]
