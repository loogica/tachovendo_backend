# -*- coding: utf-8 -*-
from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from model_mommy import mommy

from tachovendo.models import *

m = mommy.make_one
mr = mommy.make_recipe

class ModelTest(TestCase):
    def setUp(self):
        pass

    def test_import(self):
        pass
