class Furniture:
    """Is a furniture"""

    def __init__(self, style, assign):
        """
        Gives a piece of furniture a style and an assign
        :param style: str
        :param assign: str
        """
        self.style = style
        self.assign = assign

    def __str__(self):
        """
        User string
        :return: str
        """
        return f'<furniture style is {self.style}>'

    def __eq__(self, other):
        """
        Check for equality
        :param other: Furniture
        :return: bool
        """
        if isinstance(other, Furniture):
            return self.style == other.style and self.assign == other.assign
        else:
            raise TypeError


class Chair(Furniture):
    """Is a chair"""

    def __init__(self, style, assign, tipe):
        """Gives a chair a style, an assign, and a tipe"""
        super().__init__(style, assign)
        self.tipe = tipe

    def __str__(self):
        """
        User string
        :return: str
        """
        return f'<This {self.tipe} furniture style is {self.style}>'

    def get_assign(self):
        """
        Get the assign
        :return: str
        """
        return self.assign


if __name__ == '__main__':
    furniture1 = Furniture("empire", "bedroom")
    furniture2 = Furniture("modern", "bathroom")
    assert(not (furniture1 == furniture2))
    assert(furniture1.style == "empire")
    assert(furniture1.assign == "bedroom")
    assert(str(furniture1) == "<furniture style is empire>")
    chair1 = Chair("empire", "bedroom", "armchair")
    assert(chair1.tipe == "armchair")
    assert(isinstance(chair1, Furniture))
    assert(str(chair1) == "<This armchair furniture style is empire>")
    assert(chair1.get_assign() == "bedroom")
