from django.contrib import admin
from .models import User
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

admin.site.site_header = 'Job Portal Admin'
admin.site.site_title = 'Job Portal Admin Area'
admin.site.index_title = 'Welcome to Job Portal Admin Area'



class UserAdmin(admin.ModelAdmin):
    radio_fields = {"user_type": admin.HORIZONTAL}
    list_display = ['image_tag','user_fname', 'user_lname', 'user_initial','username', 'password',  'user_email', 
    'user_email', 'user_pnumber', 'pub_date']
    search_fields = ['user_fname', 'user_lname', 'username', 'user_email', 'pub_date', 'user_pnumber']

admin.site.register(User, UserAdmin)



