import logging

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        return response

class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        if authorization_header:
            auth_token = authorization_header.split(' ')[1]  # Get the token part
            try:
                user = User.objects.get(auth_token=auth_token)
                request.user = user  # Attach user object to request
            except User.DoesNotExist:
                pass  # Token is invalid, but continue processing the request

        response = self.get_response(request)
        return response