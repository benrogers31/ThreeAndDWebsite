"""django_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path , include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #***** What ever route you want to be the homepage have the path ''*****#
    
    path('admin/', admin.site.urls),
    #when someone types in /blog they look at the include statement then send them to blog.urls
    # it will only send whats remaining in the url to blog.urls
    ###### instead of making out blog a sub app its the homepage so instead of /blog its gonna be '' 
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    # authviews is a django speciality for loging in that we are implementing
    # we are storing this in a different location so we need to store the name
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    ####### NEED ALL OF THESE FOR RESETTING PASSWORD ########
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), 
        name='password_reset'),
    path('password-reset/done', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), 
        name='password_reset_done'),
    #these params are for security
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), 
        name='password_reset_complete'),
    #################
    path('', include('blog.urls')),

    #This is for the ckeditor
    #path('ckeditor/',include('ckeditor_uploader.urls')),
  
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#this line above ensures the images can be recieved in development mode

##### this imports the ckeditor but doesnt use the default implementation #####
##### The defualt only let admin users upload pictures ######
from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload
from django.conf.urls import url

urlpatterns += [
    url(r'^ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

#this is how we access the images when we are in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##############################
