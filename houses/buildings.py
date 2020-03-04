class Building:
    """Is a building"""

    def __init__(self, address):
        """
        Gives a building its address
        :param building:
        :param address:
        """
        self.address = address


class House(Building):
    """Is a house"""

    def __init__(self, building, address, flats):
        """
        Gives a house its address and flats
        :param building:
        :param address:
        :param flats:
        """
        super().init(building, address)
        self.flats = flats
