from django.urls import path
from . import views

app_name = 'breweries'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('breweries/', views.BreweriesAPIView.as_view(), name='breweries_api'),
]
