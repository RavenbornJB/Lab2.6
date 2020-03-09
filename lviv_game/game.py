import balance


class Player:
    """Represents the player and his stats."""

    def __init__(self, name="", lives=3):
        """Gives the player a name and default stats."""
        self.name = name
        self.money = balance.default_stats["money"]
        self.faith = balance.default_stats["faith"]
        self.intelligence = balance.default_stats["intelligence"]
        self.fitness = balance.default_stats["fitness"]
        self.energy = balance.default_stats["energy"]

    def get_stats(self):
        """Prints out the players stats."""
        print(f"""{self.name}, a student.
    Your balance: {self.money} UAH.
Character statistics:
    Energy: {self.energy}.
    Fitness: {self.fitness}.
    Intelligence: {self.intelligence}.
    Faith: {self.faith}.""")

    @staticmethod
    def explain_stats():
        """Explains the stats."""
        print("""Money is essential for survival.
You can get it from a local bank. 
Trapezna is where you spend it.
--------------------
Energy is the resource you use to do actions.
Have none of it - and you die.
Energy is restored through sleeping.
--------------------
Fitness is your ability to do physical activities,
such as running between locations.
If you run out of fitness, you die.
Fitness can be acquired through eating.
--------------------
Intelligence directly correlates to the amount
of questions you solve on the final test.
Increase it by studying.
--------------------
Faithful people trust in God's judgement.
The more you have, the more questions you can guess.
Faith is improved by praying.""")

    @staticmethod
    def help():
        """Provides help on the command usage."""
        print('''Use "character" or "c" to see your stats.
Use "directions" or "d" to view possible roads.
Use "stats" or "s" to get an explanation of stats.
Type one of the possible roads to move to a location.
Type an action name to do an action.
Type "sleep" to sleep.
Finally, you can type "quit" at any time and quit.''')


class Location:
    """Represents a location in-game."""

    def __init__(self, name="", action=None):
        """Initializes a location and its attributes."""
        self.__name = name
        self.linked_locations = {}
        self.action = action
        self.action_weight = None

    def link_location(self, others):
        """
        Links a location to other ones.
        :param others: dict
        :return: None
        """
        for via, location in others.items():
            self.linked_locations[via] = location
            location.linked_locations[via] = self

    def move(self, via):
        """
        Returns an adjacent location through a gateway.
        :param via: str
        :return: Location
        """
        return self.linked_locations[via]

    def do_action(self, player, weight):
        """Does an action associated with this location."""
        self.action(player, weight)

    def get_name(self):
        """
        Gets the name of the location.
        :return: str
        """
        return self.__name

    def set_action_weight(self, weight):
        """
        Sets the action weight.
        :param weight: int
        :return: None
        """
        self.action_weight = weight


# These ones will probably not be needed/may be implemented in the future.
class NPC:
    """Represents a non-player interactive character."""
    pass


class Item:
    """Represents an item of any kind."""
    pass
