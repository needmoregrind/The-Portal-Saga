from game import Game
from gameboard import GameBoard

g = Game()
gui = GameBoard("The Portal Saga", g, Game.SIZE)
gui.run()
