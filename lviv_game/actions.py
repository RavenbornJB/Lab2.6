from time import time, sleep
from random import random
import balance


def get_function_name(func):
    """
    Gets the function name.
    :param func: function
    :return: str
    """
    return func.__name__


def eat(player, action_time):
    """
    Makes the player eat.
    :param player: PLayer
    :param action_time: int
    :return: None
    """
    sleep(action_time)
    player.energy -= balance.energy_costs["bfs"]
    if player.money < 30:
        print(f'You need {30 - player.money} more UAH.')
        return
    player.money += balance.stat_changes["bfs"][0]
    player.fitness += balance.stat_changes["bfs"][1]
    player.fitness = min(player.fitness, 100)


def study(player, action_time):
    """
    Makes the player study.
    :param player: PLayer
    :param action_time: int
    :return: None
    """
    sleep(action_time)
    player.energy -= balance.energy_costs["center"]
    player.intelligence += balance.stat_changes["center"]
    player.intelligence = min(player.intelligence, 100)


def pray(player, action_time):
    """
    Makes the player pray.
    :param player: PLayer
    :param action_time: int
    :return: None
    """
    sleep(action_time)
    player.energy -= balance.energy_costs["church"]
    player.faith += balance.stat_changes["church"]
    player.faith = min(player.faith, 100)


def get_money(player, action_time):
    """
    Makes the player gen money.
    :param player: PLayer
    :param action_time: int
    :return: None
    """
    sleep(action_time)
    player.energy -= balance.energy_costs["bank"]
    player.money += balance.stat_changes["bank"]


def activate_session(player):
    """
    Checks if the player gets through the test based on their stats.
    :param player: Player
    :return: bool
    """
    print("""The test day has come. You're presented with
30 difficult questions on the subject of quantum computing.
Answering at least 20 correctly will pass you the test.
""")
    sleep(balance.SESSION_TIME / 3)

    tasks = [False for task in range(30)]

    # The amount of tasks you solve directly comes from your intelligence.
    tasks_solved = int(player.intelligence * (3 / 10))
    for task in range(tasks_solved):
        tasks[task] = True
    print(f"""You've worked as hard as you could
and were able to answer {tasks_solved} questions.
""")

    sleep(balance.SESSION_TIME / 3)

    # But some tasks can be done with some luck!
    # It just depends on how strong your faith is.
    luck = player.faith / 100
    for task in range(tasks_solved, 30):
        if luck > random():
            tasks[task] = True
    print(f"""But sometimes you just have to believe.
By sheer luck, you got a few others. Truly a miracle!""")

    sleep(balance.SESSION_TIME / 3)

    # End of the game
    right_answers = len(list(filter(lambda x: x, tasks)))
    print(f'\nYou have correctly answered {right_answers} out of 30 questions!')
    if right_answers > balance.TO_PASS:
        print("With more than enough to pass the exam, you rejoice in happiness.")
        return True
    else:
        print("But that is not enough... You failed the test this time.")
        return False
