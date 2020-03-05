from games import game


def create_room(name="Room", description=""):
    room = game.Room(name)
    room.set_description(description)
    return room


def create_enemy(name="John", description="", conversation="", weakness="", room=None):
    """
    Creates an Enemy object in a given room.
    :param name: str
    :param description: str
    :param room: Room
    :param conversation: str
    :param weakness: str
    :return: None
    """
    enemy = game.Enemy(name, description)
    enemy.set_conversation(conversation)
    enemy.set_weakness(weakness)
    room.set_enemy(enemy)
    return enemy


def create_friend(name="John", description="", conversation="", room=None, gift=None):
    """
    Creates an Enemy object in a given room.
    :param name: str
    :param description: str
    :param room: Room
    :param conversation: str
    :param gift: Item
    :return: None
    """
    friend = game.Friend(name, description)
    friend.set_conversation(conversation)
    friend.set_item(gift)
    room.set_friend(friend)
    return friend


def create_item(name="thing", description="", where=None):
    item = game.Item(name)
    item.set_description(description)
    if where:
        where.set_item(item)
    return item


kitchen = create_room(name="Kitchen",
                      description="A dank and dirty room buzzing with flies.")

dining_hall = create_room(name="Dining Hall",
                          description="A large room with ornate golden decorations on each wall.")

ballroom = create_room(name="Ballroom",
                       description="A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

cheese = create_item(name="cheese",
                     description="A large and smelly block of cheese.",
                     where=ballroom)
# cheese = game.Item("cheese")
# cheese.set_description("A large and smelly block of cheese")
# ballroom.set_item(cheese)
book = create_item(name="book",
                   description="A really good book entitled 'Knitting for dummies'.",
                   where=dining_hall)
# book = game.Item("book")
# book.set_description("A really good book entitled 'Knitting for dummies'.")
# dining_hall.set_item(book)
potion = create_item(name="potion",
                     description="A bubbling red potion. It smells funny.",
                     where=None)
# potion = game.Item("potion")
# potion.set_description("A bubbling red potion. It smells funny.")
# xanathar.set_item(potion)

xanathar = create_friend(name="Xanathar",
                         description="An old sage with a creepy smile.",
                         conversation="Good to see you, buddy! Sit with me by the fire.",
                         room=kitchen,
                         gift=potion)
dave = create_enemy(name="Dave",
                    description="A smelly zombie.",
                    conversation="What's up, dude! I'm hungry.",
                    weakness="cheese",
                    room=dining_hall)
tabitha = create_enemy(name="Tabitha",
                       description="An enormous spider with countless eyes and furry legs.",
                       conversation="Sssss....I'm so bored...",
                       weakness="book",
                       room=ballroom)
