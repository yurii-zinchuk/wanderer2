"""Module containing classes fof streets, characters
and items that are used in the game."""


class Street:
    """
    A class to represent a street in the game.

    ...

    Attributes
    ----------
    name : str
        name of the street
    next : object
        street object that comes next
    _description : str
        description of the street
    _characters : list
        list of characters on the street
    _items : list
        list of items on the street

    Methods
    -------
    print_info():
        Print all info about the street.
    """

    def __init__(self, sname: str, __o: object = None) -> None:
        """Define class object.

        Args:
            sname (str): Name of the street.
            __o (object, optional): Next street. Defaults to None.
        """
        self.name = sname
        self.next = __o
        self._description = None
        self._characters = None
        self._items = None

    @property
    def description(self) -> str:
        """Return description of the street.

        Returns:
            str: Description of the street.
        """
        return self._description

    @property
    def characters(self) -> list:
        """Return characters of the street.

        Returns:
            list: Characters of the street.
        """
        return self._characters

    @property
    def items(self) -> list:
        """Return items of the street.

        Returns:
            list: Items of the street.
        """
        return self._items

    @description.setter
    def description(self, sdescription: str) -> None:
        """Set description of the street.

        Args:
            sdescription (str): Description of the street.
        """
        self._description = sdescription

    @characters.setter
    def characters(self, scharacters: list) -> None:
        """Set charactes of the street.

        Args:
            scharacters (list): Characters of the street.
        """
        self._characters = scharacters

    @items.setter
    def items(self, sitems: list) -> None:
        """Set items of the street.

        Args:
            sitems (list): Items of the street.
        """
        self._items = sitems

    def print_info(self) -> None:
        """Print all info about the street to the console.
        """
        print('\n')
        print(f'You are on {self.name}')
        print('-'*20)
        print(self.description)


class Character:
    """
    A class to represent a character in the game.

    ...

    Attributes
    ----------
    name : str
        name of the character
    conversation : str
        lines that character says

    Methods
    -------
    print_info():
        Print info about the character.
    talk():
        Print conversation of the character.
    """

    def __init__(self, cname: str) -> None:
        """Define class object.

        Args:
            cname (str): Name of the character.
        """
        self.name = cname
        self.conversation = None

    def print_info(self) -> None:
        """Print info about the character.
        """
        print(f'{self.name} is here! He is a {str(self)}')

    def talk(self) -> None:
        """Print character's conversation.
        """
        print(f'[{self.name} says:] {self.conversation}')


class Enemy(Character):
    """
    A class to define an enemy in the game.
    Inherits from Character.
    """

    def __init__(self, cname: str) -> None:
        super().__init__(cname)


class Friend(Character):
    """
    A class to represent a friend in the game.
    Inherits from Character.
    """

    def __init__(self, cname: str) -> None:
        """Define class instance.

        Args:
            cname (str): Character name.
        """
        super().__init__(cname)


class Student(Friend):
    """
    A class to represent a student in the game.
    Inherits from Character.

    ...

    Attributes
    ----------
    conversation : str
        conversation of the student

    Methods
    -------
    give_hint(street):
        Print info about zbui if he is present.
    """

    def __init__(self, cname: str) -> None:
        """Define class instance.

        Args:
            cname (str): Name of the student.
        """
        super().__init__(cname)
        self.conversation = 'Feed me to hear how to defeat a zbui.'

    def __str__(self) -> str:
        """Redefine str representation of the object,
        so that it returns 'student'.

        Returns:
            str: Word 'student'.
        """
        return 'student'

    def give_hint(self, street: object) -> None:
        """Print information how to defeat a zbui.

        Args:
            street (object): Street where you currently are.
        """
        found = False
        for character in street.characters:
            if isinstance(character, Zbui):
                found = True
                zbui = character
                break
        if found:
            print(f'You can defeat {zbui.name} using {zbui.weakness}.')
        else:
            print('No zbui in this street, sorry.')


