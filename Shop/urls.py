from django.urls import path
from django.conf.urls import url
from .views import shop, product_list, product_detail

urlpatterns = [
    path('', shop),
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        product_detail,
        name='product_detail'),
]
