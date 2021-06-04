from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from .models import Human, Gender, City, Country, TimeZoneResidence, \
#     LevelLanguage, LevelLanguageTitle, LevelLanguageKnowledge, \
#     LanguageProgramming, FrameworkProgramming, \
#     SkillProgramming, IntervalWork, RateWork
from . import models

# GOST - on serializers.HyperlinkedModelSerializer


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['pk', 'title', 'description', ]


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        fields = ['pk', 'domen', 'title', 'description', ]


class TimeZoneResidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TimeZoneResidence
        fields = ['pk', 'timezone', 'hours', 'description', ]


class CitySerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()
    timezone = TimeZoneResidenceSerializer()

    class Meta:
        model = models.City
        fields = ['pk', 'title', 'description', 'country', 'timezone', ]


class LevelLanguageTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LevelLanguageTitle
        fields = ['pk', 'suffix', 'title', 'description', ]


class LevelLanguageKnowledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LevelLanguageKnowledge
        fields = ['pk', 'title', 'description', ]


class LevelLanguageSerializer(serializers.HyperlinkedModelSerializer):
    level = LevelLanguageTitleSerializer()
    knowledge = LevelLanguageKnowledgeSerializer()

    class Meta:
        model = models.LevelLanguage
        fields = ['pk', 'CEFR', 'level', 'knowledge', 'description', ]


class LanguageProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LanguageProgramming
        fields = ['pk', 'title', 'description', ]


class FrameworkProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageProgrammingSerializer()

    class Meta:
        model = models.FrameworkProgramming
        fields = ['pk', 'title', 'language', 'description', ]


class SkillProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SkillProgramming
        fields = ['pk', 'title', 'description', ]


class IntervalWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.IntervalWork
        fields = ['pk', 'title', 'timeFrom', 'timeTo', 'description', ]


class RateWorkSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageProgrammingSerializer()
    framework = FrameworkProgrammingSerializer()

    class Meta:
        model = models.RateWork
        fields = ['pk', 'title', 'language', 'framework', 'price_dollar', 'price_rub', 'description', ]


class HumanSerializer(serializers.HyperlinkedModelSerializer):
    gender = GenderSerializer()
    city = CitySerializer()
    level_english = LevelLanguageSerializer()
    language_programming = LanguageProgrammingSerializer(read_only=True, many=True)
    framework_programming = FrameworkProgrammingSerializer(read_only=True, many=True)
    skills_programming = SkillProgrammingSerializer(read_only=True, many=True)
    interval_works = IntervalWorkSerializer(read_only=True, many=True)
    rate_works = RateWorkSerializer(read_only=True, many=True)

    class Meta:
        model = models.Human
        fields = ['pk', 'nickname', 'phone', 'email', 'email_first', 'email_second', 'email_third',
                  'surname', 'name', 'middle_name', 'gender', 'city', 'level_english',
                  'language_programming', 'framework_programming', 'skills_programming',
                  'interval_works', 'rate_works', ]



# VIEW - on serializers.HyperlinkedModelSerializer


class GenderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['pk', 'title', 'description', ]


class CountryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ['pk', 'domen', 'title', 'description', ]


class TimeZoneResidenceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeZoneResidence
        fields = ['pk', 'timezone', 'hours', 'description', ]


class CityViewSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    timezone = TimeZoneResidenceSerializer()

    class Meta:
        model = models.City
        fields = ['pk', 'title', 'description', 'country', 'timezone', ]


class LevelLanguageTitleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LevelLanguageTitle
        fields = ['pk', 'suffix', 'title', 'description', ]


class LevelLanguageKnowledgeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LevelLanguageKnowledge
        fields = ['pk', 'title', 'description', ]


class LevelLanguageViewSerializer(serializers.ModelSerializer):
    level = LevelLanguageTitleSerializer()
    knowledge = LevelLanguageKnowledgeSerializer()

    class Meta:
        model = models.LevelLanguage
        fields = ['pk', 'CEFR', 'level', 'knowledge', 'description', ]


class LanguageProgrammingViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LanguageProgramming
        fields = ['pk', 'title', 'description', ]


class FrameworkProgrammingViewSerializer(serializers.ModelSerializer):
    language = LanguageProgrammingSerializer()

    class Meta:
        model = models.FrameworkProgramming
        fields = ['pk', 'title', 'language', 'description', ]


class SkillProgrammingViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillProgramming
        fields = ['pk', 'title', 'description', ]


class IntervalWorkViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IntervalWork
        fields = ['pk', 'title', 'timeFrom', 'timeTo', 'description', ]


class RateWorkViewSerializer(serializers.ModelSerializer):
    language = LanguageProgrammingSerializer()
    framework = FrameworkProgrammingSerializer()

    class Meta:
        model = models.RateWork
        fields = ['pk', 'title', 'language', 'framework', 'price_dollar', 'price_rub', 'description', ]


class HumanViewSerializer(serializers.ModelSerializer):
    gender = GenderSerializer()
    city = CitySerializer()
    level_english = LevelLanguageSerializer()
    language_programming = LanguageProgrammingSerializer(read_only=True, many=True)
    framework_programming = FrameworkProgrammingSerializer(read_only=True, many=True)
    skills_programming = SkillProgrammingSerializer(read_only=True, many=True)
    interval_works = IntervalWorkSerializer(read_only=True, many=True)
    rate_works = RateWorkSerializer(read_only=True, many=True)

    class Meta:
        model = models.Human
        fields = ['pk', 'pk', 'nickname', 'name', 'middle_name', 'gender', 'city', 'level_english',
                  'language_programming', 'framework_programming', 'skills_programming',
                  'interval_works', 'rate_works', ]

# CREATE - on serializers.ModelSerializer


class GenderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = ['pk', 'title', 'description', ]


class CountryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ['pk', 'domen', 'title', 'description', ]


class TimeZoneResidenceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TimeZoneResidence
        fields = ['pk', 'timezone', 'hours', 'description', ]


class CityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ['pk', 'title', 'description', 'country', 'timezone', ]


class LevelLanguageTitleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LevelLanguageTitle
        fields = ['pk', 'suffix', 'title', 'description', ]


class LevelLanguageKnowledgeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LevelLanguageKnowledge
        fields = ['pk', 'title', 'description', ]


class LevelLanguageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LevelLanguage
        fields = ['pk', 'CEFR', 'level', 'knowledge', 'description', ]


class LanguageProgrammingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LanguageProgramming
        fields = ['pk', 'title', 'description', ]


class FrameworkProgrammingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FrameworkProgramming
        fields = ['pk', 'title', 'language', 'description', ]


class SkillProgrammingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillProgramming
        fields = ['pk', 'title', 'description', ]


class IntervalWorkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IntervalWork
        fields = ['pk', 'title', 'timeFrom', 'timeTo', 'description', ]


class RateWorkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RateWork
        fields = ['pk', 'title', 'language', 'framework', 'price_dollar', 'price_rub', 'description', ]


class HumanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Human
        fields = ['pk', 'pk', 'nickname', 'name', 'middle_name', 'gender', 'city', 'level_english',
                  'language_programming', 'framework_programming', 'skills_programming',
                  'interval_works', 'rate_works', ]



#
# class HumanCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Human
#         fields = "__all__"
