from houses.buildings import Building


class AcademicBuilding(Building):
    """An academic building"""

    def __init__(self, address, classrooms):
        """
        Gives a building an address and some classrooms
        :param address: str
        :param classrooms: list
        """
        super().__init__(address)
        self.classrooms = classrooms

    def __str__(self):
        """User string"""
        res = self.address
        for room in self.classrooms:
            res += f'\n{room}'
        return res

    def total_equipment(self):
        """Calculates the total equipment of a building"""
        equipment = {}
        for room in self.classrooms:
            for item in room.equipment:
                equipment[item] = equipment.get(item, 0) + 1
        return list(equipment.items())
