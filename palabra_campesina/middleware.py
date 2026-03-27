from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class SitePasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        session_password_saved = request.session.get('site_password')

        if (session_password_saved) or (request.path == reverse('contraseña_or_password')):
            return self.get_response(request)

        if (request.path == reverse('contraseña_or_password')):
            return self.get_response(request)

        # if no session password saved, redirect to login
        if not session_password_saved:
                return redirect('contraseña_or_password')

        return self.get_response(request)
