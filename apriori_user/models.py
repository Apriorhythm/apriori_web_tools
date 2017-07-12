# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class AprioriUser(AbstractUser):
    placeholder = models.SmallIntegerField('placeholder', default=1)
    #pl2 = models.CharField(max_length=128, default='pl2')


    class Meta:
        verbose_name = 'Apriori_User'
        verbose_name_plural = 'Apriori_User'

