from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone , password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone=self.normalize_email(phone),
        )

        user.set_password(password)
        # user.set_email(email)
        # user.set_Full_name(Full_name)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='پست الکترونیک',
        max_length=255,
    )
    username = models.CharField(max_length=200, verbose_name='نام کاربری' ,unique=True , null=True, blank=True)
    area_of_activity = models.CharField(max_length=50 , verbose_name='حوضه فعالیت', null=True, blank=True)
    phone = models.CharField(max_length=12 , verbose_name='شماره تلفن', default='0' ,unique=True,)
    image = models.ImageField(upload_to='UserImage' , verbose_name='عکس کاربر' , null=True, blank=True)
    Full_name = models.CharField(max_length=200 , verbose_name='نام کامل' , null=True, blank=True)
    date_of_birth = models.CharField(max_length=100 , verbose_name='تاریخ تولد' , null=True, blank=True)
    birth_place = models.CharField(max_length=100 , verbose_name='مکان تولد' , null=True, blank=True)
    instagram_address = models.TextField(verbose_name='ادرس اینستاگرام', null=True, blank=True)
    is_active = models.BooleanField(default=True , verbose_name='فعال')
    is_admin = models.BooleanField(default=False , verbose_name='ادمین')
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.phone
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural ='کاربر ها'
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin