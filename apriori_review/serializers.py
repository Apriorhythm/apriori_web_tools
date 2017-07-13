# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import AprioriReview


class AprioriReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = AprioriReview
        fields = ('content', 'create_date')

