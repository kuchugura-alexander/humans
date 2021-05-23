from django.contrib import admin

# Register your models here.

from .models import Human, Gender


class HumanAdmin(admin.ModelAdmin):
    model = Human
    list_display = ['nickname', 'surname', 'name', 'middle_name', 'email']
    readonly_fields = ['pub_date']
    # list_filter=['date']


admin.site.register(Human, HumanAdmin)


class GenderAdmin(admin.ModelAdmin):
    model = Gender
    list_display = ['gender', 'description']
    readonly_fields = ['pub_date']
    # list_filter=['date']


admin.site.register(Gender, GenderAdmin)
