from django.contrib import admin

from service.models import Services, Apppointment


# Register your models here.
@admin.register(Services)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'price')


@admin.register(Apppointment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('date', 'course', 'masseur',  'name', 'surname', 'phone')
