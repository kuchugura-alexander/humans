from django.urls import include, path
from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as drf_views


router = routers.DefaultRouter()
router.register(r'human', views.HumanView, basename="HumanView")
router.register(r'gender', views.GenderView, basename="GenderView")
router.register(r'city', views.CityView, basename="CityView")
router.register(r'country', views.CountryView, basename="CountryView")
router.register(r'timezoneresidence', views.TimeZoneResidenceView, basename="TimeZoneResidenceView")
router.register(r'levellanguage', views.LanguageProgrammingView, basename="LevelLanguageView")
router.register(r'levellanguagetitle', views.LevelLanguageTitleView, basename="LevelLanguageTitleView")
router.register(r'levellanguageknowledge', views.LevelLanguageKnowledgeView, basename="LevelLanguageKnowledgeView")
router.register(r'languageprogramming', views.LanguageProgrammingView, basename="LanguageProgrammingView")
router.register(r'frameworkprogramming', views.FrameworkProgrammingView, basename="FrameworkProgrammingView")
router.register(r'skillprogramming', views.SkillProgrammingView, basename="SkillProgrammingView")
router.register(r'intervalwork', views.InternalWorkView, basename="IntervalWorkView")
router.register(r'ratework', views.RateWorkView, basename="RateWorkView")

router.register(r'humanCreate', views.HumanCreate, basename="HumanCreate")
router.register(r'genderCreate', views.GenderCreate, basename="GenderCreate")
router.register(r'cityCreate', views.CityCreate, basename="CityCreate")
router.register(r'countryCreate', views.CountryCreate, basename="CountryCreate")
router.register(r'timezoneresidenceCreate', views.TimeZoneResidenceCreate, basename="TimeZoneResidenceCreate")
router.register(r'levellanguageCreate', views.LanguageProgrammingCreate, basename="LevelLanguageCreate")
router.register(r'levellanguagetitleCreate', views.LevelLanguageTitleCreate, basename="LevelLanguageTitleCreate")
router.register(r'levellanguageknowledgeCreate', views.LevelLanguageKnowledgeCreate, basename="LevelLanguageKnowledgeCreate")
router.register(r'languageprogrammingCreate', views.LanguageProgrammingCreate, basename="LanguageProgrammingCreate")
router.register(r'frameworkprogrammingCreate', views.FrameworkProgrammingCreate, basename="FrameworkProgrammingCreate")
router.register(r'skillprogrammingCreate', views.SkillProgrammingCreate, basename="SkillProgrammingCreate")
router.register(r'intervalworkCreate', views.InternalWorkCreate, basename="IntervalWorkCreate")
router.register(r'rateworkCreate', views.RateWorkCreate, basename="RateWorkCreate")
#
# router.register(r'hr/human', views.HrHumansView, basename="hr_human")
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