class Kavaler(Friend):
    """
    A class to represent a kavaler in the game.
    Inherints from Friend.

    ...

    Attributes
    ----------
    conversation : str
        conversation of the kavaler
    """

    def __init__(self, cname: str) -> None:
        """Define class instance.

        Args:
            cname (str): Name of the kavaler.
        """
        super().__init__(cname)
        self.conversation = f'Hi! My name is {self.name} and I am a kavaler.\n\
I am just chilling.'

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'kavaler'.

        Returns:
            str: Word 'kavaler'.
        """
        return 'kavaler'


class Batyar(Friend):
    """
    A class to represent a batyar in the game.
    Inherints from Friend.

    ...

    Attributes
    ----------
    conversation : str
        conversation of the batyar
    """

    def __init__(self, cname: str) -> None:
        """Define class instance.

        Args:
            cname (str): Name of the batyar.
        """
        super().__init__(cname)
        self.conversation = 'Yo! Got smth to drink? If you give me a sip, \
I will defeat a lotr for you.'

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'batyar'.

        Returns:
            str: Word 'batyar'.
        """
        return 'batyar'


class Lotr(Enemy):
    """
    A class to represent a lotr in the game.
    Inherits from Enemy.

    ...

    Attributes
    ----------
    conversation : str
        conversation of the lotr
    """

    def __init__(self, cname: str) -> None:
        """Define class instance.

        Args:
            cname (str): Name of the lotr.
        """
        super().__init__(cname)
        self.conversation = 'Only a Batyar can defeat me.'

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'lotr'.

        Returns:
            str: Word 'lotr'.
        """
        return 'lotr'


class Zbui(Enemy):
    """
    A class to represent a zbui in the game.
    Inherits from Enemy.

    ...

    Attributes
    ----------
    conversation : str
        conversation of the zbui
    weakness : str
        weapon to defeat the zbui
    """

    def __init__(self, cname: str, zweakness: str) -> None:
        """Define class instance.

        Args:
            cname (str): Name of the zbui.
            zweakness (str): Weapon that defeats zbui.
        """
        super().__init__(cname)
        self.conversation = 'You can only defeat me with a specific weapon.'
        self.weakness = zweakness

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'zbui'.

        Returns:
            str: Word zbui.
        """
        return 'zbui'


class Laydak(Enemy):
    """
    A class to represent a laydak in the game.
    Inherints from Enemy.

    ...

    Attributes
    ----------
    conversation : str
        conversation of the laydak
    """

    def __init__(self, cname: str) -> None:
        """Define class instance.

        Args:
            cname (str): Name of the laydak.
        """
        super().__init__(cname)
        self.conversation = 'I will steal all your belongings if you pass me.'

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'laydak'.

        Returns:
            str: Word 'laydak'.
        """
        return 'laydak'


class Item:
    """
    A class to represent an item in the game.

    ...

    Attributes
    ----------
    name : str
        name of the item

    Methods
    -------
    print_info():
        Print all info about the item.
    """

    def __init__(self, iname: str) -> None:
        """Define class instance.

        Args:
            iname (str): Name of the item.
        """
        self.name = iname
        self.type = None

    def print_info(self) -> None:
        """Print all info about the item to the console.
        """
        print(f'[{self.name}] is here.')


class Life(Item):
    """
    A class to represent an extralife in the game.
    Inherits from Item.
    """

    def __init__(self, iname: str) -> None:
        """Define class instance.

        Args:
            iname (str): Name of the extralife.
        """
        super().__init__(iname)

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it retruns word 'life'.

        Returns:
            str: Word 'life'.
        """
        return 'life'


class Food(Item):
    """
    A class to represent food.
    Inherits from Item.
    """

    def __init__(self, iname: str) -> None:
        """Define class instance.

        Args:
            iname (str): Name of the food.
        """
        super().__init__(iname)

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'food'.

        Returns:
            str: Word 'food'
        """
        return 'food'


class Drink(Item):
    """
    A class to represent a drink in the game.
    Inherits from Item.
    """

    def __init__(self, iname: str) -> None:
        """Define class instance.

        Args:
            iname (str): Name of the drink.
        """
        super().__init__(iname)

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'drink'.

        Returns:
            str: Word 'drink'.
        """
        return 'drink'


class Weapon(Item):
    """
    A class to represent a weapon in the game.
    Inherits from Item.
    """

    def __init__(self, iname: str) -> None:
        """Define class instance.

        Args:
            iname (str): Name of the weapon.
        """
        super().__init__(iname)

    def __str__(self) -> str:
        """Redefine string representation of the object,
        so that it returns word 'weapon'.

        Returns:
            str: Word 'weapon'.
        """
        return 'weapon'
