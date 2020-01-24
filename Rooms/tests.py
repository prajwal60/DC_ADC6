from django.test import TestCase

from .models import *
from .views import *
from django.urls import reverse
import json


# Create your tests here.


class Test(TestCase):

    def test_location(self):
        room = Room.objects.create(location="Jorpati")
        self.assertTrue(room.TestRoomlocation())

    def test_desc(self):
        desc=Room.objects.create(location="jorpati",
                                 phone_number="96322544",
                                 price=966321,
                                 desc="they are alone")
        self.assertTrue(desc.Test_desc())