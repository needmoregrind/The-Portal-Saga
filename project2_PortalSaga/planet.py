from items import SparePart, ShipPiece, Portal
import random

class Planet:

    def __init__(self, size=15, starting=False):
        # TODO Part 1
        # Make the following instance fields
        # 1) The map is a size x size 2D Python list
        self.size = 15
        self.map = [[None for i in range(self.size)] for i in range(self.size)]
        self.starting = starting

        # If its the starting planet
        # Setup the starting map (when starting is True)
        # It has spaceship components, spare parts, and wormholes
        if self.starting == True:
            self.map[0][1] = ShipPiece("./Img/cabin_broken.ppm", 'broken', 'cabin')
            self.map[3][2] = ShipPiece("./Img/exhaust_broken.ppm", 'broken', 'exhaust')
            self.map[5][6] = ShipPiece("./Img/engine_broken.ppm", 'broken', 'engine')
            self.map[4][3] = ShipPiece("./Img/engine_broken.ppm", 'broken', 'engine')
            self.map[1][3]= ShipPiece("./Img/engine.ppm", 'working', 'engine')
            self.map[2][5]= ShipPiece("./Img/cabin.ppm", 'working', 'cabin')

        # Define part names corresponding to the image types
        part_types = [
            {"imageName": "./Img/bagel.ppm", "name": "bagel"},
            {"imageName": "./Img/gear.ppm", "name": "gear"},
            {"imageName": "./Img/lettuce.ppm", "name": "lettuce"},
            {"imageName": "./Img/cake.ppm", "name": "cake"},
        ]
        
        num_parts = random.randint(4,6) 
        for _ in range(num_parts):
            x,y =self.getEmptyLocation()
            part_type = random.choice(part_types)
            self.map[x][y] = SparePart(part_type["imageName"], part_type["name"])

        num_parts = random.randint(2,5) 
        for _ in range(num_parts):
            x,y =self.getEmptyLocation()
            self.map[x][y]= Portal()
            
        # If its not the starting planet
        # Setup a map for a planet that isn't the starting Planet
        # It has spare parts and wormholes
    
        # Examples of making all three items on a planet
        # x = SparePart("./Img/screw.ppm")
        # y = ShipPiece("./Img/cabin.ppm", "working")
        # z = Portal()

    def getEmptyLocation(self):
        # Optional method, but helpful for Part 1
        # Find an empty place in the map
        # Return its location as a list [row,col]

        # empty_locations = []
        # for row in range(len(self.map)):
        #     for col in range(len(self.map[row])):
        #         if self.map[row][col] is None:
        #             empty_locations.append([row,col])
        
        # if empty_locations:
        #     return random.choice(empty_locations)
        # else:
        #     return None

        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.map[x][y] is None:
                return [x,y]

    def isPortal(self, row, col):
        """Returns True if the item at the given position is a portal, False otherwise."""
        item = self.map[row][col]
        return item is not None and item.getKind() == "portal"

    def getPortal(self, row, column):
        """ Return the Portal at coordinates [row,col] or return None."""
        if 0 <= row < self.size and 0 <= column < self.size:
            if isinstance(self.map[row][column], Portal):
                return self.map[row][column]  # Return the portal object
        return None  # Return None if no portal is found at the location

    def findAPortal(self):
        """ Return the location [row,col] of some (unconnected) portal.    
        Return None if no unconnected portal is found. """
        for row in range(self.size):
            for col in range(self.size):
                # Check if the current map location contains a Portal
                if isinstance(self.map[row][col], Portal):
                    portal = self.map[row][col]
                    # Check if the portal is not connected
                    if not portal.isConnected():
                        return [row, col]  # Return the location of the unconnected portal
        return None  # Return None if no unconnected portal is found
    
    def setupWormhole(self, row, column):
        """ Make sure the wormhole is ready to go at coordinates[row, column] """
        print('setupWormhole')
        if not self.isPortal(row, column):
            return -1

        portal = self.getPortal(row, column)
        if portal.isConnected():
            return

        new_planet = Planet()
        portal_location = new_planet.findAPortal()  # Check portal location correctly
        
        # Check if no unconnected portal was found
        if portal_location is None:
            return  # No available portal to connect to
        
        new_row, new_col = portal_location
        new_portal = new_planet.getPortal(new_row, new_col)

        portal.setOtherPortal(new_portal)
        new_portal.setOtherPortal(portal)

        portal.setPlanet(self)
        portal.setLocation(row, column)
        new_portal.setPlanet(new_planet)
        new_portal.setLocation(new_row, new_col)
        print('DonesetupWormhole')

        return new_planet
    
    def getItemAt(self, row, col):
        """Return the item at the given map coordinates, or None if the space is empty."""
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.map[row][col]
        return None  # Return None if the coordinates are out of bounds