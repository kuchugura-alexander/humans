from django.contrib import admin
from django.utils.crypto import get_random_string

# Register your models here.
from .models import (
    Token, Human, Gender,
    City, Country, TimeZoneResidence,
    LevelLanguage, LevelLanguageTitle, LevelLanguageKnowledge,
    LanguageProgramming, FrameworkProgramming,
    SkillProgramming, IntervalWork, RateWork
)


class TokenAdmin(admin.ModelAdmin):
    model = Token
    list_display = ['active', 'token']
    readonly_fields = ['created_at', 'modified_at']

    def save_model(self, request, obj, form, change):
        if obj.token == "":
            new_token = ""
            query_token = ["tok"]
            while len(query_token):
                new_token = get_random_string(length=33)
                query_token = Token.objects.filter(token=new_token)
            obj.token = new_token
        obj.save()


class HumanAdmin(admin.ModelAdmin):
    model = Human
    list_display = ['nickname', 'surname', 'name', 'middle_name', 'email', 'phone']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class GenderAdmin(admin.ModelAdmin):
    model = Gender
    list_display = ['title', 'description']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['title', 'country', 'timezone']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['domen', 'title', 'description']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class TimeZoneResidenceAdmin(admin.ModelAdmin):
    model = TimeZoneResidence
    list_display = ['timezone', 'hours', 'description']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class LevelLanguageAdmin(admin.ModelAdmin):
    model = LevelLanguage
    list_display = ['level', 'knowledge', 'description']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class LevelLanguageTitleAdmin(admin.ModelAdmin):
    model = LevelLanguageTitle
    list_display = ['suffix', 'title']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class LevelLanguageKnowledgeAdmin(admin.ModelAdmin):
    model = LevelLanguageTitle
    list_display = ['title']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class FrameworkProgrammingAdmin(admin.ModelAdmin):
    model = FrameworkProgramming
    list_display = ['title']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class LanguageProgrammingAdmin(admin.ModelAdmin):
    model = LanguageProgramming
    list_display = ['title', 'language']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class SkillProgrammingAdmin(admin.ModelAdmin):
    model = SkillProgramming
    list_display = ['title']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class IntervalWorkAdmin(admin.ModelAdmin):
    model = IntervalWork
    list_display = ['title', 'timeFrom', 'timeTo']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


class RateWorkAdmin(admin.ModelAdmin):
    model = RateWork
    list_display = ['title', 'language', 'framework', 'price_dollar', 'price_rub']
    readonly_fields = ['created_at', 'modified_at', 'token']
    # list_filter=['date']


admin.site.register(Token, TokenAdmin)
admin.site.register(Human, HumanAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(TimeZoneResidence, TimeZoneResidenceAdmin)
admin.site.register(LevelLanguage, LevelLanguageAdmin)
admin.site.register(LevelLanguageTitle, LevelLanguageTitleAdmin)
admin.site.register(LevelLanguageKnowledge, LevelLanguageKnowledgeAdmin)
admin.site.register(FrameworkProgramming, LanguageProgrammingAdmin)
admin.site.register(LanguageProgramming, FrameworkProgrammingAdmin)
admin.site.register(SkillProgramming, SkillProgrammingAdmin)
admin.site.register(IntervalWork, IntervalWorkAdmin)
admin.site.register(RateWork, RateWorkAdmin)


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name = "Отдел"
    verbose_name_plural = 'Отделы'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        # if request.user.is_superuser:
        if request.user.username == "admin":
            print(qs)
            return qs
        else:
            # return qs.filter(is_superuser=False)
            return qs.exclude(username="admin")
    inlines = (EmployeeInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
