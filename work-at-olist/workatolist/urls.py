from django.conf.urls import url, include

import channels.urls

urlpatterns = [
    # Channels urls
    url(r'^', include(channels.urls)),

    # Admin is disabled
    # url(r'^admin/', admin.site.urls),
]
