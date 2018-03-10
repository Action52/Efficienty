from quickstart.models import Comment, ExperienciaLaboral, Project, Skill, Leadership
from quickstart.serializers import UserSerializer, GroupSerializer, CommentSerializer, ExperienciaLaboralSerializer, ProjectSerializer, SkillSerializer, LeadershipSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime

#EXPERIENCIA

fecha_inicio_ac = datetime.strptime('01-08-2016', '%d-%m-%Y').date()
fecha_fin_ac = datetime.strptime('16-12-2016', '%d-%m-%Y').date()

experiencialab_ac = ExperienciaLaboral(titulo='Acreditaciones', empresa='ITESM', descripcion = 'Becario de acreditaciones ABET',fecha_inicio=fecha_inicio_ac, fecha_fin = fecha_fin_ac)
experiencialab_ac.save()

fecha_inicio_mapa = datetime.strptime('01-01-2017', '%d-%m-%Y').date()
fecha_fin_mapa = datetime.strptime('08-12-2017', '%d-%m-%Y').date()

experiencialab_mapa = ExperienciaLaboral(titulo='MapaTec', empresa='ITESM', descripcion = 'Plataforma web para proyecto NOVUS',fecha_inicio=fecha_inicio_mapa, fecha_fin = fecha_fin_mapa)
experiencialab_mapa.save()


#PROJECTS

fecha_inicio_1 = datetime.strptime('01-04-2017', '%d-%m-%Y').date()
fecha_fin_1= datetime.strptime('01-05-2017', '%d-%m-%Y').date()
project_1 = Project(titulo = 'Game of Life', repository_link = 'https://github.com/Action52/GameOfLife', descripcion = 'Implementación del juego de la vida de Conway usando threads.', fecha_inicio = fecha_inicio_1, fecha_fin = fecha_fin_1)
project_1.save()

fecha_inicio_2 = datetime.strptime('01-08-2016', '%d-%m-%Y').date()
fecha_fin_2= datetime.strptime('01-08-2016', '%d-%m-%Y').date()
project_2 = Project(titulo = 'Tie Fighter Canvas', repository_link = 'https://github.com/Action52/TieFighterCanvas', descripcion = 'Programa gráfico que despliega un Tie Fighter y lo modifica.', fecha_inicio = fecha_inicio_2, fecha_fin = fecha_fin_2)
project_2.save()

fecha_inicio_3 = datetime.strptime('01-03-2015', '%d-%m-%Y').date()
fecha_fin_3= datetime.strptime('01-05-2015', '%d-%m-%Y').date()
project_3 = Project(titulo = 'Von Neumann Emulator', repository_link = 'https://github.com/Action52/VonNeumannEmulator', descripcion = 'Emulador de la máquina de Von Neumann.', fecha_inicio = fecha_inicio_3, fecha_fin = fecha_fin_3)
project_3.save()

fecha_inicio_4 = datetime.strptime('01-04-2017', '%d-%m-%Y').date()
fecha_fin_4= datetime.strptime('01-05-2017', '%d-%m-%Y').date()
project_4 = Project(titulo = 'Mexcritores', repository_link = 'https://github.com/Action52/Mexcritores', descripcion = 'Plataforma web desarrollada para la clase de bases de datos.', fecha_inicio = fecha_inicio_4, fecha_fin = fecha_fin_4)
project_4.save()

#SKILLS

skill_1 = Skill(technology = 'C', expertise_level = 7)
skill_1.save()
skill_2 = Skill(technology = 'Java', expertise_level = 9)
skill_2.save()
skill_3 = Skill(technology = 'Python', expertise_level = 5)
skill_3.save()
skill_4 = Skill(technology = 'PHP', expertise_level = 7)
skill_4.save()
skill_5 = Skill(technology = 'MySQL', expertise_level = 7)
skill_5.save()
skill_6 = Skill(technology = 'PostgreSQL', expertise_level = 8)
skill_6.save()
skill_7 = Skill(technology = 'Bootstrap', expertise_level = 6)
skill_7.save()
skill_8 = Skill(technology = 'Laravel', expertise_level = 7)
skill_8.save()
skill_9 = Skill(technology = 'Computer Vision', expertise_level = 4)
skill_9.save()
skill_10 = Skill(technology = 'Javascript', expertise_level = 5)
skill_10.save()

#LEADERSHIP

lead_date_1 = datetime.strptime('01-08-2014', '%d-%m-%Y').date()
lead_1 = Leadership(date = lead_date_1, descripcion = 'Beneficiaro de una beca académica por parte del ITESM')
lead_1.save()

lead_date_2 = datetime.strptime('01-08-2014', '%d-%m-%Y').date()
lead_2 = Leadership(date = lead_date_2, descripcion = 'Beneficiaro de una beca académica por parte de Fundación Telmex')
lead_2.save()

lead_date_3 = datetime.strptime('01-04-2017', '%d-%m-%Y').date()
lead_3 = Leadership(date = lead_date_3, descripcion = 'Participante de Hackaton local')
lead_3.save()

lead_date_4 = datetime.strptime('01-01-2018', '%d-%m-%Y').date()
lead_4 = Leadership(date = lead_date_4, descripcion = 'Miembro del equipo representativo de ajedrez del ITESM')
lead_4.save()
