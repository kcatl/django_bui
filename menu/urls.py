from django.conf.urls import patterns, include, url
from menu import views
from bui import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index),
    url(r'^assets/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),    
    url(r'code.html$', views.MainCode), 
)