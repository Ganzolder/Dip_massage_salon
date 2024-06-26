from django.contrib import admin
from users.models import User, Speciality, Masseur


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone',)


@admin.register(Speciality)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Masseur)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'speciality')
