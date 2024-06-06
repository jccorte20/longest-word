from longest_word.game import Game
import string


class TestGame:

    def test_game_initialization(self):
        # setup
        new_game = Game()

        # exercise
        grid = new_game.grid

        # verify
        assert grid != None
        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_game_is_valid(self):
        # setup
        new_game = Game()

        # exercise
        grid = list('HELLORRER')
        words = ['HELLOZ','HELLO']

        # verify
        for word in words:
            if word == 'HELLOZ':
                assert new_game.is_valid(word) == False
            else:
                assert new_game.is_valid(word) == True 
