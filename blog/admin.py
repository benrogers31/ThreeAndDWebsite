from django.contrib import admin
from .models import Post 
# Register your models here.

#this basically allows the post table to be checked by the admin 
admin.site.register(Post)
