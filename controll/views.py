from django.shortcuts import render
from django.http import HttpResponse
from models import project
# Create your views here.
def index(request):
	return render(request, "gantt.html", {"canWrite":"true",})


def add_project(request):
	if request.method == "POST":
		'''
		author = request.COOKIES.get('username')
		if author:
			return HttpResponse("你还未登录！")
		'''
		newproject = project()
		projectname = request.POST["projectname"]
		publicdate = request.POST["publicdata"]
		author = 'admin'

	else:
		return HttpResponse("请求非法！")

def show_project(request):
	projects = project.objects.all()
	return render('show_project.html', projects)