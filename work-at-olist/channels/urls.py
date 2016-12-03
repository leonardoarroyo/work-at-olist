from django.conf.urls import url, include

from rest_framework import routers

from channels import views

# Channels router
router = routers.SimpleRouter()
router.register(r'', views.ChannelResourceViewSet, 'channel')

urlpatterns = [
    url(r'^', include(router.urls)),
]
