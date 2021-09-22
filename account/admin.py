#from django.contrib import admin

from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):#ImportExportModelAdmin):#admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name',)

