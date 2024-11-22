import unittest
from game import Game
from planet import Planet
from items import Portal

class TestGame2(unittest.TestCase):

    def test_setup_wormhole(self):
        game = Game()
        planet = game.planet
        portal_location = None
        for row in range(Game.SIZE):
            for col in range(Game.SIZE):
                if planet.isPortal(row, col):
                    portal_location = [row, col]
                    break
            if portal_location:
                break
        
        self.assertIsNotNone(portal_location, "No portal found on the planet")
        
        planet.setupWormhole(portal_location[0], portal_location[1])
        portal = planet.getPortal(portal_location[0], portal_location[1])
        
        self.assertIsNotNone(portal.getOtherPortal(), "Other portal not set")
        self.assertIsNotNone(portal.getPlanet(), "Planet not set")
        self.assertEqual(portal.getLocation(), portal_location, "Location not set correctly")

    def test_unconnected_teleport(self):
        game = Game()
        planet = game.planet
        portal_location = None
        for row in range(Game.SIZE):
            for col in range(Game.SIZE):
                if planet.isPortal(row, col):
                    portal_location = [row, col]
                    break
            if portal_location:
                break
        
        self.assertIsNotNone(portal_location, "No portal found on the planet")
        
        original_planet = game.planet
        game.setRoverLocation(portal_location[0], portal_location[1])
        game.teleport()
        
        self.assertNotEqual(game.planet, original_planet, "Planet didn't change after teleport")
        self.assertNotEqual(game.getRoverLocation(), portal_location, "Location didn't change after teleport")

    def test_connected_teleport(self):
        game = Game()
        planet = game.planet
        portal_location = None
        for row in range(Game.SIZE):
            for col in range(Game.SIZE):
                if planet.isPortal(row, col):
                    portal_location = [row, col]
                    break
            if portal_location:
                break
        
        self.assertIsNotNone(portal_location, "No portal found on the planet")
        
        original_planet = game.planet
        game.setRoverLocation(portal_location[0], portal_location[1])
        game.teleport()
        game.teleport()
        
        self.assertEqual(game.planet, original_planet, "Didn't return to original planet after double teleport")
        self.assertEqual(game.getRoverLocation(), portal_location, "Didn't return to original location after double teleport")

    def test_show_way_back(self):
        game = Game()
        planet = game.planet
        portal_location = None
        for row in range(Game.SIZE):
            for col in range(Game.SIZE):
                if planet.isPortal(row, col):
                    portal_location = [row, col]
                    break
            if portal_location:
                break
        
        self.assertIsNotNone(portal_location, "No portal found on the planet")
        
        game.setRoverLocation(portal_location[0], portal_location[1])
        game.teleport()
        way_back_location = game.showWayBack()
        
        self.assertIsNotNone(way_back_location, "showWayBack() returned None")
        portal = game.planet.getPortal(way_back_location[0], way_back_location[1])
        self.assertEqual(portal.getImage(), './Img/portal_flashing.ppm', "Portal is not flashing")

if __name__ == '__main__':
    unittest.main()