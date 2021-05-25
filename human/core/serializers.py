from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Human, Gender, City, Country, TimeZoneResidence, \
    LevelLanguage, LevelLanguageTitle, LevelLanguageKnowledge, \
    LanguageProgramming, FrameworkProgramming, \
    SkillProgramming, IntervalWork, RateWork


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender', 'description', ]


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['domen', 'title', 'description', ]


class TimeZoneResidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeZoneResidence
        fields = ['timezone', 'hours', 'description', ]


class CitySerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()
    timezone = TimeZoneResidenceSerializer()

    class Meta:
        model = City
        fields = ['title', 'description', 'country', 'timezone', ]


class LevelLanguageTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelLanguageTitle
        fields = ['suffix', 'title', 'description', ]


class LevelLanguageKnowledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelLanguageKnowledge
        fields = ['title', 'description', ]


class LevelLanguageSerializer(serializers.HyperlinkedModelSerializer):
    level = LevelLanguageTitleSerializer()
    knowledge = LevelLanguageKnowledgeSerializer()

    class Meta:
        model = LevelLanguage
        fields = ['CEFR', 'level', 'knowledge', 'description', ]


class LanguageProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageProgramming
        fields = ['title', 'description', ]


class FrameworkProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageProgrammingSerializer()

    class Meta:
        model = FrameworkProgramming
        fields = ['title', 'language', 'description', ]


class SkillProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillProgramming
        fields = ['title', 'description', ]


class IntervalWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntervalWork
        fields = ['title', 'timeFrom', 'timeTo', 'description', ]


class RateWorkSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageProgrammingSerializer()
    framework = FrameworkProgrammingSerializer()

    class Meta:
        model = RateWork
        fields = ['title', 'language', 'framework', 'price_dollar', 'price_rub', 'description', ]


class HumanSerializer(serializers.HyperlinkedModelSerializer):
    gender = GenderSerializer()
    city = CitySerializer()
    level_english = LevelLanguageSerializer()
    language_programming = LanguageProgrammingSerializer()
    # language_programming = "qweqwe" # GenderSerializer()
    # framework_programming = FrameworkProgrammingSerializer()
    framework_programming = "qweqwe" # GenderSerializer()
    skills_programming = SkillProgrammingSerializer()
    interval_works = IntervalWorkSerializer()
    # rate_works = RateWorkSerializer()
    rate_works = "qweqwe" # GenderSerializer()

    class Meta:
        model = Human
        fields = ['nickname', 'phone', 'email', 'email_first', 'email_second', 'email_third',
                  'surname', 'name', 'middle_name', 'gender', 'city', 'level_english',]
                  # 'language_programming', 'framework_programming', 'skills_programming',
                  # 'interval_works', 'rate_works', ]
