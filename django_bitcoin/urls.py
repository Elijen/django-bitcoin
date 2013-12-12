try:
    from django.conf.urls import patterns, url, include
except ImportError:
    from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('django_bitcoin.views',
    url(r'^qrcode/(?P<key>.+)/(?P<size>.+)/$', 'qrcode_view', name='qrcode'),
    url(r'^qrcode/(?P<key>.+)/$', 'qrcode_view', name='qrcode'),
)
