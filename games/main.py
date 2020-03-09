from setup import *


current_room = kitchen
inventory = []
life = 3

print("""
Welcome to my dungeon-crawler game!
--------------------
You have 3 lives.

Possible commands include:
north, south, east, west - for moving between rooms.
talk - for talking with enemies of the room.
fight - to fight an enemy.
take - to take an item.
inventory - to view your inventory
quit - to end the game.
""")

while life > 0:

    current_room.get_details()

    friend = current_room.get_friend()
    if friend is not None:
        friend.describe()

    enemy = current_room.get_enemy()
    if enemy is not None:
        enemy.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)

    elif command == "inventory":
        if inventory:
            for item in inventory:
                print(f'{item.name} --> {item.get_description()}')
        else:
            print('Your inventory is empty')

    elif command == "talk":
        # Talk to the character - check whether there is one!
        if enemy is not None:
            enemy.talk()
        if friend is not None:
            friend.talk()
            gift = friend.get_item()
            if gift is not None:
                print(f"Here, let me give you this. It's a great [{gift.get_name()}].")
                inventory.append(gift)
                print("\nYou have acquired an item!")
                friend.set_item(None)

    elif command == "fight":
        if enemy is not None:
            # Fight with the enemy, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in list(map(game.Item.get_name, inventory)):

                if fight_with == "potion":
                    inventory.remove(potion)
                    fight_result = True
                else:
                    fight_result = enemy.fight(fight_with)

                if fight_result:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.set_enemy(None)
                    if enemy.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        break
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    life -= 1
                    if life > 0:
                        print(f'{life} lives left.')
                    else:
                        print("That's the end of the game")
                        break
            else:
                print(f"You don't have a {fight_with}.")
        else:
            print("There is no one here to fight with.")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your inventory")
            inventory.append(item)
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")

    elif command == "quit":
        break

    else:
        print("Unknown command.")

    print("\n")
