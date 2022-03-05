class Street:
    def __init__(self, sname: str, __o: object = None) -> None:
        self.name = sname
        self.next = __o
        self.description = None
        self.characters = None
        self.items = None

    def set_description(self, sdescr: str) -> None:
        self.description = sdescr

    def add_characters(self, scharacters: list) -> None:
        self.characters = scharacters

    def add_items(self, sitems: list) -> None:
        self.items = sitems

    def get_info(self) -> None:
        print(self.name)
        print('----------------')
        print(self.description)

    def get_characters(self) -> list:
        return self.characters

    def get_items(self) -> list:
        return self.items


class Character:
    def __init__(self, cname: str) -> None:
        self.name = cname
        self.conversation = None
        self.type = None

    def get_info(self) -> None:
        print(f'{self.name} is here! He is a {self.type}')

    def talk(self) -> None:
        print(f'[{self.name} says:] {self.conversation}')


class Student(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'Feed me to hear how to defeat a Zbui.'
        self.type = 'friend student'

    def give_hint(self, street: object) -> None:
        found = False
        for character in street.characters:
            if isinstance(character, Zbui):
                found = True
                char = character
                break
        if found:
            print(f'You can defeat {char.name} using {char.weakness}.')
        else:
            print('No Zbui here, sorry.')


class Kavaler(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = f'Hi! My name is {self.name}, I am just chillin.'
        self.type = 'friend kavaler'


class Batyar(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'Yo! Got smth to drink? I can defeat a Lotr!'
        self.type = 'friend batyar'


class Lotr(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'Only a Batyar can defeat me!'
        self.type = 'enemy lotr'


class Zbui(Character):
    def __init__(self, cname: str, zweakness: str) -> None:
        super().__init__(cname)
        self.conversation = 'You have to defeat me before you can keep going.'
        self.weakness = zweakness
        self.type = 'enemy zbui'

    def fight(self, weapon: str) -> bool:
        return self.weakness == weapon


class Laydak(Character):
    def __init__(self, cname: str) -> None:
        super().__init__(cname)
        self.conversation = 'I will steal all your stuff if you pass me!'
        self.type = 'enemy laydak'


class Item:
    def __init__(self, iname: str) -> None:
        self.name = iname
        self.type = None

    def get_info(self) -> None:
        print(f'{self.type} {self.name} is here.')


class Life(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)
        self.type = 'extralife'


class Support(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)
        self.type = 'support'


class Weapon(Item):
    def __init__(self, iname: str) -> None:
        super().__init__(iname)
        self.type = 'weapon'
