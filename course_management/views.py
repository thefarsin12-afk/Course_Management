from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from course_management.serializers import RegisterSerializer
from course_management.serializers import CourseSerailizers
from course_management.models import Course
from course_management.pagination import CustomPagination,CustomLimitOffset



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

    pagination_class = CustomLimitOffset

    def get_queryset(self):

        qs = Course.objects.all()

        query_parameters = self.request.query_params

        if "language" in query_parameters:

            language = query_parameters.get("language")

            qs = qs.filter(language__iexact=language)

        if "price" in query_parameters:

            price = query_parameters.get("price") 

            qs = qs.filter(price=price)

        if "trainer" in query_parameters:

            trainer = query_parameters.get("trainer")

            qs = qs.filter(trainer__iexact=trainer) 

        if "title" in query_parameters:

            title = query_parameters.get("title")

            qs = qs.filter(title__icontains=title)    

        return qs    

            

class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CourseSerailizers

    queryset = Course.objects.all()    


