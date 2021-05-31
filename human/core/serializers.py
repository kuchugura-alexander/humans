from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Human, Gender, City, Country, TimeZoneResidence, \
    LevelLanguage, LevelLanguageTitle, LevelLanguageKnowledge, \
    LanguageProgramming, FrameworkProgramming, \
    SkillProgramming, IntervalWork, RateWork


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['pk', 'url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['pk', 'url', 'name']

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['pk', 'title', 'description', ]


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['pk', 'domen', 'title', 'description', ]


class TimeZoneResidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeZoneResidence
        fields = ['pk', 'timezone', 'hours', 'description', ]


class CitySerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer()
    timezone = TimeZoneResidenceSerializer()

    class Meta:
        model = City
        fields = ['pk', 'title', 'description', 'country', 'timezone', ]


class LevelLanguageTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelLanguageTitle
        fields = ['pk', 'suffix', 'title', 'description', ]


class LevelLanguageKnowledgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelLanguageKnowledge
        fields = ['pk', 'title', 'description', ]


class LevelLanguageSerializer(serializers.HyperlinkedModelSerializer):
    level = LevelLanguageTitleSerializer()
    knowledge = LevelLanguageKnowledgeSerializer()

    class Meta:
        model = LevelLanguage
        fields = ['pk', 'CEFR', 'level', 'knowledge', 'description', ]


class LanguageProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LanguageProgramming
        fields = ['pk', 'title', 'description', ]


class FrameworkProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageProgrammingSerializer()

    class Meta:
        model = FrameworkProgramming
        fields = ['pk', 'title', 'language', 'description', ]


class SkillProgrammingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillProgramming
        fields = ['pk', 'title', 'description', ]


class IntervalWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntervalWork
        fields = ['pk', 'title', 'timeFrom', 'timeTo', 'description', ]


class RateWorkSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageProgrammingSerializer()
    framework = FrameworkProgrammingSerializer()

    class Meta:
        model = RateWork
        fields = ['pk', 'title', 'language', 'framework', 'price_dollar', 'price_rub', 'description', ]


# class HumanAllInfoSerializer(serializers.HyperlinkedModelSerializer):
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
        model = Human
        fields = ['pk', 'nickname', 'phone', 'email', 'email_first', 'email_second', 'email_third',
                  'surname', 'name', 'middle_name', 'gender', 'city', 'level_english',
                  'language_programming', 'framework_programming', 'skills_programming',
                  'interval_works', 'rate_works', ]


# # class HumanMiniInfoSerializer(serializers.HyperlinkedModelSerializer):
# class HumanSerializer(serializers.HyperlinkedModelSerializer):
#     gender = GenderSerializer()
#     city = CitySerializer()
#     level_english = LevelLanguageSerializer()
#     language_programming = LanguageProgrammingSerializer(read_only=True, many=True)
#     framework_programming = FrameworkProgrammingSerializer(read_only=True, many=True)
#     skills_programming = SkillProgrammingSerializer(read_only=True, many=True)
#     interval_works = IntervalWorkSerializer(read_only=True, many=True)
#     rate_works = RateWorkSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Human
#         fields = ['pk', 'pk', 'nickname', 'surname', 'name', 'middle_name', 'gender', 'city', 'level_english',
#                   'language_programming', 'framework_programming', 'skills_programming',
#                   'interval_works', 'rate_works', ]


#
# class HumanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Human
#         fields = "__all__"
