from django.contrib import admin
from users.models import User, Masseur


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone',)


@admin.register(Masseur)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
