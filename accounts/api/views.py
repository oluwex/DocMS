from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, UpdateAPIView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)

from .serializers import (
    UserCreateSerializer,
    UserStaffAdminCreateSerializer,
    UserDetailSerializer,
    UserDeleteSerializer,
    UserLoginSerializer,
    UserChangePasswordSerializer,
)

from .permissions import IsOwnProfileOrAdmin

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]


class UserStaffAdminCreateAPIView(CreateAPIView):
    serializer_class = UserStaffAdminCreateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, ]


class UserDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnProfileOrAdmin, ]
    lookup_field = 'username'


class UserDeleteAPIView(DestroyAPIView):
    serializer_class = UserDeleteSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, ]
    lookup_field = 'username'


class UserChangePasswordAPIView(UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnProfileOrAdmin, ]
    lookup_field = 'username'


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data,
                            status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
