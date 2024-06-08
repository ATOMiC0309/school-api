# Create your views here.
from rest_framework import viewsets
from .models import Class, Teacher, Student
from .serializers import ClassSerializer, StudentSerializer, TeacherSerializer
from rest_framework import permissions
from rest_framework import authentication


class ClassAPIView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class TeacherAPIView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentAPIView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
