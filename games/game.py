class Room:
    """Represents a room in a house. Can contain things."""

    def __init__(self, room):
        """
        Initializes a room.
        :param room: str
        """
        self.__room = room
        self.__description = ""
        self.__friend = None
        self.__enemy = None
        self.__item = None
        self.__linked_rooms = {"north": None,
                               "south": None,
                               "west": None,
                               "east": None}

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
        Gets a room name.
        :return: str
        """
        return self.__room

    def set_description(self, description):
        """
        Sets a room description.
        :param description: str
        :return: None
        """
        self.__description = description

    def set_friend(self, friend):
        """
        Sets the friend in the room.
        :param friend: Friend
        :return: None
        """
        self.__friend = friend

    def get_friend(self):
        """
        Gets the friend in the room.
        :return: Friend
        """
        return self.__friend

    def set_enemy(self, enemy):
        """
        Sets the enemy in the room.
        :param enemy: Enemy
        :return: None
        """
        self.__enemy = enemy

    def get_enemy(self):
        """
        Gets the enemy in the room.
        :return: Enemy
        """
        return self.__enemy

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
        new_room = self.__linked_rooms[direction]
        return new_room if new_room is not None else self

    def get_details(self):
        """
        Prints out the details about this room.
        :return: None
        """
        print(f'''{self.__room}
--------------------
{self.__description}
''')
        for direction, room in self.__linked_rooms.items():
            if room is not None:
                print(f'The {room.get_name()} is {direction}')


class Character:

    def __init__(self, name, description=""):
        """
        Initializes a non-player character.
        :param name: str
        :param description: str
        """
        self.name = name
        self.__description = description
        self.__conversation = ""

    def set_conversation(self, conversation):
        """
        Sets the conversation for the character.
        :param conversation: str
        :return: None
        """
        self.__conversation = conversation

    def describe(self):
        """
        Describes this character.
        :return: None
        """
        print(f'\n{self.name} is here!\n{self.__description}\n')

    def talk(self):
        """
        Makes this character talk to you.
        :return: None
        """
        print(f'[{self.name} says]: {self.__conversation}')


class Friend(Character):

    def __init__(self, name, description=""):
        super().__init__(name, description)
        self.__gift = None

    def set_item(self, gift):
        """
        Sets the gift for the friend.
        :param gift: Item
        :return: None
        """
        self.__gift = gift

    def get_item(self):
        """
        Gets the gift for the friend.
        :return: Item
        """
        return self.__gift


class Enemy(Character):
    """Represents a living enemy that inhabits the rooms."""

    __defeated_enemies = 0

    def __init__(self, name, description=""):
        """
        Initializes an enemy.
        :param name: str
        :param description: str
        """
        super().__init__(name, description)
        self.__weakness = None

    def set_weakness(self, weakness):
        """
        Sets the weakness for the character.
        :param weakness: str
        :return: None
        """
        self.__weakness = weakness

    def fight(self, weapon):
        """
        Determines the result of a fight with this enemy.
        The chosen weapon must equal the weakness.
        :param weapon: str
        :return: bool
        """
        if weapon == self.__weakness:
            print(f'You fend {self.name} off with the {weapon}')
            Enemy.__defeated_enemies += 1
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer!')
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
        self.name = name
        self.__description = ""

    def get_name(self):
        """
        Gets the name of the item.
        :return: str
        """
        return self.name

    def set_description(self, description):
        """
        Sets the description for the item.
        :param description: str
        :return: None
        """
        self.__description = description

    def get_description(self):
        """
        Gets the description for the item.
        :return: str
        """
        return self.__description

    def describe(self):
        """
        Describes this item.
        :return: None
        """
        print(f'The [{self.name}] is here - {self.__description}')
