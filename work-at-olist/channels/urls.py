from django.conf.urls import url, include

from rest_framework import routers

from channels import views

# Channels router
channels = routers.SimpleRouter()
channels.register(r'channels', views.ChannelResourceViewSet, 'channel')

# Categories router
categories = routers.SimpleRouter()
categories.register(r'categories', views.CategoryResourceViewSet, 'category')

urlpatterns = [
    url(r'^', include(channels.urls)),
    url(r'^', include(categories.urls)),
]
