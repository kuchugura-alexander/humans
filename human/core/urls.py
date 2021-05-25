from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'humans', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('test/', views.test, name='test'),
    # path('', include(router.urls)),
    path('humans/', views.HumansList.as_view()),
    path('human/<int:pk>/', views.HumanDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_core'))

]
