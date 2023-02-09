from django.db import models
from django.urls import reverse
from account.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100 , null=True , blank=True , verbose_name="نام پست")
    english_title = models.CharField(max_length=100 , null=True , blank=True , verbose_name="نام پست به اینگلیسی")
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True , verbose_name="تهیه کننده پست")
    slug = models.SlugField(null=True , blank=True , verbose_name="اسلاگ")
    image = models.FileField(upload_to='blog/image' , null=True , blank=True , verbose_name="عکس1")
    image2 = models.FileField(upload_to='blog/image' , null=True , blank=True , verbose_name="عکس2")
    image3 = models.FileField(upload_to='blog/image' , null=True , blank=True , verbose_name="عکس3")
    discription = models.TextField(null=True , blank=True , verbose_name="توضیحات")
    content = models.TextField(null=True , blank=True , verbose_name="بدنه پست")
    meta_title = models.CharField(max_length=100 , null=True , blank=True , verbose_name="نام دیگر")
    meta_content = models.TextField(null=True , blank=True , verbose_name="توضیحات بیشتر")
    date_published = models.CharField(max_length=100 , null=True , blank=True , verbose_name="ماه زمان اراعه پست")
    number_date = models.SmallIntegerField(null=True , blank=True , verbose_name="روز اراعه پست")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'وبلاگ'
        verbose_name_plural ='تنضیمات قسمت وبلاگ'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Post , self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:blog_detail' , kwargs={'slug':self.slug})
    
class PostComments(models.Model):
    user = models.ForeignKey(User , related_name="comments" , on_delete=models.CASCADE , verbose_name = 'کاربر')
    posts = models.ForeignKey(Post , related_name="comments" , on_delete=models.CASCADE, verbose_name = 'کار ها')

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'replies' , null=True , blank=True, verbose_name = 'پست جواب داده شده')

    message = models.TextField(null=True, blank=True, verbose_name = 'نظرات')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.phone}-{self.posts.title}'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = "تنظیمات قسمت نظرات"
        ordering = ('-created',)

class PostLike(models.Model):
    users = models.ForeignKey(User , related_name='likes' , on_delete=models.CASCADE , verbose_name = 'کاربر')
    posts = models.ForeignKey(Post , related_name='likes' , on_delete=models.CASCADE , verbose_name = 'کار ها')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.users.username} - {self.posts.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "تنظیمات قسمت لایک ها"
        ordering = ("-created",)