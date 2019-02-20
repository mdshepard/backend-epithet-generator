import pytest
from flask_testing import TestCase
from sprintb.app import app
from sprintb import helpers

test_app = app.test_client()


class config_test(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_root(self):
        res = test_app.get('/')
        assert res.status_code == 200

    def test_vocabulary(self):
        res = test_app.get('/vocabulary')
        assert res.status_code == 200

    def test_epithet(self):
        test_app = app.test_client()
        res = test_app.get('/')
        assert res.status_code == 200

    def test_multiples(self):
        test_app = app.test_client()
        res = test_app.get('/epithets/3')
        assert len(res.json) == 3
        assert res.status_code == 200

    def test_random(self):
        res = test_app.get('/random')
        assert res.status_code == 200
