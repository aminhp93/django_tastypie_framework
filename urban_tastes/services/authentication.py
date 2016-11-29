from tastypie.models import ApiKey
from tastypie.http import HttpUnauthorized
from tastypie.authentication import Authentication
from django.core.exceptions import ObjectDoesNotExist

class CustomApiKeyAuthentication(Authentication):
	def _unauthorzied(self):
		return HttpUnauthorized()

	def is_authenticated(self, request, **kwargs):
		if not(request.META.get("HTTP_AUTHROIZATION")):
			return self._unauthorzied()

		api_key = request.META["HTTP_AUTHORIZATION"]
		key_auth_check = self.get_key(api_key, request)
		return key_auth_check

	def get_key(self, api_key, request):
		try:
			user = ApiKey.objects.get(key=api_key)
		except ObjecetDoesNotExist:
			return self._unauthorzied()
		return True

