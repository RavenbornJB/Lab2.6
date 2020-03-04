class Animal:
    """Is an animal"""

    def __init__(self, phylum, clas):
        """
        Gives an animal a phylum and a class
        :param phylum: str
        :param clas: str
        """
        self.phylum = phylum
        self.clas = clas

    def __str__(self):
        """
        User string
        :return: str
        """
        return f'<animal class is {self.clas}>'

    def __eq__(self, other):
        """
        Check for equality
        :param other: Animal
        :return: bool
        """
        return self.phylum == other.phylum and self.clas == other.clas


class Cat(Animal):

    def __init__(self, phylum, clas, genus):
        """
        Gives a cat a phylum, a class, and a genus
        :param phylum: str
        :param clas: str
        :param genus: str
        """
        super().__init__(phylum, clas)
        self.genus = genus

    def __str__(self):
        """
        User string
        :return: str
        """
        return f'<This {self.genus} animal class is {self.clas}>'

    @staticmethod
    def sound():
        """
        Makes a 'Meow' sound
        :return: str
        """
        return "Meow"


if __name__ == '__main__':
    animal1 = Animal("chordata", "mammalia")
    assert(animal1.phylum == "chordata")
    assert(animal1.clas == "mammalia")
    assert(str(animal1) == "<animal class is mammalia>")
    animal2 = Animal("chordata", "birds")
    assert(not (animal1 == animal2))
    cat1 = Cat("chordata", "mammalia", "felis")
    assert(cat1.sound() == "Meow")
    assert(cat1.genus == "felis")
    assert(isinstance(cat1, Animal))
    assert(str(cat1) == "<This felis animal class is mammalia>")