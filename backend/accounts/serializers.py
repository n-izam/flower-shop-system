from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims directly into the decoded JWT payload
        token['username'] = user.username
        token['role'] = user.role
        token['shop_id'] = user.shop.id if user.shop else None
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Add extra user metadata directly to the HTTP JSON response body
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'role': self.user.role,
            'shop_id': self.user.shop.id if self.user.shop else None,
            'shop_name': self.user.shop.name if self.user.shop else "All Shops (Global/Owner)",
        }
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer