from django.urls import path
from django.conf.urls import url
from .views import product_list, product_detail
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shop'

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
