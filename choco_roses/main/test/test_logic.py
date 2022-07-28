from django.test import TestCase
from ..views import foo
from django.urls import reverse

class LogicTestCase(TestCase):
    def test_foo(self):
        result = foo(1)
        self.assertEqual(2, result)
