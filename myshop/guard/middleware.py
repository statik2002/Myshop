from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from asgiref.sync import iscoroutinefunction, markcoroutinefunction

from guard.models import Metrica, RequestHistory

class GuardMiddleware:
    async_capable = True
    sync_capable = False

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(self.get_response):
            markcoroutinefunction(self)
        # One-time configuration and initialization.
        self.s = SessionStore()
        self.s.create()

    async def __call__(self, request):
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
        session_hash = hash(ipaddress + request.headers.get('User-Agent'))

        '''
        metrica, created = await Metrica.objects.aupdate_or_create(
            session_key=self.s.session_key,
            ip=ipaddress,
            user_agent=request.headers.get('User-Agent'),
            defaults={'last_request': timezone.now()}
        )
        request_history = RequestHistory.objects.create(metrica=metrica, path=request.path)
        request_history.save()
        '''


        response = await self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response