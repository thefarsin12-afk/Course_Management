from django.contrib.auth.models import User

from rest_framework import serializers

from course_management.models import Course

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
    
            model = User
    
            fields = ["username","email","password"]

class CourseSerailizers(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","created_at","updated_at","cover_picture"] 