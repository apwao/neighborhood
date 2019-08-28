from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url(r'^$', views.homepage, name='homepage'),
    url(r'^view_businesses/', views.view_businesses,name='view_businesses'),
    url(r'^process_bizform/$', views.process_biz_form, name='process_biz_form'),
    url(r'^business_form/$', views.business_form, name='business_form'),
    url(r'^profile_form/$',views.profile_form, name='profile_form'),
    url(r'^view_profile/$',views.view_profile, name='view_profile'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
