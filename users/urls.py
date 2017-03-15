from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'', views.add, name='add'),
    url(r'^submitted/$', views.submitted, name='submitted'),
]
