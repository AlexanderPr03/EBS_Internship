# Create your views here.
from apps.users.models import User
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from apps.users.serializers import UserSerializer, MyTokenObtainPairSerializer, UserViewSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(UserSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_superuser=True,
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()

        return Response(UserSerializer(user).data)



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserListView(GenericAPIView):
    serializer_class = UserViewSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        users = User.objects.all()

        return Response(UserViewSerializer(users, many=True).data)

