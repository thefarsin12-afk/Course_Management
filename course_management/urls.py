from django.urls import path

from course_management.views import AdminRegisterView
from course_management.views import CouserListCreateView,CourseRetrieveUpdateDeleteView

urlpatterns = [

    path('admin/',AdminRegisterView.as_view()),

    path('create/',CouserListCreateView.as_view()),

    path('create/<int:pk>/',CourseRetrieveUpdateDeleteView.as_view()),

    
]