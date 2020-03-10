from lviv_game import game, actions, balance


# Room Creation, preparing the game environment
bank = game.Location(name="UCU Bank", action=actions.get_money)
bank.set_action_weight(balance.weights["bank"])
campus = game.Location(name="Kozelnytska Campus")
bfs = game.Location(name="Trapezna Building", action=actions.eat)
bfs.set_action_weight(balance.weights["bfs"])
church = game.Location(name="The Church", action=actions.pray)
church.set_action_weight(balance.weights["church"])
center = game.Location(name="Sheptytsky Center", action=actions.study)
center.set_action_weight(balance.weights["center"])
kolegium = game.Location(name="UCU Kolegium")

# Linking the rooms
campus.link_location({"BFS Entrance": bfs,
                      "Center Door": center,
                      "Church Door": church,
                      "Kolegium Door": kolegium,
                      "Road to Bank": bank})
center.link_location({"Underground Tunnel": church})


# Player Creation
you = game.Player(name=input("Enter your name: "))


# Starting parameters
day = 0
current_location = campus
print(f'''
Welcome to my dungeon-crawler RPG!!!
It is based in the setting of the Kozelnytska UCU campus.
--------------------
You are a student studying computer science, and you are determined to become the best.
But it's not that easy. Quantum computing is your weakness, and just in {balance.DAYS} days
you are having the final exam on it. Can you do what it takes to pass the exam?
--------------------
Type "help" or "h" to view possible commands.
''')


# Main game loop. Continues while you are alive.
while you.energy > 0 and you.fitness > 0:
    print(f'Day {day}.')

    # Scary stuff. End goal of the game. Triggers when the
    if day == balance.DAYS:
        result = you.activate_session()
        if result:
            print("\n\n\nVICTORY :D")
        else:
            print("\n\n\nDEFEAT :(")
        break

    # Where are you right now?
    name = current_location.get_name()
    print(f'You are in {name}.')

    # Does this location have an associated action?
    action_name = None
    if current_location.action is not None:
        action_name = actions.get_function_name(current_location.action).replace("_", " ")
        print(f'In this location you can {action_name}. (type "{action_name}" to do so)')

    print('-' * 20)

    # Where can you go from here?
    gateways = current_location.linked_locations.keys()

    # Input a command.
    command = input("> ")

    # From here I describe different command options
    if command.lower() == "character" or command.lower() == "c":
        # View your character stats.
        you.get_stats()

    elif command.lower() == "stats" or command.lower() == "s":
        # Explain the meaning of the stats.
        you.explain_stats()

    elif command.lower() == "help" or command.lower() == "h":
        # List of possible commands.
        you.help()

    elif command.lower() == "directions" or command.lower() == "d":
        # View all directions you can go from here.
        for via, location in current_location.linked_locations.items():
            print(f'You can get to {location.get_name()} via {via}')

    elif command in gateways:
        # Can go anywhere if you're out of fitness.
        if you.fitness < balance.MOVE_COST:
            print('You are too tired to go somewhere else. Try to get some sleep.')
        # Else, move there.
        current_location = current_location.move(command)
        you.fitness -= balance.MOVE_COST

    elif action_name is not None and command == action_name:
        # If there's an action, do it.
        print(f'You decided to {action_name}.')
        current_location.do_action(you, current_location.action_weight)

    elif command == "sleep":
        # You sleep till the morning.
        day += 1

        if name == "UCU Kolegium":
            # Sleep is best in Kolegium, although that is not told to the player by default.
            print("You slept well in your dorm. You're full of energy!")
            you.energy = 100
        elif name == "Kozelnytska Campus":
            # On the contrary, sleeping on the street is really bad for you.
            print("""You were hardly able to fall asleep on the grass.
Besides, your muscles are now sore. Fitness decreased.""")
            you.energy += 20
            you.fitness -= 20
        else:
            # Anywhere else is fine, but not great.
            print("""You've had a good rest on a couch.
Not as good as you could've had on your trusty bed though.""")
            you.energy += 50
        you.energy = min(you.energy, 100)

    elif command == "quit":
        # Quit the game.
        break

    else:
        # What did you even type?
        print("This command does not exist.")

    print('\n')

else:
    # If you exit out of the loop normally, it means your energy or fitness dropped to 0. You die.
    print("""YOU DIED""")
