from django.db import models
from django.utils.text import slugify
from account.models import User

class Categories(models.Model):
    title = models.CharField(max_length=50 , null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی ها کار ها'
        verbose_name_plural ='تنضیمات قسمت دسته بندی های کاری'

class Work(models.Model):
    title = models.CharField(max_length=150 , null=True , blank=True)
    english_title = models.CharField(max_length=150 , null=True , blank=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    slug = models.SlugField(null=True , blank=True )
    categories = models.ManyToManyField(Categories , related_name="works")
    image = models.FileField(upload_to='works/image')
    discription = models.TextField(null=True , blank=True)
    content = models.TextField(null=True , blank=True)
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

