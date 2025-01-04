import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.conf import settings
from users.models import Utilisateur
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.generics import GenericAPIView,CreateAPIView
from .serializers import AuthenticationSerializer,AccountRegistrationSerializer




    
class LoginUserView(GenericAPIView):
    serializer_class = AuthenticationSerializer

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    



class ForgotPasswordView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data.get('email')
        
        if not email:
            return JsonResponse({'error': 'Email is required.'}, status=400)

        try:
            utilisateur = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            return JsonResponse({'error': 'User does not exist.'}, status=400)

        reset_token = get_random_string(length=6)
        utilisateur.reset_token = reset_token  # Assuming you have added this field to the Utilisateur model

        try:
            utilisateur.save()
        except Exception as e:
            return JsonResponse({'error': 'Failed to save reset token: ' + str(e)}, status=500)

        try:
            send_mail(
                'Password Reset',
                f'Use this token to reset your password: {reset_token}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({'error': 'Failed to send reset email: ' + str(e)}, status=500)

        return JsonResponse({'message': 'Password reset token sent successfully.'})
      

class ResetPasswordView(View):
    def post(self, request):
        data = json.loads(request.body)
        reset_token = data.get('reset_token')
        new_password = data.get('new_password')

        if not reset_token or not new_password:
            return JsonResponse({'error': 'Token and new password are required.'}, status=400)

        try:
            utilisateur = Utilisateur.objects.get(reset_token=reset_token)
        except Utilisateur.DoesNotExist:
            return JsonResponse({'error': 'Invalid token.'}, status=400)

        try:
            utilisateur.password = make_password(new_password)
            utilisateur.reset_token = ''  # Clear the reset token after successful password reset
            utilisateur.save()
        except Exception as e:
            return JsonResponse({'error': 'Failed to reset password: ' + str(e)}, status=500)

        return JsonResponse({'message': 'Password reset successful.'})





class ChangePasswordView(APIView):
    def put(self, request, *args, **kwargs):
        utilisateur_id = request.data.get('user_id')
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        # Basic validation of input fields
        if not utilisateur_id:
            return Response({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not current_password:
            return Response({"detail": "Current password is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not new_password:
            return Response({"detail": "New password is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            utilisateur = Utilisateur.objects.get(id=utilisateur_id)
        except Utilisateur.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the current password matches
        if not utilisateur.check_password(current_password):
            return Response({"detail": "Current password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure new password meets minimum length requirement
        if len(new_password) < 8:
            return Response({"detail": "New password must be at least 8 characters long."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Set and save the new password
            utilisateur.set_password(new_password)
            utilisateur.save()
            return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)
        except ValidationError as ve:
            # Handle password validation error (if any)
            return Response({"detail": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Catch-all for any other errors
            return Response({"detail": "An error occurred while changing the password: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResendTokenView(View):
    def post(self, request):
        # Get email from session
        email = request.session.get('activation_email')

        if not email:
            return JsonResponse({'error': 'Email is required.'}, status=400)

        try:
            utilisateur = Utilisateur.objects.get(email=email)  # Get the utilisateur by email
        except Utilisateur.DoesNotExist:
            return JsonResponse({'error': 'User does not exist.'}, status=400)

        # Generate a new activation token
        activation_token = get_random_string(length=32)  # Generate a random token
        utilisateur.activation_token = activation_token  # Update the utilisateur's token
        utilisateur.save()  # Save the utilisateur with the new token

        # Send activation email
        try:
            send_mail(
                'Activate Your Account',
                f'Use this token to activate your account: {activation_token}',
                settings.DEFAULT_FROM_EMAIL,  # The sender email
                [email],  # Recipient email
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({'error': 'Failed to send activation email: ' + str(e)}, status=500)

        return JsonResponse({'message': 'Activation token resent successfully.'}, status=200)
