import unittest
from planet import Planet
from items import SparePart, ShipPiece, Portal

class TestPlanet(unittest.TestCase):
    def testInstanceFields(self):
        # The below fails so you remember to replace it with a real test
        # Hint: you need to verify if the attributes are initialized as they should
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True) 
        # Test the type of each instance field
        self.assertEqual(p.size, 15)
        self.assertTrue(p.starting)
        self.assertIsInstance(p.size, int)
        self.assertIsInstance(p.starting, bool)
    
    def testShipPieces(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of ship components to make sure there are enough
        # and they have the correct variety (broken, etc)
        total_ship_pieces = 0
        broken_ship_pieces = 0
        unique_kinds = set()

        for row in p.map:
            for obj in row:
                if isinstance(obj, ShipPiece):
                    total_ship_pieces += 1
                    if 'broken' in obj.getImageName():
                        broken_ship_pieces += 1
                    unique_kinds.add(obj.getImageName())

        self.assertGreaterEqual(total_ship_pieces, 5)
        self.assertGreaterEqual(broken_ship_pieces, 4)
        self.assertGreaterEqual(len(unique_kinds), 3)

    def testSpareParts(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of spare parts to make sure there are enough
        # Also test that multiple sorts of spare parts are represented

        # Make second, third, and fourth starting Planets
        # Get the number of spare parts of each
        # Test that they do not all have the same number of spare parts.
        total_spare_parts = 0
        unique_kinds = set()
        for row in p.map:
            for obj in row:
                if isinstance(obj, SparePart):
                    total_spare_parts += 1
                    unique_kinds.add(obj.getImageName())

        self.assertGreaterEqual(total_spare_parts, 3)
        self.assertGreaterEqual(len(unique_kinds), 3)

        p2 = Planet(15, True)

        total_spare_parts_2 = 0
        for row in p2.map:
            for obj in row:
                if isinstance(obj, SparePart):
                    total_spare_parts_2 += 1

        p3 = Planet(15, True)
        total_spare_parts_3 = 0
        for row in p3.map:
            for obj in row:
                if isinstance(obj, SparePart):
                    total_spare_parts_3 += 1

        p4 = Planet(15, True)
        total_spare_parts_4 = 0
        for row in p4.map:
            for obj in row:
                if isinstance(obj, SparePart):
                    total_spare_parts_4 += 1

        self.assertNotEqual(total_spare_parts_2, total_spare_parts_3)
        self.assertNotEqual(total_spare_parts_3, total_spare_parts_4)
        self.assertNotEqual(total_spare_parts_2, total_spare_parts_4)

    def testPortals(self):
        # The below fails so you remember to replace it with a real test
        
        # TODO Part 1
        # Make a starting Planet
        p = Planet(15, True)
        # Test the number of portals to make sure there are enough
        total_portals = 0
        for row in p.map:
            for obj in row:
                if isinstance(obj, Portal):
                    total_portals += 1

        self.assertEqual(total_portals, 2)

        # Make second, third, and fourth starting Planets
        # Get the number of portals of each
        # Test that they do not all have the same number of portals.
        p2 = Planet(15, True)
        total_portals_2 = 0
        for row in p2.map:
            for obj in row:
                if isinstance(obj, Portal):
                    total_portals_2 += 1

        p3 = Planet(15, True)
        total_portals_3 = 0
        for row in p3.map:
            for obj in row:
                if isinstance(obj, Portal):
                    total_portals_3 += 1

        p4 = Planet(15, True)
        total_portals_4= 0
        for row in p4.map:
            for obj in row:
                if isinstance(obj, Portal):
                    total_portals_4 += 1
        self.assertNotEqual(total_portals_2, total_portals_3)
        self.assertNotEqual(total_portals_2, total_portals_4)
        self.assertNotEqual(total_portals_3, total_portals_4)

if __name__ == '__main__':
    unittest.main()
