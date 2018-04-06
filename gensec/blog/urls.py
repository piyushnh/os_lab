from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
url(r'^posts/$',views.PostListView.as_view(),name='post_list'),
url(r'^ongoing/$',views.EventListView.as_view(),name='event_list'),
url(r'^secreply/(?P<pk>\d+)/$',views.ReplyComment, name='reply_secretary'),
url(r'^$',views.HomeView.as_view(),name='home'),



]
