from unittest import TestCase

from .helper import FlaskTestBase

class TestApiCinema(FlaskTestBase):
    def test_cinema_all(self):
        self.get_succ_json('/cinema/all/')

    def test_cinema_halls(self):
        self.assert_get('/cinema/halls/',400,cid='abc')
        self.get_succ_json('/cinema/halls/',cid=1)

