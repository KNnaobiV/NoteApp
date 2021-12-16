from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, 
    date_of_birth, password=None):
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')
        
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth, first_name=first_name,
            last_name=last_name, username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, 
    email, date_of_birth, password=None):
        user = self.create_user(first_name=first_name, last_name=last_name,
        date_of_birth=date_of_birth, username=username,
         email=email, password=password,)
        user.is_admin=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
            unique=True, max_length=255,)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=50)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS =['date_of_birth','first_name', 'last_name', 'email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('accounts:profile', args=[self.pk,])

    def has_perm(self, obj=None):
        return True

    def has_module_perms(self, admin):
        return True

    @property
    def is_staff(self):
        return self.is_admin

        


#Next time use base user manager to handle user management