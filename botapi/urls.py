# from django.conf.urls import url, include
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r'snippets', views.GetMessage)

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     url(r'^', include(router.urls))
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getBotDetails, name='index'),
    url(r'^updates/$', views.getUpdates, name='updates'),
]