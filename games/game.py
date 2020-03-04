class Room:
    """Represents a room in a house. Can contain things."""

    def __init__(self, room):
        """
        Initializes a room.
        :param room: str
        """
        self.__room = room
        self.__description = ""
        self.__character = None
        self.__item = None
        self.__linked_rooms = {"north": None,
                               "south": None,
                               "west": None,
                               "east": None}

    def set_description(self, description):
        """
        Sets a room description.
        :param description: str
        :return: None
        """
        self.__description = description

    def link_room(self, other, direction):
        """
        Links this room to a different one in some direction.
        :param other: Room
        :param direction: str
        :return: None
        """
        if isinstance(other, Room):
            self.__linked_rooms[direction] = other

    def get_name(self):
        """
        Returns the room name.
        :return: str
        """
        return self.__room

    def set_character(self, character):
        """
        Sets the character in the room.
        :param character: Enemy
        :return: None
        """
        self.__character = character

    def get_character(self):
        """
        Gets the character in the room.
        :return: Enemy
        """
        return self.__character

    def set_item(self, item):
        """
        Sets the item in the room.
        :param item: Item
        :return: None
        """
        self.__item = item

    def get_item(self):
        """
        Gets the item in the room.
        :return: Item
        """
        return self.__item

    def move(self, direction):
        """
        Returns a linked room in the given direction.
        :param direction: str
        :return: Room
        """
        return self.__linked_rooms[direction]

    def get_details(self):
        """
        Prints out the details about this room.
        :return: None
        """
        print(f'''{self.__room}
--------------------
{self.__description}''')
        for direction, room in self.__linked_rooms.items():
            if room is not None:
                print(f'The {room.get_name()} is {direction}')


class Enemy:
    """Represents a living enemy that inhabits the rooms."""

    __defeated_enemies = 0

    def __init__(self, name, description=""):
        """
        Initializes an enemy.
        :param name: str
        :param description: str
        """
        self.__name = name
        self.__description = description
        self.__conversation = ""
        self.__weakness = None

    def set_conversation(self, conversation):
        """
        Sets the conversation for the character.
        :param conversation: str
        :return: None
        """
        self.__conversation = conversation

    def set_weakness(self, weakness):
        """
        Sets the weakness for the character.
        :param weakness: str
        :return: None
        """
        self.__weakness = weakness

    def describe(self):
        """
        Describes this enemy.
        :return: None
        """
        print(f'{self.__name} is here!\n{self.__description}')

    def talk(self):
        """
        Makes this enemy talk to you.
        :return: None
        """
        print(f'[{self.__name} says]: {self.__conversation}')

    def fight(self, weapon):
        """
        Determines the result of a fight with this enemy.
        The chosen weapon must equal the weakness.
        :param weapon: str
        :return: bool
        """
        if weapon == self.__weakness:
            print(f'You fend {self.__name} off with the {weapon}')
            Enemy.__defeated_enemies += 1
            return True
        else:
            print(f'{self.__name} crushes you, puny adventurer!')
            return False

    @classmethod
    def get_defeated(cls):
        """
        Returns the number of defeated enemies.
        :return: int
        """
        return cls.__defeated_enemies


class Item:
    """Represents an item that lies in the rooms."""

    def __init__(self, name):
        """
        Initializes the item.
        :param name: str
        """
        self.__name = name
        self.__description = ""

    def set_description(self, description):
        """
        Sets the description for the item.
        :param description: str
        :return: None
        """
        self.__description = description

    def get_name(self):
        """
        Gets the name of the item.
        :return: str
        """
        return self.__name

    def describe(self):
        """
        Describes this item.
        :return: None
        """
        print(f'The [{self.__name}] is here - {self.__description}')
