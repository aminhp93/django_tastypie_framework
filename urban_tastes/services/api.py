
from tastypie.resources import ModelResource
from services.models import Product, Order

from tastypie.authentication import BasicAuthentication


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        excludes = ['product_type', 'price']
        allowed_methods = ['get']
        authentication = BasicAuthentication()


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        allowed_methods = ['get', 'post', 'put']