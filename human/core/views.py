from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.models import User, Group
from rest_framework import permissions
from .serializers import (
    GenderSerializer,
    CountrySerializer, TimeZoneResidenceSerializer,
    CitySerializer, LevelLanguageTitleSerializer,
    LevelLanguageKnowledgeSerializer, LevelLanguageSerializer,
    LanguageProgrammingSerializer, FrameworkProgrammingSerializer,
    SkillProgrammingSerializer, IntervalWorkSerializer,
    RateWorkSerializer,
    HumanSerializer, HumanFirstSerializer
)
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import (
    Human, Gender,
    City, Country, TimeZoneResidence,
    LevelLanguage, LevelLanguageTitle, LevelLanguageKnowledge,
    LanguageProgramming, FrameworkProgramming,
    SkillProgramming, IntervalWork, RateWork
)
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, 'index.html', {})


def gender(request):
    return render(request, 'index.html', {})


def human(request):
    return render(request, 'index.html', {})


def humanCreate(request):
    return render(request, 'index.html', {})


def city(request):
    return render(request, 'index.html', {})


def country(request):
    return render(request, 'index.html', {})


def timezoneresidence(request):
    return render(request, 'index.html', {})


def levellanguage(request):
    return render(request, 'index.html', {})


def levellanguagetitle(request):
    return render(request, 'index.html', {})


def levellanguageknowledge(request):
    return render(request, 'index.html', {})


def languageprogramming(request):
    return render(request, 'index.html', {})


def frameworkprogramming(request):
    return render(request, 'index.html', {})


def skillprogramming(request):
    return render(request, 'index.html', {})


def intervalwork(request):
    return render(request, 'index.html', {})


def ratework(request):
    return render(request, 'index.html', {})


def gender_detail(request, id):
    return render(request, 'index.html', {id:id})


def human_detail(request, id):
    return render(request, 'index.html', {id:id})


def city_detail(request, id):
    return render(request, 'index.html', {id:id})


def country_detail(request, id):
    return render(request, 'index.html', {id:id})


def timezoneresidence_detail(request, id):
    return render(request, 'index.html', {id:id})


def levellanguage_detail(request, id):
    return render(request, 'index.html', {id:id})


def levellanguagetitle_detail(request, id):
    return render(request, 'index.html', {id:id})


def levellanguageknowledge_detail(request, id):
    return render(request, 'index.html', {id:id})


def languageprogramming_detail(request, id):
    return render(request, 'index.html', {id:id})


def frameworkprogramming_detail(request, id):
    return render(request, 'index.html', {id:id})


def skillprogramming_detail(request, id):
    return render(request, 'index.html', {id:id})


def intervalwork_detail(request, id):
    return render(request, 'index.html', {id:id})


def ratework_detail(request, id):
    return render(request, 'index.html', {id:id})


class AbsModelViewSet(viewsets.ModelViewSet):
    """
    Abstract model for all ModelViewSet.
    """
    permission_classes = [permissions.AllowAny]

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     return HttpResponse("Hello, world.")
        # pass

    # def retrieve(self, request, pk=None):
    #     pass

    def update(self, request, pk=None):
        return HttpResponse("Hello, world.")
        # pass

    def partial_update(self, request, pk=None):
        return HttpResponse("Hello, world.")
        # pass

    def destroy(self, request, pk=None):
        return HttpResponse("Hello, world.")
        # pass

    class Meta:
        abstract = True


class HumanFirstSerializer(AbsModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanFirstSerializer

    def create(self, request):
        return HttpResponse("Hello, world.")
        # pass


class HumanCreateSerializer(AbsModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

    def list(self, request):
        return HttpResponse("Hello, world.")
        # pass

    def retrieve(self, request, pk=None):
        return HttpResponse("Hello, world.")
        # pass


class GenderViewSet(AbsModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class CityViewSet(AbsModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CountryViewSet(AbsModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class TimeZoneResidenceViewSet(AbsModelViewSet):
    queryset = TimeZoneResidence.objects.all()
    serializer_class = TimeZoneResidenceSerializer


class LevelLanguageViewSet(AbsModelViewSet):
    queryset = LevelLanguage.objects.all()
    serializer_class = LevelLanguageSerializer


class LevelLanguageTitleViewSet(AbsModelViewSet):
    queryset = LevelLanguageTitle.objects.all()
    serializer_class = LevelLanguageTitleSerializer


class LevelLanguageKnowledgeViewSet(AbsModelViewSet):
    queryset = LevelLanguageKnowledge.objects.all()
    serializer_class = LevelLanguageKnowledgeSerializer


class LanguageProgrammingViewSet(AbsModelViewSet):
    queryset = LanguageProgramming.objects.all()
    serializer_class = LanguageProgrammingSerializer


class FrameworkProgrammingViewSet(AbsModelViewSet):
    queryset = FrameworkProgramming.objects.all()
    serializer_class = FrameworkProgrammingSerializer


class SkillProgrammingViewSet(AbsModelViewSet):
    queryset = SkillProgramming.objects.all()
    serializer_class = SkillProgrammingSerializer


class InternalWorkViewSet(AbsModelViewSet):
    queryset = IntervalWork.objects.all()
    serializer_class = IntervalWorkSerializer


class RateWorkViewSet(AbsModelViewSet):
    queryset = RateWork.objects.all()
    serializer_class = RateWorkSerializer

