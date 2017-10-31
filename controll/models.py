from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class project(models.Model):
	##add you desc
	projectname = models.CharFiled(max_length=100)
	pulbicdate = models.DateFiled(auto_now=False)
	updatedate = models.DateTimeFiled(auto_now=True)
	author = models.CharFiled(max_length=100)

	def __init__(self):
		super.__init__(self)

	def ___init__(self, projectname, pulbicdate, author):
		super().__init__()
		self.projectname = projectname
		self.pulbicdate = pulbicdate
		self.author = author


	def __unicode__(self):
		return self.projectname

	def get_absolute_url(self):
		return reverse('projects', {self.projects,})
		