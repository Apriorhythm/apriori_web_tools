# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AprioriReview(models.Model):
    content = models.CharField('content',max_length=520)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Apriori_Review'
        verbose_name_plural = 'Apriori_Review'

