from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from .models import UserProfile, Brewery
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class RegisterView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={200: 'Registration successful', 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful'})
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password')
            },
            required=['username', 'password']
        ),
        responses={200: 'Login successful', 401: 'Login failed'}
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            print("Generated Token:", token)
            #
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.auth_token = token
            user_profile.save()
            #
            return Response({'message': 'Login successful', 'token': token})
        return Response({'message': 'Login failed'}, status=401)

class BreweriesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        security=[{"Bearer": []}],  # Require Bearer token
        manual_parameters=[
            openapi.Parameter('query', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request):
        query = request.GET.get('query', '')  # Get the query parameter from the request
        api_url = f'https://api.openbrewerydb.org/breweries/search?query={query}'
        response = requests.get(api_url)
        data = response.json()

        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

        for brewery_data in data:
            id = brewery_data.get('id')
            brewery, _ = Brewery.objects.get_or_create(id=id)
            brewery.users_interacted.add(user_profile)  # Add the user profile to the many-to-many relationship

        return Response(data)






