"""
    Author: Luis Alfredo León Villapún
    Creation date: 8/3/2018
    Last modification date: 8/3/2018
"""

#Imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from quickstart.models import Comment, ExperienciaLaboral, Project, Skill, Leadership
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, CommentSerializer, ExperienciaLaboralSerializer, ProjectSerializer, SkillSerializer, LeadershipSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    #This will allow users to be edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    #This will allow groups to be edited
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    #This will allow comments to be edited
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ExperienciaLaboralViewSet(viewsets.ModelViewSet):
    #This will allow comments to be edited
    queryset = ExperienciaLaboral.objects.all().order_by('-fecha_fin')
    serializer_class = ExperienciaLaboralSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    #This will allow comments to be edited
    queryset = Project.objects.all().order_by('-fecha_fin')
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    #This will allow comments to be edited
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class LeadershipViewSet(viewsets.ModelViewSet):
    #This will allow comments to be edited
    queryset = Leadership.objects.all()
    serializer_class = LeadershipSerializer
