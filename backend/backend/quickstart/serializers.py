"""
    Author: Luis Alfredo León Villapún
    Creation date: 8/3/2018
    Last modification date: 8/3/2018
"""

#Imports
from django.contrib.auth.models import User, Group
from quickstart.models import Comment, ExperienciaLaboral, Project, Skill, Leadership
from rest_framework import serializers

#Los ModelSerializers ayudan a que el codigo se reduzca y no se tenga que hacer un serializer mas largo

#User serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#Group serializer
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

#Comment serializer
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('nickname', 'comment', 'date')

#ExperienciaLaboral serializer
class ExperienciaLaboralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExperienciaLaboral
        fields = ('titulo', 'empresa', 'descripcion', 'fecha_inicio', 'fecha_fin')

#Project serializer
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('titulo', 'repository_link', 'descripcion', 'fecha_inicio', 'fecha_fin')

#Skill serializer
class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('technology', 'expertise_level')

#Leadership serializer
class LeadershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leadership
        fields = ('date', 'descripcion')
