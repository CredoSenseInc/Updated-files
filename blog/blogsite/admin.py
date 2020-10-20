from django.contrib import admin
from blogsite.models import Post
from blogsite.models import Comment


# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
