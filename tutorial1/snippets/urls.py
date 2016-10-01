from django.conf.urls import include, url
from .views import snippet_detail, snippet_list

urlpatterns = [
 	url(r'^snippets/$', snippet_list),
    url(r'snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]
