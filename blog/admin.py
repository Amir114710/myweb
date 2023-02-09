from django.contrib import admin
from .models import Post , PostLike , PostComments

admin.site.register(Post)
admin.site.register(PostComments)
admin.site.register(PostLike)
