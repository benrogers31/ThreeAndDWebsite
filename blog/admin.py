from django.contrib import admin
from .models import Post, Comment
# Register your models here.

#this basically allows the post table to be checked by the admin 
admin.site.register(Post)
admin.site.register(Comment)
