from django.contrib import admin

from .models import Commands, Articles
# Register your models here.

admin.site.register(Commands)
admin.site.register(Articles)