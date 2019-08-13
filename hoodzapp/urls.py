from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^new/project$', views.new_post, name='new-post'),
    url(r'^post/(\d+)',views.post, name='post'),
    url(r'^profile/',views.profile,name ='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile_update/',views.update_profile,name='profile_update')
    url(r'^switch_hood/$', views.switch_hood,name='switch_hood')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)