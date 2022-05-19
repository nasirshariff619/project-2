from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
    def create_app(self):
         return app

class TestResponse(TestBase):
    def test_prediction(self):
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "Test"
                p.return_value.text = "Testing"
                response = self.client.get(url_for('get_task'))
                self.assertIn(b'Test', response.data)
                self.assertIn(b'Testing', response.data)

#pytest --cov=app --cov-report=term-missing