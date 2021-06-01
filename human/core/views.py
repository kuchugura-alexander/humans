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


def gender_detail(request, id):
    return render(request, 'index.html', {id:id})


def human_detail(request, id):
    return render(request, 'index.html', {id:id})


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all()
#    serializer_class = HumanSerializer
    serializer_class = HumanFirstSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         permission_classes = [permissions.AllowAny]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]

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


class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
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


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
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


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
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


class TimeZoneResidenceViewSet(viewsets.ModelViewSet):
    queryset = TimeZoneResidence.objects.all()
    serializer_class = TimeZoneResidenceSerializer
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


class LevelLanguageViewSet(viewsets.ModelViewSet):
    queryset = LevelLanguage.objects.all()
    serializer_class = LevelLanguageSerializer
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


class LevelLanguageTitleViewSet(viewsets.ModelViewSet):
    queryset = LevelLanguageTitle.objects.all()
    serializer_class = LevelLanguageTitleSerializer
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


class LevelLanguageKnowledgeViewSet(viewsets.ModelViewSet):
    queryset = LevelLanguageKnowledge.objects.all()
    serializer_class = LevelLanguageKnowledgeSerializer
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


class LanguageProgrammingViewSet(viewsets.ModelViewSet):
    queryset = LanguageProgramming.objects.all()
    serializer_class = LanguageProgrammingSerializer
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


class FrameworkProgrammingViewSet(viewsets.ModelViewSet):
    queryset = FrameworkProgramming.objects.all()
    serializer_class = FrameworkProgrammingSerializer
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


class SkillProgrammingViewSet(viewsets.ModelViewSet):
    queryset = SkillProgramming.objects.all()
    serializer_class = SkillProgrammingSerializer
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


class InternalWorkViewSet(viewsets.ModelViewSet):
    queryset = IntervalWork.objects.all()
    serializer_class = IntervalWorkSerializer
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


class RateWorkViewSet(viewsets.ModelViewSet):
    queryset = RateWork.objects.all()
    serializer_class = RateWorkSerializer
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


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class HumanAllInfoListDetail(APIView):
#     """
#     Retrieve, update or delete a Human.
#     """
#     def get_object(self, pk):
#         """
#         Prepare before launch methods of the class.
#         """
#         try:
#             return Human.objects.get(pk=pk)
#         except Human.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         """
#         Retrieve.
#         """
#         human = self.get_object(pk)
#         serializer = HumanAllInfoSerializer(human)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         """
#         Create and Update.
#         """
#         human = self.get_object(pk)
#         serializer = HumanAllInfoSerializer(human, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(serializer.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         """
#         Delete.
#         """
#         human = self.get_object(pk)
#         human.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
