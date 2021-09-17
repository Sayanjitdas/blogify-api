from django.urls import path
from .views import UserRegistrationAPIView,UserDetailsAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/',UserRegistrationAPIView.as_view(),name='signup'),
    path('login/',obtain_auth_token,name='login'),
    path('obtain-user-details/',UserDetailsAPIView.as_view(),name='user-details')
]