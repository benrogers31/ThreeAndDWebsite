from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .fields import NonStrippingTextField




class MyAccountManager(BaseUserManager):
    #Methods that need to be overridden in BaseUserManager
    
    #just required information is here
    def create_user(self,email,username, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")



        user = self.model(
            #normalizes all letters in email to lower case
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,username, password):
        user = self.create_user(
            #normalizes all letters in email to lower case
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

#We are making our own custom user in this
class Account(AbstractBaseUser):
    #these are all required to extend the absract class  
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=25, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #these are the things we want to add
    display_name = NonStrippingTextField(default=username)
    is_author = models.BooleanField(default=False)

    #this is what the user can use to log in with
    USERNAME_FIELD = 'username'
    
    objects = MyAccountManager()

    REQUIRED_FIELDS = ['email', ]

    #methods needed to fill to extend abstract class
    def __str__(self):
        return self.email

    def has_perm(self, perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    #this ensures a user only has one profile
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    #setting an image feild and making the default deafault.jpg
    #profile_pics will be the directory images get stored in when we upload a profile 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #this is basically how the profile will look as a string 
    def __str__(self):
        return f'{self.user.username} Profile'

    #this is being overridden
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #getting the image that we saved
        img = Image.open(self.image.path)
        #resizing our images
        #there is a bunch of ways to do this so we can look into it
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
