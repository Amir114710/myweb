from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from account.models import User

class Categories(models.Model):
    title = models.CharField(max_length=50 , null=True , blank=True , verbose_name="نام دسته")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی ها کار ها'
        verbose_name_plural ='تنضیمات قسمت دسته بندی های کاری'

class Work(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True , verbose_name="نام پست")
    english_title = models.CharField(max_length=150 , null=True , blank=True, verbose_name="نام پست به اینگلیسی")
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True, verbose_name="تولید کننده ی محتوا")
    slug = models.SlugField(null=True , blank=True , verbose_name="اسلاگ")
    categories = models.ManyToManyField(Categories , related_name="works", verbose_name="دسته بندی ها")
    image = models.FileField(upload_to='works/image' , null=True , blank=True, verbose_name="عکس1") 
    image2 = models.FileField(upload_to='works/image' , null=True , blank=True, verbose_name="عکس2")
    image3 = models.FileField(upload_to='works/image' , null=True , blank=True, verbose_name="عکس3")
    discription = models.TextField(null=True , blank=True, verbose_name="توضیحات")
    content = models.TextField(null=True , blank=True , verbose_name="توضیحات کامل")
    title_content = models.CharField(max_length=100 , null=True , blank=True , verbose_name="نام برای توضیحات بیشتر")
    meta_content = models.TextField(null=True , blank=True , verbose_name="توضیحات کامل بیشتر")
    detail = models.BooleanField(default=True , null=True , blank=True , verbose_name="دارای بخش توضیحات باشد ؟")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'دسته بندی ها کار ها'
        verbose_name_plural ='تنضیمات قسمت کاری'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Work , self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('work:work_detail' , kwargs={'slug':self.slug})

class Comments(models.Model):
    user = models.ForeignKey(User , related_name="comment" , on_delete=models.CASCADE , verbose_name = 'کاربر')
    works = models.ForeignKey(Work, related_name="comment" , on_delete=models.CASCADE, verbose_name = 'کار ها')

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'replies' , null=True , blank=True, verbose_name = 'پست جواب داده شده')

    message = models.TextField(null=True, blank=True, verbose_name = 'نظرات')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.phone}-{self.works.title}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ('-created',)