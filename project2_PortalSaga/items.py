""" Classes for items that appear in the map (except the rover).
    Each class has a getKind() method which returns what sort of 
    item it is as a String.
"""

class SparePart:
    def __init__(self, imageName, name = ''):
        # TODO Part 1
        # Make the following instance fields
        # 1) The image name
        self.imageName = imageName
        self.name = name

    def getImageName(self):
        # TODO Part 1
        # return the image name including the imagepath if any
        return self.imageName

    def getKind(self):
        return 'part'
    
    def getName(self):
        """Return a string representation of the spare part’s name."""
        return self.name

class ShipPiece:
    def __init__(self, imageName, status, name = ''):
        # TODO Part 1
        # Make the following instance fields
        # 1) The image name
        # 2) Its status; is it broken or working?
        self.imageName = imageName
        self.status = status
        self.name = name

    def getImageName(self):
        # TODO Part 1
        # return the image name including the imagepath if any
        """Return the image name based on the status of the ship piece."""
        if self.status == "broken":
            return './Img/cabin_broken.ppm'  # Return broken image
        return './Img/cabin_.ppm'  # Return working image
        
    def getKind(self):
        return "ship"
    
    def getStatus(self):
        # TODO Part 1
        # return "broken" or "working"
        return self.status
    
    def getName(self):
        return self.name
    
    def setStatus(self, status):
        """Set the status of the ship piece to 'working' or 'broken'."""
        self.status = status
        
class Portal:
    def __init__(self):
        # TODO Part 1
        # Make the following instance fields
        # 1) The current image name ("./Img/portal.ppm" or "./Img/portal_flashing.ppm")
        self.currentimage = "./Img/portal_flashing.ppm"

        # TODO Part 2
        # Make the following instance fields
        # 1) The map that this portal is on
        # 2) The location [row, column] of this portal on this map
        # 3) The portal at the other end of the wormhole (None if it isn't known yet)
        self._location = None
        self._portal = None
        self._planet = None

    def getImageName(self):
        # TODO Part 1
        # return the image name including the imagepath if any
        return self.currentimage

    def getKind(self):
        return "portal"
    
    def isConnected(self):
        """ Check if this portal is connected to another portal. """
        return self._portal is not None
    
    def setPlanet(self, planet):
        """ Set the planet the portal is on. """
        self._planet = planet

    def getPlanet(self):
        """ Get the planet the portal is on. """
        return self._planet
    
    def setLocation(self, row, column):
        """ Set the location of the portal on the map. """
        self._location = [row, column]
    
    def getLocation(self):
        """ Get the location of the portal. """
        return self._location
    
    def setOtherPortal(self, portal):
        """ Set the portal on the other end of the wormhole. """
        self._portal = portal

    def getOtherPortal(self):
        """ Get the portal on the other end of the wormhole. """
        return self._portal