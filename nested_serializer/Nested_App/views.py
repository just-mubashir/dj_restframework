from django.shortcuts import render
# Create your views here
from rest_framework import authentication
from rest_framework import generics
from.serializers import InstructorSerializer, CourseSerializer
from . models import Course, Instructor
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# AUTH
# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)


class WriteByAdminPermission(BasePermission):
    def has_permission(self, request, view):
        # return super().has_permission(request, view)
        user = request.user
        if request.method == 'GET':
            return True
        
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False

class InstructorListView(generics.ListCreateAPIView):
    serializer_class =InstructorSerializer
    queryset = Instructor.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =InstructorSerializer
    queryset = Instructor.objects.all()



class CourseListView(generics.ListCreateAPIView):
    # authentication_classes =[BasicAuthentication]
    # authentication_classes =[TokenAuthentication]  #added in settings.py
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated, WriteByAdminPermission]
    serializer_class =CourseSerializer
    queryset = Course.objects.all()



class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =CourseSerializer
    queryset = Course.objects.all()