from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class project(models.Model):
	##add you desc
	projectname = models.CharField(max_length=100)
	pulbicdate = models.DateField(auto_now=False)
	updatedate = models.DateTimeField(auto_now=True)
	author = models.CharField(max_length=100)

	def __unicode__(self):
		return self.projectname

	def get_absolute_url(self):
		return reverse('projects', args=(self.projectname,))
		