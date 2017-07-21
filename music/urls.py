from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    #Whenever requested anything
    #/music/
    url(r'^$', views.index, name='index'),
    #/music/id/ any following id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/id/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]