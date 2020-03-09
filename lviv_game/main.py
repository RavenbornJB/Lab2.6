import game, actions, balance


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

campus.link_location({"BFS Entrance": bfs,
                      "Center Door": center,
                      "Church Door": church,
                      "Kolegium Door": kolegium,
                      "Road to Bank": bank})
center.link_location({"Underground Tunnel": church})


# Player Creation
you = game.Player(name=input("Enter your name: "), lives=3)


# Starting parameters
day = 0
current_location = campus
print('Type "help" or "h" to view possible commands.\n')


# Main game loop.
while you.energy > 0 and you.fitness > 0:
    print(f'Day {day}.')

    # Scary stuff. End goal of the game.
    if day == balance.DAYS:
        result = actions.activate_session(you)
        if result:
            print("\n\n\nVICTORY :D")
        else:
            print("\n\n\nDEFEAT :(")
        break

    name = current_location.get_name()
    print(f'You are in {name}.')

    action_name = None
    if current_location.action is not None:
        action_name = actions.get_function_name(current_location.action).replace("_", " ")
        print(f'In this location you can {action_name}. (type "{action_name}" to do so)')

    print('-' * 20)

    gateways = current_location.linked_locations.keys()

    command = input("> ")

    # From here I describe different command options
    if command in gateways:
        if you.fitness < balance.MOVE_COST:
            print('You are too tired to go somewhere else. Try to get some sleep.')
        current_location = current_location.move(command)
        you.fitness -= balance.MOVE_COST

    elif command.lower() == "character" or command.lower() == "c":
        you.get_stats()

    elif command.lower() == "stats" or command.lower() == "s":
        you.explain_stats()

    elif command.lower() == "help" or command.lower() == "h":
        you.help()

    elif command.lower() == "directions" or command.lower() == "d":
        for via, location in current_location.linked_locations.items():
            print(f'You can get to {location.get_name()} via {via}')

    elif action_name is not None and command == action_name:
        print(f'You decided to {action_name}.')
        current_location.do_action(you, current_location.action_weight)

    elif command == "sleep":
        # You sleep till the morning
        day += 1

        if name == "UCU Kolegium":
            print("You slept well in your dorm. You're full of energy!")
            you.energy = 100
        elif name == "Kozelnytska Campus":
            print("""You were hardly able to fall asleep on the grass.
Besides, your muscles are now sore. Fitness decreased.""")
            you.energy += 20
            you.fitness -= 20
        else:
            print("""You've had a good rest on a couch.
Not as good as you could've had on your trusty bed though.""")
            you.energy += 50
        you.energy = min(you.energy, 100)

    elif command == "quit":
        break

    else:
        print("This command does not exist.")

    print('\n')
else:
    print("""YOU DIED""")
