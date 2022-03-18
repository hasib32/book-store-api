from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.conf import settings


class UserManger(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves an User with the given email and password

        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        if password:
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves an superuser with the given email

        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user',
        blank=True,
        null=True
    )

    objects = UserManger()
    all_objects = models.Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """
        Is the user a member of staff?
        Simplest possible answer: All admins are staff
        :return:
        """
        return self.is_admin
