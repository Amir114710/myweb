from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, username , email , password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=self.normalize_email(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username , password=None):
        """
        Creates and saves a superuser with the given email. and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='ادرس ایمیل',
        max_length=255,
    )
    phone = models.CharField(max_length=13 , verbose_name='شماره تلفن' , null=True , blank=True)
    earea_activity = models.CharField(max_length=150 , verbose_name='حوضه فعالیت' , null=True , blank=True)
    username = models.CharField(max_length=150  , verbose_name='نام کاربری' , unique=True)
    fullname = models.CharField(max_length=50 , verbose_name='نام کامل' , null=True , blank=True)
    image = models.ImageField(upload_to='user/user_image')
    date_of_birth = models.CharField(max_length=100 , null=True , blank=True , verbose_name='تاریخ تولد')
    birth_place = models.CharField(max_length=100 , verbose_name='محل تولد' , null=True , blank=True)
    instagram = models.CharField(max_length=500 , null=True , blank=True , verbose_name='ادرس اینستا')
    github = models.CharField(max_length=500 , null=True , blank=True  , verbose_name='ادرس گیت هاب')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural ='تنضیمات قسمت کاربر '

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
    

class Profile(models.Model):
    email = models.EmailField(
        verbose_name='ادرس ایمیل',
        max_length=255,
    )
    phone = models.CharField(max_length=13 , verbose_name='شماره تلفن' , null=True , blank=True)
    earea_activity = models.CharField(max_length=150 , verbose_name='حوضه فعالیت' , null=True , blank=True)
    username = models.CharField(max_length=150  , verbose_name='نام کاربری' , unique=True)
    fullname = models.CharField(max_length=50 , verbose_name='نام کامل' , null=True , blank=True)
    image = models.ImageField(upload_to='user/user_image')
    date_of_birth = models.CharField(max_length=100 , null=True , blank=True , verbose_name='تاریخ تولد')
    birth_place = models.CharField(max_length=100 , verbose_name='محل تولد' , null=True , blank=True)
    instagram = models.CharField(max_length=500 , null=True , blank=True , verbose_name='ادرس اینستا')
    github = models.CharField(max_length=500 , null=True , blank=True  , verbose_name='ادرس گیت هاب')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural ='تنضیمات قسمت پروفایل '