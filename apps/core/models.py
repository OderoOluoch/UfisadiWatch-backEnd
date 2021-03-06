from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

class UserAccountManager(BaseUserManager):
    def create_user(self, email,username, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have a username.')
        if not first_name:
            raise ValueError('User must have a firstname.')
        if not last_name:
            raise ValueError('User must have a lastname.')

        user = self.model(
            email = self.normalize_email(email),
            username= username,
            first_name= first_name,
            last_name= last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name,last_name, username, password):
        user = self.create_user(
                email = self.normalize_email(email),
                username= username,
                first_name = first_name,
                last_name = last_name,
                password = password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=20, unique=True)

    created_at = models.DateTimeField(verbose_name='created-on', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last-login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #LOGINFIELD
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_email(self):
        return self.email
    
    
    
class UserType(models.Model):
    is_public= models.BooleanField(default=False)
    is_eacc = models.BooleanField(default=False)
    user = models.OneToOneField(User, related_name='type', on_delete=models.CASCADE)

    def __str__(self):
        if self.is_manager == True:
            return User.get_email(self.user) + '- is_manager'
        elif self.is_cm == True:
            return User.get_email(self.user) + '- is_ceo'
        elif self.is_ceo == True:
            return User.get_email(self.user) + '- is_ceo'
        elif self.is_admin:
            return User.get_email(self.user) + '- is_admin'
        else:
            return f"{self.user} has no type"


