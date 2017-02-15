from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^ncr$', views.ncr, name='ncr'),
]
