
import random
from api.models import Player, Room, Item


def gen_room(ranInt, roomId):
    room_names = ["Prehistoric Cave", "Medieval Wizards Tower", "Abandoned Cottage", "Alchemists Laboratory", "Viking Barracks",
                    "Roman Colosseum", "London Shop", "Futuristic Lab", "Barbaric Outpost", "Western Town", "Colonial Puritan Church",
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
    def generate_rooms(self, size_x, size_y):
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
                    room.positionx = x
                    room.positiony = y
                    room.save()
                else:
                    ran = random.randint(0,14)
                    room = gen_room(ranInt=ran, roomId=idCount)
                    idCount += 1
                    self.grid[x][y] = room
                    room.positionx = x
                    room.positiony = y
                    room.save()

w = World()
width = 20
height = 20
w.generate_rooms(width, height)
item = Item(1,
             "Torch",
             "This can light your path in the dark",
             "Prehistoric Cave",
             1)
item.save()
item = Item(2,
             "Bag of Jerky",
             "You can smell the beef",
             "Prehistoric Cave",
             2)
item.save()
item = Item(3,
             "Meat Club",
             "Part snack, part weapon",
             "Prehistoric Cave",
             3)
item.save()
item = Item(4,
             "Animal Skin Cloak",
             "A small amount of protection",
             "Prehistoric Cave",
             4)
item.save()
item = Item(5,
             "Dino-Tooth Saber",
             "Wickedly sharp",
             "Prehistoric Cave",
             5)
item.save()
item = Item(6,
            "Magic Wand",
            "A smooth stick with some strange engravings on the side. It feels like it has some kind of hidden power.",
            "Medieval Wizards Tower",
            1)
item.save()
item = Item(7,
            "Wizards Hat",
            "A silly old blue tattered hat that comes to a ridiculous point at the top",
            "Medieval Wizards Tower",
            2)
item.save()
item = Item(8,
            "Cloth Shoes",
            "Seriously, who would wear these?",
            "Medieval Wizards Tower",
            3)
item.save()
item = Item(9,
            "Book O' Spells",
            "A book that appears to be written in Latin or some other dead language. You can barely make out most of the text.",
            "Medieval Wizards Tower",
            4)
item.save()
item = Item(10,
            "\"A History of Imps and things\"",
            "\"Written by A.J. Holden. A book of need to knows when faced with those little red devils.\"",
            "Medieval Wizards Tower",
            5)
item.save()
item = Item(11,
            "Magical Pet Rock",
            "One of those silly rocks with the googley eyes. This one has some weird energy coming off of it though.",
            "Medieval Wizards Tower",
            6)
item.save()
item = Item(12,
            "Lock of white beard hair",
            "Gross. Looks like someones grampa shaved in here",
            "Medieval Wizards Tower",
            7)
item.save()
item = Item(13,
            "Broken Glasses",
            "Some unfortunate chap seems to be going blind today",
            "Medieval Wizards Tower",
            8)
item.save()
item = Item(14,
            "A Frog Named Harold",
            "This frog has a collar, and the name says \"Harold\"....?",
            "Medieval Wizards Tower",
            9)
item.save()
item = Item(15,
            "Scrappy Book",
            "All the pages are faded, and what you can make out appears to be in a strange language",
            "Abandoned Cottage",
            1)
item.save()
item = Item(16,
            "Healing Potion",
            "Provides a moderate amount of healing",
            "Abandoned Cottage",
            2)
item.save()
item = Item(17,
            "Warm Blanket",
            "Increases your ability to take rests",
            "Abandoned Cottage",
            3)
item.save()
item = Item(18,
            "Wooden Spoon",
            "Doesn't seem like it'd be very useful",
            "Abandoned Cottage",
            4)
item.save()
item = Item(19,
            "Box of Matches",
            "You can start a fire with these",
            "Abandoned Cottage",
            5)
item.save()
item = Item(20,
            "Old Scroll",
            "Looks like some kind of incantation",
            "Abandoned Cottage",
            6)
item.save()
item = Item(21,
            "Gleaming Longsword",
            "It's heavy, but in good condition",
            "Abandoned Cottage",
            7)
item.save()
item = Item(22,
            "Potion of Strength",
            "Drinking this will make your muscles BULGE!",
            "Alchemists' Laboratory",
            1)
item.save()
item = Item(23,
            "Potion of Mystery",
            "Causes unknown effect",
            "Alchemists' Laboratory",
            2)
item.save()
item = Item(24,
            "Potion of Invisibility",
            "Drinking this will make you invisible",
            "Alchemists' Laboratory",
            3)
item.save()
item = Item(25,
            "Empty Vial",
            "Maybe you can fill it with something.",
            "Alchemists' Laboratory",
            4)
item.save()
item = Item(26,
            "Alchemist's cookbook",
            "Probably worth something to the right person",
            "Alchemists' Laboratory",
            5)
item.save()
item = Item(27,
            "Strong Potion of Healing",
            "This is the good stuff!",
            "Alchemists' Laboratory",
            6)
item.save()
item = Item(28,
            "Half-eaten Turkey leg",
            "Looks like someone didn't get to finish their lunch",
            "Viking Barracks",
            1)
item.save()
item = Item(29,
            "Giant War Axe",
            "This thing looks like it could do some real damage",
            "Viking Barracks",
            2)
item.save()
item = Item(30,
            "Leather Tunic",
            "It looks incredibly uncomfortable if worn for extended periods of time",
            "Viking Barracks",
            3)
item.save()
item = Item(31,
            "Chainmail Armor",
            "A marvel of defense. Breathability, and Get-stabbed-ability",
            "Viking Barracks",
            4)
item.save()
item = Item(32,
            "Goat Horn Challice",
            "Looks like it's time to grab the mead",
            "Viking Barracks",
            5)
item.save()
item = Item(33,
            "Authentic Gold Coins",
            "A good day of pillaging always ends up with some of these in your pocket",
            "Viking Barracks",
            6)
item.save()
item = Item(34,
            "Blood-stained Shield",
            "This thing looks like it has seen some battle.",
            "Viking Barracks",
            7)
item.save()
item = Item(35,
            "Iron Spear",
            "A weapon used by gladiators",
            "Roman Colosseum",
            1)
item.save()
item = Item(36,
            "Iron Axe",
            "The arc of the axe is sharp to the touch",
            "Roman Colosseum",
            2)
item.save()
item = Item(37,
            "Iron Dagger",
            "There is blood stained across the hilt",
            "Roman Colosseum",
            3)
item.save()
item = Item(38,
            "Iron Sword",
            "A good all-around weapon",
            "Roman Colosseum",
            4)
item.save()
item = Item(39,
            "Coin Purse",
            "Used to hold coins",
            "Roman Colosseum",
            5)
item.save()
item = Item(40,
            "Leather Armor",
            "Provides mobility and protection",
            "Roman Colosseum",
            6)
item.save()
item = Item(41,
            "Shield of Champions",
            "A very Strong shield made of an amalgamation of different metals",
            "Roman Colosseum",
            7)
item.save()
item = Item(42,
            "Monocle",
            "The epitome of class! Also, the epitome of corrective glass.",
            "London Shop",
            1)
item.save()
item = Item(43,
            "Glass Figurine",
            "I've never understood why people get so worked up about collecting these things.",
            "London Shop",
            2)
item.save()
item = Item(44,
            "Old Timey Globe",
            "This doesn't make much sense. Half of the world just says \"British Colonial Area\"",
            "London Shop",
            3)
item.save()
item = Item(45,
            "English to French Dictionary",
            "Ce livre pourrait être utile si vous alliez en France",
            "London Shop",
            4)
item.save()
item = Item(46,
            "Antique Teapot",
            "Good for antique tea, and the like.",
            "London Shop",
            5)
item.save()
item = Item(47,
            "Cash Register",
            "Oh, a spot of bad luck. It seems that someone has already cleared it out.",
            "London Shop",
            6)
item.save()
item = Item(48,
            "Accounting Book",
            "Now I'm no Auditer, but \"Definitely not money laundering\" seems pretty suspicious...",
            "London Shop",
            7)
item.save()
item = Item(49,
            "Mipmorp",
            "What could this possibly do?",
            "Futuristic Lab",
            1)
item.save()
item = Item(50,
            "Bic Pen",
            "You could use this to write messages, if you had some paper",
            "Futuristic Lab",
            2)
item.save()
item = Item(51,
            "Laser Pointer",
            "Great for distraction, or giving a seminar",
            "Futuristic Lab",
            3)
item.save()
item = Item(52,
            "Robo-Cat",
            "This indifferent companion doesn't seem too fond of you",
            "Futuristic Lab",
            4)
item.save()
item = Item(53,
            "Scientist's Notes",
            "This seems worthless to you",
            "Futuristic Lab",
            5)
item.save()
item = Item(54,
            "3D goggles",
            "Putting these on turns the entire world 3d. Amazing!",
            "Futuristic Lab",
            6)
item.save()
item = Item(55,
            "Tin-Foil Hat",
            "Provides protection from certain types of mind-control",
            "Futuristic Lab",
            7)
item.save()
item = Item(56,
            "Laser-Gun",
            "It looks like this weapon uses the health of the user as a power source",
            "Futuristic Lab",
            8)
item.save()
item = Item(57,
            "Invisability Apparatus",
            "Attaching this to your back could turn you invisible, but it might drain your HP to supply the power",
            "Futuristic Lab",
            9)
item.save()
item = Item(58,
            "Pile O' Bones",
            "Eeew",
            "Barbaric Outpost",
            1)
item.save()
item = Item(59,
            "Skull Challice",
            "This looks like it would be perfect to hold the blood of your enemies",
            "Barbaric Outpost",
            2)
item.save()
item = Item(60,
            "Sharp Stick",
            "Poke poke",
            "Barbaric Outpost",
            3)
item.save()
item = Item(61,
            "Assorted Furs",
            "These are some high quality skins! Good for keeping you warm through those harsh, unrelenting winters.",
            "Barbaric Outpost",
            4)
item.save()
item = Item(62,
            "Loincloth",
            "Put this on, and all you need is a vine. Look out Tarzan, there's a new hero in town.",
            "Barbaric Outpost",
            5)
item.save()
item = Item(63,
            "Steel Revolver",
            "Allows you to attack at range",
            "Western Town",
            1)
item.save()
item = Item(64,
            "Box of Bullets",
            "Plenty of Ammo in here",
            "Western Town",
            2)
item.save()
item = Item(65,
            "Cowbow Chaps",
            "These would be embarrassing to wear, but they would provide some protection",
            "Western Town",
            3)
item.save()
item = Item(66,
            "Dusty Gearbox",
            "This primitive machine fits in your hand, and seems to track time, or something",
            "Western Town",
            4)
item.save()
item = Item(67,
            "Pint of Beer",
            "This should take the edge off of your wounds",
            "Western Town",
            5)
item.save()
item = Item(68,
            "Shot of Whiskey",
            "This should take the edge off of your troubles",
            "Western Town",
            6)
item.save()
item = Item(69,
            "Stonejug of MoonShine",
            "This should take a few weeks off of your lifespan",
            "Western Town",
            7)
item.save()
item = Item(70,
            "\"A Purely Puritan Book of Morals\"",
            "Just inside the front cover, it says \"Read this and know how much of a heathen thou hast been\"",
            "Colonial Puritan Church",
            1)
item.save()
item = Item(71,
            "Book of Hymns",
            "The tastiest of jams coming straight from the Sunday slaps playlist",
            "Colonial Puritan Church",
            2)
item.save()
item = Item(72,
            "Shoe with a Buckle",
            "Now I'm no shoe engineer, but it seems like a buckle might not be the most efficient fastening device",
            "Colonial Puritan Church",
            3)
item.save()
item = Item(73,
            "\"How to Identify a Witch\"",
            "It says \"If you suspect one of being a heathenous witch. Drown the heretic in the lake. If they return unharmed, they are a witch. If they drown to death, they were an innocent\"",
            "Colonial Puritan Church",
            4)
item.save()
item = Item(74,
            "Washboard",
            "This looks like the bane of my laundry day",
            "Colonial Puritan Church",
            5)
item.save()
item = Item(75,
            "Gold Cross Necklace",
            "Looks like it came straight from the neck of a modern day street thug",
            "Colonial Puritan Church",
            6)
item.save()
item = Item(76,
            "Tactical Map",
            "The map is divided by \"Conquered\" and \"Yet to be conquered\"",
            "Nazi Meeting Hall",
            1)
item.save()
item = Item(77,
            "Kongsberg Colt handgun",
            "A true mark of history in the means of handgun technology",
            "Nazi Meeting Hall",
            2)
item.save()
item = Item(78,
            "SS Uniform",
            "This thing looks incredibly uncomfortable. No wonder why they were so angry all the time.",
            "Nazi Meeting Hall",
            3)
item.save()
item = Item(79,
            "Military Blueprints",
            "It says \"Turn to other side for even bigger bomb\"",
            "Nazi Meting Hall",
            4)
item.save()
item = Item(80,
            "Mein Kampf",
            "Nothing says humble like a book about how great you are at overcoming anything...",
            "Nazi Meeting Hall",
            5)
item.save()
item = Item(81,
            "Flowery Kimono",
            "These are worn by men too, you know",
            "Chinese Pagoda",
            1)
item.save()
item = Item(82,
            "Black Kimono",
            "The fabric flows, and has a golden dragon embedded on the back",
            "Chinese Pagoda",
            2)
item.save()
item = Item(83,
            "Practice Katana",
            "The bamboo shaft looks like it has some wear",
            "Chinese Pagoda",
            3)
item.save()
item = Item(84,
            "Steel Katana",
            "Ouch! It's sharp..",
            "Chinese Pagoda",
            4)
item.save()
item = Item(85,
            "Shogun Helmet",
            "Provides great protection",
            "Chinese Pagoda",
            5)
item.save()
item = Item(86,
            "Shogun Armor",
            "This armor is bulky, but effective",
            "Chinese Pagoda",
            6)
item.save()
item = Item(87,
            "Big Red Nuclear Button",
            "If only it was attached to something...",
            "Cold War Nuclear Site",
            1)
item.save()
item = Item(88,
            "Hazmat Suit",
            "This must be how cockroaches plan to survive a Nuclear Winter",
            "Cold War Nuclear Site",
            2)
item.save()
item = Item(89,
            "Launch Codes",
            "They just leave these things lying around?!?!? That seems incredibly irresonsible",
            "Cold War Nuclear Site",
            3)
item.save()
item = Item(90,
            "Russian Planted Bug",
            "Looks like someone is listening...",
            "Cold War Nuclear Site",
            4)
item.save()
item = Item(91,
            "Handcuffed Briefcase",
            "I don't know where the hand is, but it seems to be slacking at it's job.",
            "Cold War Nuclear Site",
            5)
item.save()
item = Item(92,
            "Gold Coin",
            "You can see light reflected from its surface",
            "Beached Pirate Ship",
            1)
item.save()
item = Item(93,
            "Bag of Gold",
            "You're rich!",
            "Beached Pirate Ship",
            2)
item.save()
item = Item(94,
            "Cutlass",
            "A large blade with a ring on one end of the hilt",
            "Beached Pirate Ship",
            3)
item.save()
item = Item(95,
            "Fake Pirate Beard",
            "I guess some pirates don't grow it naturally",
            "Beached Pirate Ship",
            4)
item.save()
item = Item(96,
            "Captain's Hat",
            "Very prestigious.",
            "Beached Pirate Ship",
            5)
item.save()
item = Item(97,
            "Ankle Pistol",
            "Only a truly nefarious person would need this",
            "Beached Pirate Ship",
            6)
item.save()
item = Item(98,
            "One Bullet Revolver",
            "A pirate keeps this as a last resort",
            "Beached Pirate Ship",
            7)
item.save()
item = Item(99,
            "Golden Revolver",
            "A truly rich pirate once owned this. It fires gold coins with deadly propulsion",
            "Beached Pirate Ship",
            8)
item.save()
print(f"\n\nWorld\n  height: {height}\n  width: {width}")
