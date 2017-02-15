from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /questions
    url(r'^questions/$', views.question_list, name='question_list'),
]
