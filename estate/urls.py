from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.homepage, name='homepage'),
    url('^view_businesses/(\d+)/', views.view_businesses,name='view_businesses')
]