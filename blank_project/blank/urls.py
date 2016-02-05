from django.conf.urls import url
from blank import views

urlpatterns = [
    url(r'^blank/$', views.post_list),
]
