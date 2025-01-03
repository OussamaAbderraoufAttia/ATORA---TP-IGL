from django.contrib import admin
from django.urls import path, include
from .views import LoginUserView,NewDpiView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
   path('login/', LoginUserView.as_view(), name='authenticate-user'),
   path('newdpi/', NewDpiView.as_view(), name='new-dpi'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   
]
