from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.authtoken.models import Token

from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    ValidationError
)

User = get_user_model()


class UserCreateSerializer(ModelSerializer):

    email2 = EmailField(label='Confirm email')
    password1 = CharField(
        label='Password',
        min_length=6,
        write_only=True
    )
    password2 = CharField(
        label='Confirm password',
        min_length=6,
        write_only=True
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'first_name',
            'last_name',
            'staff',
            'admin',
            'password1',
            'password2',
        ]

    # def validate_email2(self, value):
    #     data = self.get_initial()
    #     email1 = data['email']
    #     email2 = value
    #     if email1 != email2:
    #         raise ValidationError('Emails do not match')
    #     return value

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data['email2']
        email2 = value
        if email1 != email2:
            raise ValidationError('Emails do not match')
        prev_user = User.objects.filter(email=email1)
        if prev_user:
            raise ValidationError("This user already exists.")
        return value

    def validate_password1(self, value):
        data = self.get_initial()
        password2 = data['password2']
        password1 = value
        if password1 != password2:
            raise ValidationError("Passwords do not match")
        return value


    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data["email"]
        password = validated_data['password1']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        admin = validated_data['admin']
        staff = validated_data['staff']

        new_user = User(email=email, username=username, first_name=first_name, last_name = last_name
                        , admin=admin, staff=staff)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserDeleteSerializer(ModelSerializer):
    class Meta:
        model = User


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email address', required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def validate(self, data):
        user_obj = None
        print(data)
        username = data.get('username', None)
        email = data.get('email', None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username/email is required to login.")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        )
        if user.exists() and user.count() != 0:
            user_obj = user.first()
        else:
            raise ValidationError("The username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials. Please try again.")

        try:
            data['token'] = Token.objects.get(user=user_obj)
        except Token.DoesNotExist:
            raise ValidationError("Token absent for user. Please contact admin.")

        return data
