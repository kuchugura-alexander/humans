from django.urls import include, path
from django.conf.urls import url
from . import views
from rest_framework import routers
from rest_framework.authtoken import views as drf_views


router = routers.DefaultRouter()
router.register(r'human', views.HumanViewSet, basename="Human")
router.register(r'gender', views.GenderViewSet, basename="Gender")
router.register(r'city', views.CityViewSet, basename="City")
router.register(r'country', views.CityViewSet, basename="Country")
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
    path('gender', views.gender, name='gender'),
    path('human', views.human, name='human'),
    path('gender/<int:id>', views.gender_detail, name='gender_detail'),
    path('human/<int:id>', views.human_detail, name='human_detail'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_core')),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),

] + router.urls
