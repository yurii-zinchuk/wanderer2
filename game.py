class Street:
    def __init__(self, sname: str, __o: object = None) -> None:
        self.name = sname
        self.next = __o
        self._description = None
        self._characters = None
        self._items = None

    @property
    def description(self) -> None:
        return self._description

    @property
    def characters(self) -> list:
        return self._characters

    @property
    def items(self) -> list:
        return self._items

    @description.setter
    def description(self, sdescription: str) -> None:
        self._description = sdescription

    @characters.setter
    def characters(self, scharacters: list) -> None:
        self._characters = scharacters

    @items.setter
    def items(self, sitems: list) -> None:
        self._items = sitems

    def print_info(self) -> None:
        print('\n')
        print(f'You are on {self.name}')
        print('-'*20)
        print(self.description)


class Character:
    def __init__(self, cname: str) -> None:
        self.name = cname
        self.conversation = None

    def print_info(self) -> None:
        print(f'{self.name} is here! He is a {str(self)}')

    def talk(self) -> None:
        print(f'[{self.name} says:] {self.conversation}')


class Enemy(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)


class Friend(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)


class Student(Friend):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'Feed me to hear how to defeat a zbui.'

    def __str__(self) -> str:
        return 'student'

    def give_hint(self, street: object) -> None:
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
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = f'Hi! My name is {self.name} and I am a kavaler.\n\
I am just chilling.'

    def __str__(self) -> str:
        return 'kavaler'


class Batyar(Friend):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'Yo! Got smth to drink? If you give me a sip, \
I will defeat a lotr for you.'

    def __str__(self) -> str:
        return 'batyar'


class Lotr(Enemy):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'Only a Batyar can defeat me.'

    def __str__(self) -> str:
        return 'lotr'


class Zbui(Enemy):
    def __init__(self, cname: str, zweakness: str) -> None:
        super().__init__(cname)
        self.conversation = 'You can only defeat me with a specific weapon.'
        self.weakness = zweakness

    def __str__(self) -> str:
        return 'zbui'


class Laydak(Enemy):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'I will steal all your belongings if you pass me.'

    def __str__(self) -> str:
        return 'laydak'


class Item:
    def __init__(self, iname: str) -> None:
        self.name = iname
        self.type = None

    def print_info(self) -> None:
        print(f'[{self.name}] is here.')


class Life(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)

    def __str__(self) -> str:
        return 'life'


class Food(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)

    def __str__(self) -> str:
        return 'food'


class Drink(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)

    def __str__(self) -> str:
        return 'drink'


class Weapon(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)

    def __str__(self) -> str:
        return 'weapon'
