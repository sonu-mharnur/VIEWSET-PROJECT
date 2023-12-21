from django.shortcuts import render, get_object_or_404
from .serializers import CourseSerializer
from .models import Course
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework .viewsets import ViewSet ,ModelViewSet


### ModelViewSet Method

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




### Viewset Method

# class CourseViewSet(ViewSet):
#     def list(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

    # def create(self,request):
    #     serializer = CourseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


    # def retrieve(self, request, pk):
    #     try:
    #         course = Course.objects.get(pk=pk)
    #     except :
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = CourseSerializer(course)
    #     return Response(serializer.data)
