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
    def test_sausage_roll(self):
        with patch('random.randint') as p:
            p.return_value = 0
            response = self.client.get(url_for('get_food'))
            self.assertIn(b'Sausage-roll', response.data)



#pytest --cov=app --cov-report=term-missing