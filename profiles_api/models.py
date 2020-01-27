from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Difference between AbstractUser and AbstractBaseUser in Django
# https://stackoverflow.com/questions/21514354/difference-between-abstractuser-and-abstractbaseuser-in-django
# PermissionMixin to set permission for our user


class UserProfileManager(BaseUserManager):
    """Manage user profile"""

    def create_user(self, email, name, password):
        """Create a new user profile"""
        if not email:  # if email is not given that raise ValueError
            raise ValueError("User email address is required")

        email = self.normalize_email(email)  # to set email as normalize_email
        user = self.model(email=email, name=name)  # to create new user
        user.set_password(password)  # to set hash password
        user.save(using=self._db)  # to save user in database
        return user

    def create_superuser(self, email, name, password):
        """Create new super user and save with its details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for  users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # We create custom user so that we also create custom model manager as follow
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """To Retrieve user full name """
        return self.name

    def get_short_name(self):
        """To Retrieve user short name here we not take short name os that we return name also"""
        return self.name

    def __str__(self):
        """To return string representation of UserProfile class
        Here we return only email we can also return all attribute of that class """
        return self.email

# Create your models here.
# class Demo(models.Model):
#     name=models.CharField(max_length=25);
#     age=models.IntegerField();
#
#
#     def __str__(self):
#         return self.name+"  "+str(self.age);


# Every time to change model and/or create new model than we must create migrations file
# Migration file will contain the steps required to modify the database to match our
# Updated model
