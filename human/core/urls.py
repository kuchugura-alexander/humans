from django.urls import include, path
from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as drf_views


router = routers.DefaultRouter()
router.register(r'human', views.HumanFirstSerializer, basename="Human")
router.register(r'humanCreate', views.HumanCreateSerializer, basename="Human")
router.register(r'gender', views.GenderViewSet, basename="Gender")
router.register(r'city', views.CityViewSet, basename="City")
router.register(r'country', views.CountryViewSet, basename="Country")
router.register(r'timezoneresidence', views.TimeZoneResidenceViewSet, basename="TimeZoneResidence")
router.register(r'levellanguage', views.LanguageProgrammingViewSet, basename="LevelLanguage")
router.register(r'levellanguagetitle', views.LevelLanguageTitleViewSet, basename="LevelLanguageTitle")
router.register(r'levellanguageknowledge', views.LevelLanguageKnowledgeViewSet, basename="LevelLanguageKnowledge")
router.register(r'languageprogramming', views.LanguageProgrammingViewSet, basename="LanguageProgramming")
router.register(r'frameworkprogramming', views.FrameworkProgrammingViewSet, basename="FrameworkProgramming")
router.register(r'skillprogramming', views.SkillProgrammingViewSet, basename="SkillProgramming")
router.register(r'intervalwork', views.InternalWorkViewSet, basename="IntervalWork")
router.register(r'ratework', views.RateWorkViewSet, basename="RateWork")
# router.register(r'hr/human', views.HrHumansViewSet, basename="hr_human")
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.index),
    path('test/', views.test, name='test'),
    path('human', views.human, name='human'),
    path('humanCreate', views.humanCreate, name='humanCreate'),
    path('gender', views.gender, name='gender'),
    path('city', views.city, name='city'),
    path('country', views.country, name='country'),
    path('timezoneresidence', views.timezoneresidence, name='timezoneresidence'),
    path('levellanguage', views.levellanguage, name='levellanguage'),
    path('levellanguagetitle', views.levellanguagetitle, name='levellanguagetitle'),
    path('levellanguageknowledge', views.levellanguageknowledge, name='levellanguageknowledge'),
    path('languageprogramming', views.languageprogramming, name='languageprogramming'),
    path('frameworkprogramming', views.frameworkprogramming, name='frameworkprogramming'),
    path('skillprogramming', views.skillprogramming, name='skillprogramming'),
    path('intervalwork', views.intervalwork, name='intervalwork'),
    path('ratework', views.ratework, name='ratework'),
    path('human/<int:id>', views.human_detail, name='human_detail'),
    path('gender/<int:id>', views.gender_detail, name='gender_detail'),
    path('city/<int:id>', views.city_detail, name='city_detail'),
    path('country/<int:id>', views.country_detail, name='country_detail'),
    path('timezoneresidence/<int:id>', views.timezoneresidence_detail, name='timezoneresidence_detail'),
    path('levellanguage/<int:id>', views.levellanguage_detail, name='levellanguage_detail'),
    path('levellanguagetitle/<int:id>', views.levellanguagetitle_detail, name='levellanguagetitle_detail'),
    path('levellanguageknowledge/<int:id>', views.levellanguageknowledge_detail, name='levellanguageknowledge_detail'),
    path('languageprogramming/<int:id>', views.languageprogramming_detail, name='languageprogramming_detail'),
    path('frameworkprogramming/<int:id>', views.frameworkprogramming_detail, name='frameworkprogramming_detail'),
    path('skillprogramming/<int:id>', views.skillprogramming_detail, name='skillprogramming_detail'),
    path('intervalwork/<int:id>', views.intervalwork_detail, name='intervalwork_detail'),
    path('ratework/<int:id>', views.ratework_detail, name='ratework_detail'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_core')),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),

] + router.urls
