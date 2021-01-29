from django.contrib import admin

# Register your models here.

from .models import Institute, Users

class InstituteAdmin(admin.ModelAdmin):
    search_fields = ['name']

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution')

admin.site.register(Users, UserAdmin)
admin.site.register(Institute, InstituteAdmin)
