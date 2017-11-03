# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import project
import datetime
import json
# Create your views here.
def index(request):
	#return render(request, "gantt.html", {"canWrite":"true",})
	projects = project.objects.all()
	print projects
	return render(request, "index.html", {"projects":projects})

def add_project(request):
	if request.method == "POST":
		'''
		author = request.COOKIES.get('username')
		if author:
			return HttpResponse("你还未登录！")
		'''
		newproject = project()
		projectname = request.POST["projectname"]
		publicdate = request.POST["publicdate"].split("-")
		
		author = 'admin'
		newproject.projectname = projectname
		newproject.pulbicdate = datetime.date(
			int(publicdate[0]), 
			int(publicdate[1]),
			int(publicdate[2] ) ) 


		newproject.author = author
		newproject.save()
		return HttpResponseRedirect("/")

	else:
		return HttpResponse("请求非法！")

def show_projects(request, project_name):

	return render(request, 'gantt.html', {"projectname":project_name})


def store_data(projectname, projectdata):
	pass


def load_data(projectname):
	with open("controll/data/%s.json"%projectname) as datafile:
		projectdata = json.load(datafile)

		return projectdata



def get_project_data(request):
	projectname =  request.GET["taskId"]
	#获取项目进度json数据
	projectdata = load_data(projectname)

	return HttpResponse(json.dumps(projectdata), content_type="application/json")
