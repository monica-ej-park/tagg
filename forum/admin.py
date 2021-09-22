#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Thread

class ThreadAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Thread, ThreadAdmin)
