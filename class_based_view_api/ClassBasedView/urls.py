"""ClassBasedView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include
# from ClassBasedApp.views import CourseDetailView, CourseListView
from rest_framework.routers import DefaultRouter
from ClassBasedApp.models import Course
from ClassBasedApp.views import CourseViewSet

router = DefaultRouter()
router.register(
    'courses',
    CourseViewSet,
    basename='course'
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/', include ('ClassBasedApp.urls'))
    # path('api/courses/', CourseListView.as_view()),
    # path('api/courses/<int:pk>', CourseDetailView.as_view()),
]
