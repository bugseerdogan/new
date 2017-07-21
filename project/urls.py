from django.conf.urls import url
from . import views

app_name='project'

urlpatterns = [
    #Whenever requested anything
    #/project/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    #url(r'^$', views.index, name='index'),
    #/music/id/ any following id
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^plans/(?P<pk>[0-9]+)/$', views.plans, name='plans'),
    #/project/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #/project/plan/add/
    url(r'plan/add/$', views.PlanCreate.as_view(), name='plan-add'),


]