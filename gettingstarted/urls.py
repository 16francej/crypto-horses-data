from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import hello.views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
