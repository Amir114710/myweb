from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=150 , null=True ,  blank=True , verbose_name='نام کاربر')
    email = models.EmailField(null=True ,  blank=True , verbose_name='ایمیل کاربر')
    message = models.TextField(null=True ,  blank=True , verbose_name='پیام کاربر')
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.username}-{self.message}'
       
    class Meta:
        ordering = ("-created",)
        verbose_name = "تماس با من"
        verbose_name_plural = "تنظیمات قسمت تماس با من"