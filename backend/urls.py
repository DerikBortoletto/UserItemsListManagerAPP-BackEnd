from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet, ItemViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter() 
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"list", ListViewSet, basename="list")
router.register(r"items", ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
]

