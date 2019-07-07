from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url(r'^$', views.homepage, name='homepage'),
    url(r'^view_businesses/(\d+)/', views.view_businesses,name='view_businesses'),
    url(r'^process_bizform/$', views.process_biz_form, name='process_biz_form'),
    url(r'^business_form/$', views.business_form, name='business_form')
]