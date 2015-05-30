#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import sys
stdin, stdout = sys.stdin, sys.stdout
reload(sys)
sys.stdin, sys.stdout = stdin, stdout
sys.setdefaultencoding('utf-8')
# Create your models here.
class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	create_date=models.DateTimeField(default=timezone.now)
	publishe_date=models.DateTimeField(blank=True, null=True)
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title

	
