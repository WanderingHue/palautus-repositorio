import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def __init__(self):
        self.players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

    def get_players(self):
        return self.players

    def get_player(self, index):
        return self.players[index]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stub = PlayerReaderStub()
        self.stats = StatisticsService(self.stub)

    def test_search(self):
        self.assertEqual(self.stats.search("Semenko"), self.stub.get_player(0))
        self.assertEqual(self.stats.search("Pukki"), None)
        self.assertEqual(self.stats.search(""), None)

    def test_team(self):
        self.assertEqual(self.stats.team("MOI"), [])
        self.assertEqual(self.stats.team("EDM"), [self.stub.get_player(0),
                                                  self.stub.get_player(2),
                                                  self.stub.get_player(4)])

        self.assertEqual(self.stats.team("PIT"), [self.stub.get_player(1)])
        self.assertEqual(self.stats.team(""), [])

    def test_top(self):

        self.assertEqual(self.stats.top(-1), [])
        self.assertEqual(self.stats.top(0), [])
        self.assertEqual(self.stats.top(1), [self.stub.get_player(4)])
        self.assertEqual(self.stats.top(5), [self.stub.get_player(1),
                                             self.stub.get_player(3),
                                             self.stub.get_player(2),
                                             self.stub.get_player(0)])
