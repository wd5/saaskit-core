### -*- coding: utf-8 -*- ##

from django.http import Http404
from django.conf import settings

from muaccount_content.views import mu_flatpage

class FlatpageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404 or not hasattr(request, 'muaccount'):
            return response # No need to check for a flatpage for non-404 responses.
        try:
            return mu_flatpage(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
