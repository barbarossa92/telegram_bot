# -*- coding: utf8 -*-


from django.conf.urls import url

from main.views import CommandReceiveView

urlpatterns = [
    url(r'^bot/(?P<bot_token>.+)/$', CommandReceiveView.as_view(), name='command'),
]