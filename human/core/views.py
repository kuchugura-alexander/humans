from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth.models import User, Group
from rest_framework import permissions
from . import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from . import models
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


class AbsModelViewNotAll(viewsets.ModelViewSet):
    """
    Abstract model for all Access Denied ModelViewSet.
    """
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        return HttpResponse("Hello, world.")

    def create(self, request):
        return HttpResponse("Hello, world.")

    def retrieve(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def update(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def partial_update(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def destroy(self, request, pk=None):
        return HttpResponse("Hello, world.")

    class Meta:
        abstract = True


class AbsModelViewOnlyView(viewsets.ModelViewSet):
    """
    Abstract model for View ModelViewSet.
    """
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        return HttpResponse("Hello, world.")

    def update(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def partial_update(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def destroy(self, request, pk=None):
        return HttpResponse("Hello, world.")

    class Meta:
        abstract = True


class AbsModelViewOnlyCreate(viewsets.ModelViewSet):
    """
    Abstract model for Create ModelViewSet.
    """
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        return HttpResponse("Hello, world.")

    def retrieve(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def update(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def partial_update(self, request, pk=None):
        return HttpResponse("Hello, world.")

    def destroy(self, request, pk=None):
        return HttpResponse("Hello, world.")

    class Meta:
        abstract = True

# VIEW - on serializers.HyperlinkedModelSerializer


class HumanView(AbsModelViewOnlyView):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanViewSerializer

    def create(self, request):
        return HttpResponse("Hello, world.")
        # pass


class GenderView(AbsModelViewOnlyView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderViewSerializer


class CityView(AbsModelViewOnlyView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CityViewSerializer


class CountryView(AbsModelViewOnlyView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountryViewSerializer


class TimeZoneResidenceView(AbsModelViewOnlyView):
    queryset = models.TimeZoneResidence.objects.all()
    serializer_class = serializers.TimeZoneResidenceViewSerializer


class LevelLanguageView(AbsModelViewOnlyView):
    queryset = models.LevelLanguage.objects.all()
    serializer_class = serializers.LevelLanguageViewSerializer


class LevelLanguageTitleView(AbsModelViewOnlyView):
    queryset = models.LevelLanguageTitle.objects.all()
    serializer_class = serializers.LevelLanguageTitleViewSerializer


class LevelLanguageKnowledgeView(AbsModelViewOnlyView):
    queryset = models.LevelLanguageKnowledge.objects.all()
    serializer_class = serializers.LevelLanguageKnowledgeViewSerializer


class LanguageProgrammingView(AbsModelViewOnlyView):
    queryset = models.LanguageProgramming.objects.all()
    serializer_class = serializers.LanguageProgrammingViewSerializer


class FrameworkProgrammingView(AbsModelViewOnlyView):
    queryset = models.FrameworkProgramming.objects.all()
    serializer_class = serializers.FrameworkProgrammingViewSerializer


class SkillProgrammingView(AbsModelViewOnlyView):
    queryset = models.SkillProgramming.objects.all()
    serializer_class = serializers.SkillProgrammingViewSerializer


class InternalWorkView(AbsModelViewOnlyView):
    queryset = models.IntervalWork.objects.all()
    serializer_class = serializers.IntervalWorkViewSerializer


class RateWorkView(AbsModelViewOnlyView):
    queryset = models.RateWork.objects.all()
    serializer_class = serializers.RateWorkViewSerializer


# CREATE - on serializers.ModelSerializer


class HumanCreate(AbsModelViewOnlyCreate):
    queryset = models.Human.objects.all()
    serializer_class = serializers.HumanCreateSerializer


class GenderCreate(AbsModelViewOnlyCreate):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderCreateSerializer


class CityCreate(AbsModelViewOnlyCreate):
    queryset = models.City.objects.all()
    serializer_class = serializers.CityCreateSerializer


class CountryCreate(AbsModelViewOnlyCreate):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountryCreateSerializer


class TimeZoneResidenceCreate(AbsModelViewOnlyCreate):
    queryset = models.TimeZoneResidence.objects.all()
    serializer_class = serializers.TimeZoneResidenceCreateSerializer


class LevelLanguageCreate(AbsModelViewOnlyCreate):
    queryset = models.LevelLanguage.objects.all()
    serializer_class = serializers.LevelLanguageCreateSerializer


class LevelLanguageTitleCreate(AbsModelViewOnlyCreate):
    queryset = models.LevelLanguageTitle.objects.all()
    serializer_class = serializers.LevelLanguageTitleCreateSerializer


class LevelLanguageKnowledgeCreate(AbsModelViewOnlyCreate):
    queryset = models.LevelLanguageKnowledge.objects.all()
    serializer_class = serializers.LevelLanguageKnowledgeCreateSerializer


class LanguageProgrammingCreate(AbsModelViewOnlyCreate):
    queryset = models.LanguageProgramming.objects.all()
    serializer_class = serializers.LanguageProgrammingCreateSerializer


class FrameworkProgrammingCreate(AbsModelViewOnlyCreate):
    queryset = models.FrameworkProgramming.objects.all()
    serializer_class = serializers.FrameworkProgrammingCreateSerializer


class SkillProgrammingCreate(AbsModelViewOnlyCreate):
    queryset = models.SkillProgramming.objects.all()
    serializer_class = serializers.SkillProgrammingCreateSerializer


class InternalWorkCreate(AbsModelViewOnlyCreate):
    queryset = models.IntervalWork.objects.all()
    serializer_class = serializers.IntervalWorkCreateSerializer


class RateWorkCreate(AbsModelViewOnlyCreate):
    queryset = models.RateWork.objects.all()
    serializer_class = serializers.RateWorkCreateSerializer
