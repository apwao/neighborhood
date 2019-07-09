from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    # url(r'^view_posts/$', views.view_posts,name='view_posts'),
    url(r'^post_form/$',views.post_form, name='post_form'),
]

