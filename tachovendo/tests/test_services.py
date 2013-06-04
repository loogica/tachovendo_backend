import unittest

from django.conf import settings
from django.test import TestCase

from tachovendo.services import auth, rain_service, flood_service, schools_service

class RainServiceTest(TestCase):
    def test_auth(self):
        result = auth(settings.APP_ID, settings.APP_SECRET)

        self.assertTrue(result[0] != None)
        self.assertTrue(result[1] != None)

    def test_rain_service(self):
        (token, token_expires) = auth(settings.APP_ID, settings.APP_SECRET)

        result = rain_service(token)
        self.assertTrue(result != None)

    def test_flood_service(self):
        (token, token_expires) = auth(settings.APP_ID, settings.APP_SECRET)

        result = flood_service(token)
        self.assertTrue(result != None)
