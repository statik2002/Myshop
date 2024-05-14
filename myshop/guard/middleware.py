from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from asgiref.sync import iscoroutinefunction, markcoroutinefunction

from guard.models import Metrica, RequestHistory, ResponseErrors

class GuardMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(self.get_response):
            markcoroutinefunction(self)
        # One-time configuration and initialization.
        self.s = SessionStore()
        self.s.create()

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        #print(request.path)
        #print(ipaddress)
        #print(request.headers)
        #print(request.user)
        #print(request.COOKIES)
        #print(request.session)
        #session_hash = hash(ipaddress + request.headers.get('User-Agent'))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        '''
        if response.status_code in [400, 401, 403, 404, 405, 408, 413, 414, 415, 419, 429, 431, 500, 502, 503, 504, 507, 508, 522, 524, 525, 526]:
            error_response = ResponseErrors.objects.create(
                session_key=self.s.session_key,
                ip=ipaddress,
                user_agent=request.headers.get('User-Agent'),
                error_code=response.status_code,
                request=request
            )
        '''

        return response