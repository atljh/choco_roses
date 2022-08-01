from django.test import TestCase, RequestFactory
from .views import index


class TestIndex(TestCase):
    def test_index(self):
        factory = RequestFactory()
        request_in = factory.get('/index')
        resp = index(request_in)
        print('aaa')