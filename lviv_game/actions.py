from time import sleep
from lviv_game import balance


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
