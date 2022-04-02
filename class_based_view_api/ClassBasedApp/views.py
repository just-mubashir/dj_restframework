from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . models import Course, CourseSerializer
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet
# Create your views here.

# ________________________
# FINALLY
# ________________________

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# ________________________


'''class CourseListView(
    generics.ListAPIView, 
    generics.CreateAPIView,
    ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class CourseListView(
    generics.ListCreateAPIView,
    ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class CourseListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    # mixins.DestroyModelMixin ,
    generics.GenericAPIView
    ):
    serializer_class = CourseSerializer
    def get (self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)'''



# _____________________________________----

# class CourseViewSet(ViewSet):
#     def list(
#         self,
#         request
#     ):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many = True)
#         return Response(serializer.data)
    
#     def create(
#         self,
#         request
#     ):
#         # courses = Course.objects.all()
#         # serializer = CourseSerializer(courses, many = True)
#         # return Response(serializer.data)
#         serializer = CourseSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
    
#     def retrieve(
#         self, 
#         request, 
#         pk
#     ):
#         try:
#            course = Course.objects.all(pk=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)



# _____________________________________----

'''class CourseDetailView(
    generics.RetrieveUpdateDestroyAPIView
    ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class CourseDetailView(
    generics.RetrieveAPIView, 
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

'''class CourseDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''







'''class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)
    def post(self, request):
        courseSerializer = CourseSerializer(data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response (courseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(courseSerializer.errors)
class CourseDetailView(APIView):

    def get_course(self, pk):
        try:
            # course = Course.objects.get(pk=pk)
            return Course.objects.get(pk=pk)
            # return Course.objects.get_or_create(pk=pk)
        except:
            # return Response (status=status.HTTP_400_BAD_REQUEST)
            raise Http404
    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course);
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        course = self.get_course(pk)
        courseSerializer = CourseSerializer(course, data = request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response (courseSerializer.data)
        return Response(courseSerializer.errors)'''
