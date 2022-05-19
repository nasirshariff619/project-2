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
    def test_england_sausage_roll(self):
        response = self.client.post(url_for('post_task'), data = 'England Sausage-roll')
        self.assertIn(b'Go to London and buy a sausage-roll from greggs', response.data)

    def test_england_croissant(self):
        response = self.client.post(url_for('post_task'), data = 'England Croissant')
        self.assertIn(b'Eat a croissant on the London Eye', response.data)

    def test_england_schnitzel(self):
        response = self.client.post(url_for('post_task'), data = 'England Schnitzel')
        self.assertIn(b'Google where to buy schnitzel in England because I have no clue or try again', response.data)

    def test_france_sausage_roll(self):
        response = self.client.post(url_for('post_task'), data = 'France Sausage-roll')
        self.assertIn(b'Sausage-rolls are banned from France. Try again.', response.data) 

    def test_france_croissant(self):
        response = self.client.post(url_for('post_task'), data = 'France Croissant')
        self.assertIn(b'Eat a croissant at the top of the Eiffel Tower', response.data)
    
    def test_france_schnitzel(self):
        response = self.client.post(url_for('post_task'), data = 'France Schnitzel')
        self.assertIn(b'Google where to buy schnitzel in France because I have no clue or try again', response.data)

    def test_germany_sausage_roll(self):
        response = self.client.post(url_for('post_task'), data = 'Germany Sausage-roll')
        self.assertIn(b'Watch Bayern Munich play while eating sausage roll', response.data) 

    def test_germany_croissant(self):
        response = self.client.post(url_for('post_task'), data = 'Germany Croissant')
        self.assertIn(b'Eat croissant at Nuremberg Clock Tower', response.data)    

    def test_germany_schnitzel(self):
        response = self.client.post(url_for('post_task'), data = 'Germany Schnitzel')
        self.assertIn(b'Eat Schnitzel at an Oktoberfest event', response.data)    

#pytest --cov=app --cov-report=term-missing