from django.db import models
from django.utils import timezone
#this imports the user table that django already works well with
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation



#things that we need to save: Users, posts -> users already have their thing in django so we are gonna work with posts to start

#this is a class post that inherits from class model
#each class is going to be it's own table in the database 
#each attribute will be its own feild in the database
class Post(models.Model):
    
    #A good rule of thumb is that you use CharField when you need to limit the maximum length, TextField otherwise. 
    title = models.CharField(max_length = 100)
    summary = models.TextField(default="Whoops our author forgot to put a summary... Roast them in the comment secton!")
    #this is such that the text feild has more functionality than a regular text feild  
    content = RichTextUploadingField() 
    #auto_now = changes evertime updated, auto_now_add is only there when it is initialized
    #default = timezone.now takes timezone into account, and only passes the function doesnt execute it 
    date_posted = models.DateTimeField(default = timezone.now)
    # User is foreign key for author, on_delete means when user is deleted then what do we do
    # in this case CASCADE means we also delete the post 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #storing default height and widths for our header images
    image_width = models.IntegerField(default=2560)
    image_height = models.IntegerField(default=1440)
    #this is our header image 
    header_image = models.ImageField(
        default = "default_header.png",
        upload_to="blog_headers",
        width_field="image_width",
        height_field="image_height",
    )

    #this function basically states how the object will be presented as a string 
    def __str__(self):
        return self.title

    #get the url for a specific post and return it as a string 
    #the view will handle the redirect 
    def get_absolute_url(self):
        #gets the full path to post-detail with the primary key in the url
        return reverse('post-detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    content = models.TextField(max_length=10000,default="3&D")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)