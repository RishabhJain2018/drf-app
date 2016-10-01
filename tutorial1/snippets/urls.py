from django.conf.urls import include, url
from .views import snippet_detail, snippet_list
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
 	url(r'^snippets/$', snippet_list),
    url(r'snippets/(?P<pk>[0-9]+)/$', snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
