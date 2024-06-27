from django.contrib import admin
from users.models import User, Course, Masseur


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone',)


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Masseur)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'course')
