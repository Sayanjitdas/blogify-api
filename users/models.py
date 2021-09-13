from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


def upload_profile_pic(instance, filename):

    return f'profile_pic/{instance.email}.jpg'


class BlogifyUserManager(BaseUserManager):

    """
    This class inherits the BaseUserManager for Custom User Model
    and overrides the create_user and create_superuser method 
    """

    def create_user(self, email, password, **extrafields):

        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email), **extrafields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extrafields):

        # using the above create_user function

        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extrafields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        user = self.create_user(
            email,
            password=password,
            **extrafields
        )
        return user


class BlogifyUser(AbstractUser):

    """
    The custom user model which replaces username with email

    """
    username = None
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(
        upload_to=upload_profile_pic, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BlogifyUserManager()  # adding the custom user manager to model objects

    def __str__(self):
        return self.email
