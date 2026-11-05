from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from course_management.serializers import RegisterSerializer
from course_management.serializers import CourseSerailizers
from course_management.models import Course



class AdminRegisterView(APIView):

    def post(self,request):

        form_data = request.data 

        serializer = RegisterSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data 

            instance = User.objects.create_superuser(**cleaned_data)

            serializer = RegisterSerializer(instance)

            return Response(data=serializer.data)

        return Response(data=serializer.data)

class CouserListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CourseSerailizers

    queryset = Course.objects.all()

class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CourseSerailizers

    queryset = Course.objects.all()    

