from rest_framework import JWTauthentication

class CustomJWTAuthentication(JWTauthentication):
    def authenticate(self, request):
        # Custom authentication logic can be implemented here
        return super().authenticate(request)