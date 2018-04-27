from unittest import TestCase

from .helper import FlaskTestBase

class TestApiPlay(FlaskTestBase):
    def test_play_all(self):
        self.get_succ_json('/play/seat/',pid=1)

