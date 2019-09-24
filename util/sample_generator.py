# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.
import random
from api.models import Player, Room, Item



def gen_room(self, ranInt, roomId):
    room_names = ["Prehistoric Cave", "Medieval Wizards Tower", "Abandoned Cottage", "Alchemists Laboratory", "Viking Barracks",
                    "Roman Colloseseum", "London Shop", "Futuristic Lab", "Barbaric Outpost", "Western Town", "Colonial Puritan Church",
                    "Nazi Meeting Hall", "Chinese Pagoda", "Cold War Nuclear Site", "Beached Pirate Ship"]
    room_descriptions = ["This seems to be one of the first shelters ever to be used by mankind. A special sort of novelty. Also, it seems pretty empty...",
                         "A magical place! This is the type of place you hear about in a story book! I never knew that they were real, once upon a time....",
                         "This cottage seems to have been left long ago. The place is a bit worse for ware. I wonder who used to live here?",
                         "Ah, this is a place dedicated to one thing, THE SEARCH FOR GOLD! But not in the conventional way. It doesn't seem like they ever had much luck.",
                         "A rough and run down place. You see weapons of all sorts lying around, and what appears to be a half eaten turkey leg...",
                         "The birthplace of entertainment! People are all around, and you can faintly hear the roar of the lion in its cage.",
                         "A daily visit for most in this cobblestone village. Goods from all around, and some say this is the best place for gossip.",
                         "Everything around you is either chrome or the brightest white you've ever seen. This is the epitome of a sterile environment.",
                         "The people around here look like they're in a \"Homeless Cave Man\" costume contest. They smell like it too...",
                         "Ah, the Wild West! Just how the movies always depicted it. A real life western saloon complete with a spitoon on the deck!",
                         "The people around here look nice enough, but you'd best stand up straight and remember your please and thank you's",
                         "You never thought you'd be anywhere on this side of the war. This place looks fine enough, it's more the people you are worried about.",
                         "This place is the epitome of the far east. From the finial at the top, to the feng-shui garden on the ground below.",
                         "This place is oozing with secrecy. You can feel the tension in the air. No one seems to be very friendly of outsiders here...",
                         "ARGH ME MATEY! A real life pirate ship! I wonder if there is any \"booty\" on board?"]
    room = Room(roomId, room_names[ranInt], room_descriptions[ranInt])
    return room

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_x
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_y

        idCount = 0
        for x in range(size_x):
            for y in range(size_y):
                ranInt = random.randint(0,9)
                if ranInt < 6:
                    room = Room(idCount, "Road", "Just a dusty old road")
                    idCount += 1
                    self.grid[x][y] = room
                    room.save()
                else:
                    ran = random.randint(0,14)
                    room = gen_room(ran, idCount)
                    idCount += 1
                    self.grid[x][y] = room
                    room.save()



            # Create a room in the given direction
            #room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.grid[y][x] = room

            #room_count += 1




    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 44
width = 8
height = 7
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
