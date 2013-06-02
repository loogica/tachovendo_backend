import unittest
from django.test import TestCase

from tachovendo.services import auth, rain_service, schools_service

class RainServiceTest(TestCase):
    def test_auth(self):
        APP_ID = ""
        APP_SECRET = ""

        result = auth(APP_ID, APP_SECRET)

        self.assertTrue(result[0] != None)
        self.assertTrue(result[1] != None)

        print result

    def test_rain_service(self):
        APP_ID = ""
        APP_SECRET = ""

        (token, token_expires) = auth(APP_ID, APP_SECRET)

        result = rain_service(token)
        self.assertTrue(result != None)

    def test_schools_service(self):
        APP_ID = ""
        APP_SECRET = ""

        (token, token_expires) = auth(APP_ID, APP_SECRET)

        result = rain_service(token)
        self.assertTrue(result != None)
