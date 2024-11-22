"""
Game to play 'Lost Rovers'. This is the file you edit.
To make more ppm files, open a gif or jpg in xv and save as ppm raw.
"""
from GUI.graphics import Point
from items import SparePart, ShipPiece, Portal
from planet import Planet
from stack import LinkedStack
from mylist import MyList
from myqueue import LinkedQueue
import random
from task import Task

class Game:
    SIZE = 15                 # 15x15 squares in the map

    def __init__(self):
        # TODO Part 1
        # Your game needs instance fields for:
        # 1) a Planet instance. This is the current planet you are on. 
        #      It begins as a starting planet.
        # 2) a rover location of row and column. This is where you are 
        #       on the map.  The rover starts in an empty location on the map.
        self.planet = Planet(Game.SIZE, starting=True)
        self.roverLocation = self.planet.getEmptyLocation()

        # TODO Part 2
        # Your game needs instance fields for:
        # 1) a Stack of Portals the rover has traveled through
        self.portal_stack = LinkedStack()
        initial_portal = self.planet.getPortal(*self.roverLocation)
        if initial_portal:
            self.portal_stack.push(initial_portal)

        # TODO Part 3
        # Your game needs instance fields for:
        # 1) a List of items in your inventory
        # 2) a Queue of tasks to fix the broken ship pieces
        self.inventory = MyList()
        self.tasks = LinkedQueue()

        self.fill_tasks_queue()

    def teleport(self):
        row, col = self.roverLocation
        if self.planet.isPortal(row, col):
            portal = self.planet.getPortal(row, col)
            planet = self.planet.setupWormhole(row, col)
            portal.setPlanet(planet)
            portal.setOtherPortal(portal)
            if portal:  # Ensure portal is not None
                self.portal_stack.push(portal)
                self.planet = portal.getPlanet()
                print(f"Portal pushed: {portal}, stack: {self.portal_stack}")

    def getRoverImage(self):
        """ Called by GUI when screen updates.
            Returns image name (as a string) of the rover. 
        (Likely './Img/rover.ppm') """
        # Only edit this if you get your own rover image
        return './Img/rover.ppm'

    def setRoverLocation(self, row, col):
        """ Used for autograder testing.
            Sets the rover's location to the given row and col. """
        self.roverLocation = [row, col]

    def getRoverLocation(self):
        """ Called by GUI when screen updates.
            Returns location (as a Point). """
        # TODO Part 1
        # return Point(column, row) # backwards of what you expect
        return Point(self.roverLocation[1], self.roverLocation[0])

    def getImage(self, point):
        """ Called by GUI when screen updates.
            Returns image name (as a string) or None for the 
            spare part, ship component, or portal at the given 
            point coordinates. (such as './Img/engine.ppm') """
        row = point.y # point is backwards of what you expect
        col = point.x
        # TODO Part 1
        if self.planet.map[row][col] is not None:
            return self.planet.map[row][col].getImageName()
        return None

    def goUp(self):
        """ Called by GUI when button clicked.
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        new_row = (self.roverLocation[0] - 1) % self.SIZE
        self.roverLocation[0] = new_row

        # Update the item at the new rover location
        item_at_location = self.planet.getItemAt(self.roverLocation[0], self.roverLocation[1])
        if item_at_location and item_at_location.getKind() == "portal":
            self.teleport()

    def goDown(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        new_row = (self.roverLocation[0] + 1) % self.SIZE
        self.roverLocation[0] = new_row

        # Update the item at the new rover location
        item_at_location = self.planet.getItemAt(self.roverLocation[0], self.roverLocation[1])
        if item_at_location and item_at_location.getKind() == "portal":
            self.teleport()

    def goLeft(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        new_col = (self.roverLocation[1] - 1) % self.SIZE
        self.roverLocation[1] = new_col

        # Update the item at the new rover location
        item_at_location = self.planet.getItemAt(self.roverLocation[0], self.roverLocation[1])
        if item_at_location and item_at_location.getKind() == "portal":
            self.teleport()

    def goRight(self):
        """ Called by GUI when button clicked. 
            If legal, moves rover. If the robot lands
            on a portal, it will teleport. """
        # TODO Part 1
        # If legal, moves rover
        new_col = (self.roverLocation[1] + 1) % self.SIZE
        self.roverLocation[1] = new_col

        # Update the item at the new rover location
        item_at_location = self.planet.getItemAt(self.roverLocation[0], self.roverLocation[1])
        if item_at_location and item_at_location.getKind() == "portal":
            self.teleport()

    def showWayBack(self):
        """ Called by GUI when button clicked.
            Flash the portal leading towards home. """
        # TODO Part 2
        print("Stack before peeking:", self.portal_stack)  # Debugging
        if not self.portal_stack.isEmpty():
            last_portal = self.portal_stack.peek()
            print(f"Peeking at stack: {last_portal}")  # Debugging
            if last_portal.getPlanet() == self.planet:
                return last_portal.getLocation()
        return None

    def getInventory(self):
        """ Called by GUI when inventory updates.
            Returns entire inventory (as a string). 
        3 cake
        2 screws
        1 rug
      """
        # TODO Part 3
        inventory_summary = {}
        # Count each type of part in the inventory
        for i in range(len(self.inventory)):
            part = self.inventory.peek(i)
            part_name = part.getName()
            if part_name in inventory_summary:
                inventory_summary[part_name] += 1
            else: 
                inventory_summary[part_name] = 1

        sorted_items = sorted(inventory_summary.items())

        inventory_lines= []
        for item_name, count in sorted_items:
            if count > 1:
                plural_item = item_name + 's'
                inventory_lines.append(f"{count} {plural_item}")
            else:
                inventory_lines.append(f"{count} {item_name}")

        inventory_string = '\n'.join(inventory_lines)
    
        return inventory_string if inventory_string else ''

    def pickUp(self):
        """ Called by GUI when button clicked. 
        If rover is standing on a part (not a portal 
        or ship component), pick it up and add it
        to the inventory. """
        # TODO Part 3

        # Get the item at the rover's current location on the map
        row, col = self.roverLocation
        current_item = self.planet.getItemAt(row, col)

        if current_item and current_item.getKind() == 'part':
            # Correctly instantiate SparePart with both imageName and name
            spare_part = SparePart(imageName = current_item.getImageName(), name = current_item.getName())
            self.inventory.insert(spare_part)
            self.planet.map[row][col] = None  # Remove part from the map
            # print(f"Picked up: {spare_part.getName()}")

    def performTask(self):
        # Check if there are no tasks left, meaning we've already won
        if self.tasks.is_empty():
            print("You win!")
            return

        # Get the current task at the front of the queue
        current_task = self.tasks.peek()
        task_name = current_task.getName()
        components_needed = current_task.getComponents()

        # Check if the rover is on the correct ship piece to perform the task
        row, col = self.roverLocation
        item_at_location = self.planet.getItemAt(row, col)
        if not (item_at_location and item_at_location.getKind() == "ship_piece" and item_at_location.getName() == task_name):
            print("Rover is not at the correct location to perform the task.")
            return

        # Check if the player has all the required components in their inventory
        has_all_components = True
        for part_name, amount_needed in components_needed.items():
            if self.inventory.count(part_name) < amount_needed:
                has_all_components = False
                break

        if has_all_components:
            # Fix the ship piece: set its status to "working"
            item_at_location.setStatus("working")

            # Remove used parts from the inventory
            for part_name, amount_needed in components_needed.items():
                for _ in range(amount_needed):
                    self.inventory.remove(part_name)

            # Dequeue the completed task from the tasks queue
            self.tasks.dequeue()
            print(f"{task_name} has been fixed.")
        else:
            print("You don't have all the required components to fix this ship piece.")

    def create_random_task(self, name):
        """Create a Task with a random number of spare parts."""
        task = Task(name)
        # List of possible components
        possible_components = ['lettuce', 'bagel', 'gear', 'cake']

        # Randomly choose the number of components (between 2 and 4)
        num_components = random.randint(2, 4)
        # Randomly select components
        selected_components = random.sample(possible_components, num_components)

        for component in selected_components:
            # Assign a random count (above 0)
            count = random.randint(1, 10)  # Random number between 1 and 10
            task.addComponent(count, component)
    
        return task
    
    def fill_tasks_queue(self):
        """Fill the tasks queue with tasks for broken ship pieces."""
        
        # Define names for tasks representing broken ship pieces
        task_names = ['cabin', 'exhaust', 'engine']

        # Create and enqueue each task into self.tasks
        for name in task_names:
            task = self.create_random_task(name)  # Create a Task instance
            self.tasks.enqueue(task)  # Enqueue the Task instance to LinkedQueue

    def getCurrentTask(self):
        """ Called by GUI when task updates.
            Returns top task (as a string). 
		'Fix the engine using 2 cake, 3 rugs' or
		'You win!' 
 	  """
        # TODO Part 3
        # Check if there are no tasks left
        if self.tasks.is_empty():
            return "You win!"  # Return winning message if no tasks are in the queue
        
        # Get the current task at the front of the queue without removing it
        current_task = self.tasks.peek()
        
        if current_task is None:
            return "You win!"  # Safety check if the queue unexpectedly contains None

        task_name = current_task.getName()
        components = current_task.getComponents()
        components_str = ", ".join(f"{amount} {name}" for name, amount in components.items())
        return f"Fix the {task_name} using {components_str}"