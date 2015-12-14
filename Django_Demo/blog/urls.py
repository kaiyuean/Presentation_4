#!/usr/bin/env python
# - *- coding: utf- 8 - *-
########################################################################
# 
# Copyright (c) 2015 kaiyuean All Rights Reserved
# 
########################################################################
 
'''
 
Author: kaiyuean
Date: 2015/11/05 10:44:00
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]

