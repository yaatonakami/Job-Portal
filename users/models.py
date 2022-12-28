from django.db import models
from datetime import datetime
from django.utils import timezone
import os, random
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import mark_safe
from django.contrib.auth.hashers import make_password, check_password



now = timezone.now()

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.format(imageid = instance, 
    basename = basefilename, randomstring = randomstr, ext = file_extension, year = now.strftime('%Y'), 
    month = now.strftime('%m'), day = now.strftime('%d'))
    
TYPE = {
    (   'Job Seeker', 'Job Seeker'),
    (  'Job Provider', 'Job Provider' ),
}

# class UserManager(models.Manager):
#     def get_by_natural_key(self, username):
#         return self.get(username=username)

class User(models.Model):
    username = models.CharField( max_length = 200, verbose_name = 'Username', blank = True)
    password = models.CharField(max_length = 200, verbose_name = 'Password', blank = True)
    user_fname = models.CharField(max_length = 200, verbose_name = 'First name')
    user_lname = models.CharField(max_length = 200, verbose_name = 'Last name')
    user_initial = models.CharField(max_length = 1, verbose_name = 'Middle initial')
    user_email = models.EmailField(unique = True, max_length = 200, verbose_name = 'Work email address')
    user_pnumber = PhoneNumberField(blank = True, verbose_name = 'Phone number')
    user_image = models.ImageField(upload_to = image_path, default = 'profile_pic/image.png')
    user_type = models.CharField(max_length=100, null=True,    choices = TYPE)
    
    def image_tag(self): 
        return mark_safe('<img src = "/users/media/%s" width="50" height="50" />'%(self.user_image))

    pub_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.user_email


    # is_anonymous = False
    # is_authenticated = False
    # is_active = True
    # is_staff = True

    # def has_module_perms(self, users):
    #     return self.is_staff
    # def get_username(self):
    #     return self.username
    # def has_perm(self, perm, obj=None):
    #     return self.is_staff

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['password','user_fname','user_lname','user_initial','user_email','user_pnumber']

    # objects = UserManager()

    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)







