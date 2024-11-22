import unittest
from game import Game
from planet import Planet
from items import SparePart, ShipPiece, Portal

class TestGame(unittest.TestCase):
    def testInit(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        
        # TODO Part 1
        # Make a Game (don't call start())
        # Test that the instance fields are the correct types
        g = Game()
        self.assertIsInstance(g.planet, Planet)
        self.assertIsInstance(g.rover_row, int)
        self.assertIsInstance(g.rover_col, int)

    def testGoUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # Make a Game
        g = Game()
        # Set the rover location to a location of your choosing
        g.rover_row = 4 # chose more carefully than this
        g.rover_col = 8
        # (Don't set it where it will land on a portal. Remove the portal if needed)
        g.planet.map[3][8] = None
        # Call the goUp() method of the game
        g.goUp() # The GUI normally calls goUp but you can too
        # Test the rover's new location to make sure it has indeed gone up.
        self.assertEqual(g.rover_row, 3)
        self.assertEqual(g.rover_col, 8)

    def testGoDown(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        g = Game()
        g.rover_row = 5 # chose more carefully than this
        g.rover_col = 2
        g.planet.map[6][2] = None
        g.goDown()
        self.assertEqual(g.rover_row, 6)
        self.assertEqual(g.rover_col, 2)

    def testGoLeft(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        g = Game()
        g.rover_row = 8 # chose more carefully than this
        g.rover_col = 1
        g.planet.map[8][0] = None
        g.goLeft()
        self.assertEqual(g.rover_row, 8)
        self.assertEqual(g.rover_col, 0)
    
    def testGoRight(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 1
        # This is the same idea as goUp
        g = Game()
        g.rover_row = 10 # chose more carefully than this
        g.rover_col = 10
        g.planet.map[10][11] = None
        g.goRight()
        self.assertEqual(g.rover_row, 10)
        self.assertEqual(g.rover_col, 11)
    
    def testShowWayBack(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 2
        pass
    def testPickUp(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 3
        pass
    def testPerformTask(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify the related attributes to check if they updated correctly
        
        # TODO Part 3
        pass
    # add more test functions for other methods you have added (except simple gettter and setters methods)
    
if __name__ == '__main__':
    unittest.main()
    
