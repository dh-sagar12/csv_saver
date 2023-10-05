from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.




class CustomAccountManager(BaseUserManager):
    def create_user(self,  email, first_name,  last_name, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, first_name, last_name and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name= first_name,
            last_name = last_name, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


        
    def create_superuser(self, email, first_name, last_name, password ):

        user=  self.create_user( email=email,first_name=first_name, last_name=last_name,  password=password)

        user.is_staff =  True
        user.is_superuser =  True
        user.is_active =  True
        user.is_customer =  False
        user.gender  = 'O'
        user.save()
        
        if user.is_superuser is not True:
            raise ValueError('Superuser must be assigned to is_superuser True')

        
        if user.is_staff is not True:
            raise ValueError('Superuser must be assigned to is_staff True')
        


class User(AbstractBaseUser, PermissionsMixin):
    id  =  models.BigAutoField(primary_key=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name =  models.CharField(blank=False, null=False, max_length=50)
    middle_name =  models.CharField(blank=True, null=True,  max_length=50)
    last_name = models.CharField(null=False, blank=False,  max_length=50)
    date_of_birth =  models.DateField(null=True, blank=True)
    is_staff  =  models.BooleanField(default=False, null=False, blank=False)
    is_customer =  models.BooleanField(default=True, null=False, blank=False)
    profile_picture =  models.ImageField(upload_to='Avatars/',  blank=True)
    
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), (GENDER_OTHER, 'Other')]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=5, null=False, blank=False)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


    class Meta:
        db_table = 'users'