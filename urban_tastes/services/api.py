import time

from tastypie.resources import ModelResource
from services.models import Product, Order

# from tastypie.authentication import BasicAuthentication
# from tastypie.authentication import ApiKeyAuthentication
from services.authentication import CustomApiKeyAuthentication

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        excludes = ['product_type', 'price']
        allowed_methods = ['get']
        # authentication = BasicAuthentication()
        # authentication = ApiKeyAuthentication()
        # authentication = CustomApiKeyAuthentication()

    def dehydrate_name(self, bundle):
    	return bundle.data['name'].upper()
    	
    def dehydrate(self, bundle):
    	bundle.data["server_time"] = time.ctime()
        return bundle


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        allowed_methods = ['get', 'post', 'put']
        # authentication = CustomApiKeyAuthentication()



