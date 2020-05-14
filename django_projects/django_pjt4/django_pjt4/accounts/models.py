from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, gender, age, password=None):
        if not email :
            raise ValueError('must have user email')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            gender = gender,
            age = age,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, gender, age, password ):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            gender = gender,
            age = age,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser,PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )

    GENDER_CHOICES = {
      ('male','남성'), #오른쪽에 있는 것이 화면에 보인다.
      ('female', '여성'),
    }
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name='followings'
        )
    age = models.IntegerField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','gender','age']
