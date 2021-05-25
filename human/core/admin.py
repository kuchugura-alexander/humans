from django.contrib import admin

# Register your models here.
from .models import Human, Gender, \
    City, Country, TimeZoneResidence, \
    LevelLanguage, LevelLanguageTitle, LevelLanguageKnowledge, \
    LanguageProgramming, FrameworkProgramming, \
    SkillProgramming, IntervalWork, RateWork


class HumanAdmin(admin.ModelAdmin):
    model = Human
    list_display = ['nickname', 'surname', 'name', 'middle_name', 'email', 'phone']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class GenderAdmin(admin.ModelAdmin):
    model = Gender
    list_display = ['gender', 'description']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['title', 'country', 'timezone']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['domen', 'title', 'description']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class TimeZoneResidenceAdmin(admin.ModelAdmin):
    model = TimeZoneResidence
    list_display = ['timezone', 'hours', 'description']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class LevelLanguageAdmin(admin.ModelAdmin):
    model = LevelLanguage
    list_display = ['level', 'description']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class LevelLanguageTitleAdmin(admin.ModelAdmin):
    model = LevelLanguageTitle
    list_display = ['suffix', 'title']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class LevelLanguageKnowledgeAdmin(admin.ModelAdmin):
    model = LevelLanguageTitle
    list_display = ['title']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class FrameworkProgrammingAdmin(admin.ModelAdmin):
    model = FrameworkProgramming
    list_display = ['title']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class LanguageProgrammingAdmin(admin.ModelAdmin):
    model = LanguageProgramming
    list_display = ['title', 'language']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class SkillProgrammingAdmin(admin.ModelAdmin):
    model = SkillProgramming
    list_display = ['title']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class IntervalWorkAdmin(admin.ModelAdmin):
    model = IntervalWork
    list_display = ['title', 'timeFrom', 'timeTo']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


class RateWorkAdmin(admin.ModelAdmin):
    model = RateWork
    list_display = ['title', 'language', 'framework', 'price_dollar', 'price_rub']
    readonly_fields = ['created_at', 'modified_at']
    # list_filter=['date']


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
