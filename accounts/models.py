from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone

"""
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('the given username is not valid')
        email = self.normalize_email(email)
        user = self.model(username = username, email=email, is_active=False,is_staff=is_staff, is_superuser=is_superuser,date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields ):
        return self._create_user(username, email, password, is_active=True,is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, is_active=True,is_staff=True, is_superuser=True, **extra_fields)
        user.save(using=self._db)
        return user
ROLES = [
    ('ACCOUNTS','ACCOUNTS'),
    ('MANAGER','MANAGER'),
    ('WORKER','WORKER'),
]

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=30,blank=True, null=True)
    last_name = models.CharField(max_length=30,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    roles = models.CharField(max_length=60, null=True,choices=ROLES)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]


"""