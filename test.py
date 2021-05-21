import unittest
from unittest.mock import MagicMock

import consts
import db
import weather


class BotTests(unittest.TestCase):
    def setUp(self):
        weather.get_weather = MagicMock(return_value=50)

    def test_weather(self):
        self.assertEqual(weather.get_weather('daw'), 50)

    def test_db(self):
        db.insert(18547, 'a', 'a', 'aaa')
        self.assertEqual(db.get(18547)[0][consts.db['username']], 'aaa')
        db.delete(18547)


unittest.main()
