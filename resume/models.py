from django.db import models
from django.utils.text import slugify
from account.models import User

class Skill(models.Model):
    title = models.CharField(max_length=100 , null=True , blank=True , verbose_name='مهارت')
    persent = models.SmallIntegerField(null=True , blank=True , verbose_name='درصد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural ='تنضیمات قسمت مهارت های من'

class ResumePost(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name='اسم ها')
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True , verbose_name='تولید کننده محتوا' )
    english_title = models.CharField(max_length=200 , null=True , blank=True)
    slug = models.SlugField(null=True , blank=True)
    file = models.FileField(upload_to='resume/image' , verbose_name='فایل ها')
    image_first = models.ImageField(upload_to='resume/image' , verbose_name='عکس 1' , null=True , blank=True )
    image_seconde = models.ImageField(upload_to='resume/image' , verbose_name='عکس 2' , null=True , blank=True )
    discription = models.TextField(null=True , blank=True , verbose_name='توضیحات')
    content = models.TextField(null=True , blank=True , verbose_name='توضیحات بیشتر')
    instagram = models.CharField(max_length=500 , null=True , blank=True , verbose_name='ادرس اینستاگرام')
    github = models.CharField(max_length=1000 , null=True , blank=True , verbose_name='ادرس گیت هاب')
    linkdin = models.CharField(max_length=1000 , null=True , blank=True , verbose_name='ادرس لینکدین')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'رزومه'
        verbose_name_plural ='تنضیمات قسمت رزومه های من'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(ResumePost , self).save(*args, **kwargs)
