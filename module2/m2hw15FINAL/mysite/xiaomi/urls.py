from django.urls import include, path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'phones', views.PhoneViewSet)

urlpatterns = [
            path('/jsonapi', include(router.urls)),
            path('', views.index, name = 'index'),
            path('/json', views.return_json, name = 'json'),
            path('/doc', views.doc, name = 'Documentation')
            ]