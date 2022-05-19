from unittest.mock import patch
from flask import url_for, request
import requests
from flask_testing import TestCase
import requests_mock
from app import app


class TestBase(TestCase):
    def create_app(self):
         return app

class TestResponse(TestBase):
    def test_england(self):
        with patch('random.randint') as p:
            p.return_value = 0
            response = self.client.get(url_for('get_country'))
            self.assertIn(b'England', response.data)



#pytest --cov=app --cov-report=term-missing