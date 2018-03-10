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
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

# Create your views here.
#Las clases viewset no las ocuparé por el momento
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

class JSONResponse(HttpResponse):
    #Parsea las responses a json
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def comment_list(request):
    #Lista los comentarios o crea uno nuevo --> equivale al CommentViewSet
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201) #Codigo para created
        return JSONResponse(serializer.errors, status = 400) #Bad request

def comment_detail(request, pk):
    #Crear, borrar, o actualizar un comentario
    try:
        comment = Comment.objects.get(pk = pk)
    except Comment.DoesNotExist:
        return HttpResponse(status = 404) #Not found :D
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return JSONResponse(json.dumps(serializer.data))
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400) #Bad request
    elif request.method == 'DELETE':
        comment.delete()
        return HttpResponse(status = 204) #No content


@csrf_exempt
def experiencia_list(request):
    #Lista los comentarios o crea uno nuevo --> equivale al CommentViewSet
    if request.method == 'GET':
        experiencia = ExperienciaLaboral.objects.all()
        serializer = ExperienciaLaboralSerializer(experiencia, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExperienciaLaboralSerializer(data = data)
        if serializer.isValid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201) #Codigo para created
        return JSONResponse(serializer.errors, status = 400) #Bad request

def experiencia_detail(request, pk):
    #Crear, borrar, o actualizar un comentario
    try:
        experiencia = ExperienciaLaboral.objects.get(pk = pk)
    except ExperienciaLaboral.DoesNotExist:
        return HttpResponse(status = 404) #Not found :D

    if request.method == 'GET':
        serializer = ExperienciaLaboralSerializer(experiencia)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperienciaLaboralSerializer(experiencia, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400) #Bad request
    elif request.method == 'DELETE':
        experiencia.delete()
        return HttpResponse(status = 204) #No content


@csrf_exempt
def project_list(request):
    #Lista los comentarios o crea uno nuevo --> equivale al CommentViewSet
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data = data)
        if serializer.isValid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201) #Codigo para created
        return JSONResponse(serializer.errors, status = 400) #Bad request

def project_detail(request, pk):
    #Crear, borrar, o actualizar un comentario
    try:
        project = Project.objects.get(pk = pk)
    except Project.DoesNotExist:
        return HttpResponse(status = 404) #Not found :D

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400) #Bad request
    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status = 204) #No content


@csrf_exempt
def skill_list(request):
    #Lista los comentarios o crea uno nuevo --> equivale al CommentViewSet
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SkillSerializer(data = data)
        if serializer.isValid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201) #Codigo para created
        return JSONResponse(serializer.errors, status = 400) #Bad request

def skill_detail(request, pk):
    #Crear, borrar, o actualizar un comentario
    try:
        skill = Skill.objects.get(pk = pk)
    except Skill.DoesNotExist:
        return HttpResponse(status = 404) #Not found :D

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkillSerializer(skill, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400) #Bad request
    elif request.method == 'DELETE':
        skill.delete()
        return HttpResponse(status = 204) #No content


@csrf_exempt
def leadership_list(request):
    #Lista los comentarios o crea uno nuevo --> equivale al CommentViewSet
    if request.method == 'GET':
        leadership = Leadership.objects.all()
        serializer = LeadershipSerializer(leadership, many = True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LeadershipSerializer(data = data)
        if serializer.isValid():
            serializer.save()
            return JSONResponse(serializer.data, status = 201) #Codigo para created
        return JSONResponse(serializer.errors, status = 400) #Bad request

def leadership_detail(request, pk):
    #Crear, borrar, o actualizar un comentario
    try:
        leadership = Leadership.objects.get(pk = pk)
    except Leadership.DoesNotExist:
        return HttpResponse(status = 404) #Not found :D

    if request.method == 'GET':
        serializer = LeadershipSerializer(leadership)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LeadershipSerializer(leadership, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status = 400) #Bad request
    elif request.method == 'DELETE':
        leadership.delete()
        return HttpResponse(status = 204) #No content
