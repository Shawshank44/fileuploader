from django.contrib import admin

from myfiles.models import User_files

# Register your models here.
@admin.register(User_files)

class file_ModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','mobile','email','image','myfile']
