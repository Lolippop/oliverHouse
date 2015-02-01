#coding:utf-8
from django.conf.urls import patterns, url
from bgapplication import views
urlpatterns = patterns('',
# Examples:
# url(r'^$', 'urlmappingtest.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
#urlmapping  views.index即是views.py里的index方法  返回一个httpresponse对象或者url
    url(r'^$',views.index,name='index')
)
