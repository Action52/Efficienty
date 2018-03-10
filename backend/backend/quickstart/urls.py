from django.conf.urls import url
from quickstart import views


urlpatterns = [
    url(r'^comments/$', views.comment_list),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.comment_detail),
    url(r'^experience/$', views.experiencia_list),
    url(r'^experience/(?P<pk>[0-9]+)/$', views.experiencia_detail),
    url(r'^projects/$', views.project_list),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
    url(r'^skills/$', views.skill_list),
    url(r'^skills/(?P<pk>[0-9]+)/$', views.skill_detail),
    url(r'^leadership/$', views.leadership_list),
    url(r'^leadership/(?P<pk>[0-9]+)/$', views.leadership_detail),
]
