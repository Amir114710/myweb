from django.db import models

class Activity(models.Model):
    image = models.ImageField(upload_to='about/actitvity_image')
    content = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'فعالیت ها'
        verbose_name_plural ='تنضیمات قسمت فعالیت های من'


class About(models.Model):
    about_content = models.TextField()
    activity = models.ManyToManyField(Activity , related_name='actitvities')

    def __str__(self) -> str:
        return self.about_content[:50]

    class Meta:
        verbose_name = 'درباره ی من'
        verbose_name_plural ='تنضیمات قسمت درباره ی من'

