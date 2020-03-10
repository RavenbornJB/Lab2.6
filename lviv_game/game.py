from time import sleep
from random import random
from lviv_game import balance


class Player:
    """Represents the player and his stats."""

    def __init__(self, name=""):
        """
        Gives the player a name and default stats.
        :param name: str
        """
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

    def activate_session(self):
        """
        Checks if the player gets through the test based on their stats.
        :param self: Player
        :return: bool
        """
        print("""The test day has come. You're presented with
    30 difficult questions on the subject of quantum computing.
    Answering at least 20 correctly will pass you the test.
    """)
        # Just some artificial time delay for suspense.
        sleep(balance.SESSION_TIME / 3)

        # All tasks
        tasks = [False for task in range(30)]

        # The amount of tasks you solve directly comes from your intelligence.
        tasks_solved = int(self.intelligence * (3 / 10))
        for task in range(tasks_solved):
            tasks[task] = True
        print(f"""You've worked as hard as you could
    and were able to answer {tasks_solved} questions.
    """)

        sleep(balance.SESSION_TIME / 3)

        # But some tasks can be done with some luck!
        # It just depends on how strong your faith is.
        luck = self.faith / 100
        for task in range(tasks_solved, 30):
            # The rest of the tasks are done based on a pseudo-random distribution.
            if luck > random():
                tasks[task] = True
        print(f"""But sometimes you just have to believe.
    By sheer luck, you got a few others. Truly a miracle!""")

        sleep(balance.SESSION_TIME / 3)

        # End of the game
        right_answers = len(list(filter(lambda x: x, tasks)))
        print(f'\nYou have correctly answered {right_answers} out of 30 questions!')
        # You win if you have more right answers than the amount specified in balance.py
        if right_answers > balance.TO_PASS:
            print("With more than enough to pass the exam, you rejoice in happiness.")
            return True
        else:
            print("But that is not enough... You failed the test this time.")
            return False


class Location:
    """Represents a location in-game."""

    def __init__(self, name="", action=None):
        """
        Initializes a location and its attributes.
        :param name: str
        :param action: function
        """
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
        """
        Does an action associated with this location.
        :param player: Player
        :param weight: int
        :return: None
        """
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
