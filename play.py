"""Module setting the game environment and
running the game process"""

import game
from pprint import pprint


# can tell you how to defeat the zbui if you feed them
student1 = game.Student('Peter')
student2 = game.Student('William')
student3 = game.Student('Robert')
# just chats with you, random person
kavaler1 = game.Kavaler('Max')
kavaler2 = game.Kavaler('Dima')
kavaler3 = game.Kavaler('Dan')
kavaler4 = game.Kavaler('Zack')
# defeats enemy for you if you give him a bottle
batyar1 = game.Batyar('Vasyl')
batyar2 = game.Batyar('Oleg')
batyar3 = game.Batyar('Myron')
# robber, is defeated only by a batyar, otherwise kills you
lotr1 = game.Lotr('Andrew')
lotr2 = game.Lotr('Anatolii')
lotr3 = game.Lotr('Ivan')
# robber, is defeated using a weapon, otherwise kills you
zbui1 = game.Zbui('Matthew', 'knife')
zbui2 = game.Zbui('Alex', 'gun')
zbui3 = game.Zbui('Tymur', 'riffle')
# homeless, is defeated using a weapon, otherwise steals all your belongings
laydak1 = game.Laydak('Igor')
laydak2 = game.Laydak('Yura')

# items that can be found on the streets lyign randomly
extralife = game.Life('extralife')
wine = game.Drink('wine')
whiskey = game.Drink('whiskey')
beer = game.Drink('beer')
hotdog = game.Food('hotdog')
pasta = game.Food('pasta')
kebab = game.Food('kebab')
gun = game.Weapon('gun')
knife = game.Weapon('knife')
riffle = game.Weapon('riffle')

# streets on the route
end = game.Street('End')
end.description = 'End of the game.'
# fifth street
krakivska = game.Street('Krakivska st.', end)
krakivska.description = 'This is your final stage. Defeat the boss to win.'
krakivska.characters = [laydak2, student1]
krakivska.items = [beer, whiskey, extralife, kebab]
# fourth street
shevchenka = game.Street('Shevchenka st.', krakivska)
shevchenka.description = 'You have almost reached the end, but the real \
challanges are ahead!'
shevchenka.characters = [student3, kavaler3, batyar3, lotr3, zbui3]
shevchenka.items = [pasta, whiskey]
# third street
franka = game.Street('Franka st.', shevchenka)
franka.description = 'This is your third street. It is too soon to relax!'
franka.characters = [kavaler2, laydak1, batyar2, lotr2]
franka.items = [wine, hotdog, riffle]
# second street
kozelnytska = game.Street('Kozelnytska st.', franka)
kozelnytska.description = 'Congrats! You have made it to the second street. \
Keep going.'
kozelnytska.characters = [student2, batyar1, lotr1, zbui2]
kozelnytska.items = [extralife, whiskey, beer, pasta, kebab]
# first street
striyska = game.Street('Striyska st.', kozelnytska)
striyska.description = 'First street on you route. Farewell and stay safe!'
striyska.characters = [student1, kavaler1, zbui1]
striyska.items = [wine, gun, knife, hotdog]


current_street = striyska
backpack = {'food': [], 'drink': [], 'weapon': [], 'life': []}
DEAD = False

while DEAD is False:
    current_street.print_info()
    print('\n')

    characters = current_street.characters
    for character in characters:
        character.print_info()
    print('\n')

    items = current_street.items
    for item in items:
        if not isinstance(item, game.Life):
            item.print_info()
    print('\n')

    print('Choose action. To view all available action, enter "actions".')
    action = input('>>> ')

    if action == 'actions':
        print("""
            Available actions:
                > talk - talk to a character on this street.
                > take - put item from this room to your backpack.
                > backpack - view contents of the backpack.
                > feed - feed a student to get a hint.
                > drink - drink with a batyar to receive his help.
                > fight - fight a character with a weapon from the backpack.
                > next - move to the next street.
                \n
            """)
        action = input('>>> ')

    if action == 'talk':
        print('Who you want to talk to? Enter character name.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    character.talk()
        else:
            print('No such character in this street. Choose the correct name.')
    elif action == 'take':
        print('Choose what to take. Enter item name.')
        name = input('>>> ')
        if name in [item.name for item in current_street.items]:
            for item in current_street.items:
                if item.name == name:
                    backpack[str(item)].append(item.name)
                    current_street.items.remove(item)
                    break
            print(f'You have put [{name}] in your backpack.')
        elif current_street.items:
            print('No such item on this street. Choose another item name.')
        else:
            print('There are no more items on this street.')
    elif action == 'backpack':
        if backpack.values():
            print(f'Your backpack contains: {backpack}')
        else:
            print('Your backpack is empty. Take something to put it there.')
    elif action == 'feed':
        print('Choose who you want to feed. Enter character name.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    # if 'student' in character.type:
                    if isinstance(character, game.Student):
                        print('Choose what you want to feed the student with. \
Enter food name.')
                        name = input('>>> ')
                        found = False
                        for food in backpack['food']:
                            if food == name:
                                found = True
                                backpack['food'].remove(food)
                                character.give_hint(current_street)
                                break
                        if not found:
                            print('No such food in your backpack. \
Choose another food or take it from the street.')
                    else:
                        print(f'You can only feed students. \
{character.name} is not a student.')
        else:
            print('No such character in this street. Choose the correct name.')

    elif action == 'drink':
        print('Choose who you want to drink with. Enter character name.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    if isinstance(character, game.Batyar):
                        print('Choose what you want to drink. \
Enter a drink name.')
                        name = input('>>> ')
                        found = False
                        for drink in backpack['drink']:
                            if drink == name:
                                found = True
                                backpack['drink'].remove(drink)
                                for char in current_street.characters:
                                    if isinstance(char, game.Lotr):
                                        current_street.characters.remove(char)
                                        print(f'Batyar {character.name} \
defeated lotr {char.name} for you.')
                                        break
                                break
                        if not found:
                            print('No such drink in your backpack. \
Choose another drink or take it from the street.')
                    else:
                        print(f'You can only drink with batyars. \
{character.name} is not a batyar.')
        else:
            print('No such character in this street. Choose the correct name.')

    elif action == 'fight':
        print('Choose who you want to figth. Enter character name.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    print('Choose what to fight with. Enter weapon name.')
                    name = input('>>> ')
                    if name in backpack['weapon']:
                        if isinstance(character, game.Zbui):
                            if character.weakness == name:
                                current_street.characters.remove(character)
                                print(f'You defeated {character.name} \
with a {name}.')
                            else:
                                print(f'You lost to {character.name}.')
                                if 'extralife' in backpack['life']:
                                    backpack['life'].remove('extralife')
                                    print('Your luck you had an extra life! \
Keep playing, but be careful.')
                                else:
                                    print('Game over!')
                                    DEAD = True
                        elif isinstance(character, game.Laydak):
                            current_street.characters.remove(character)
                            print(f'You defeated {character.name} \
with a {name}.')
                        elif isinstance(character, game.Lotr):
                            print('Only batyar can defeat a lotr.')
                            print('You lost the fight!')
                            if 'extralife' in backpack:
                                backpack['life'].remove('extralife')
                                print('Your luck you had an extra life! \
Keep playing, but be careful.')
                            else:
                                print('Game over!')
                                DEAD = True
                        else:
                            print('You can only fight with zbui or landak.')
                    else:
                        print('No such weapon in your backpack. \
Choose another weapon or take it from the street.')
                    break
        else:
            print('No such character in this street. Choose the correct name.')
    elif action == 'next':
        enemies_alive = False
        laydaks_alive = False
        for character in current_street.characters:
            if isinstance(character, game.Enemy) and not isinstance(
                    character, game.Laydak):
                print('You have to defeat all enemies before you can pass.')
                enemies_alive = True
                break
        for character in current_street.characters:
            if isinstance(character, game.Laydak):
                laydaks_alive = True
                break
        if not enemies_alive:
            if laydaks_alive:
                backpack = {'food': [], 'drink': [], 'weapon': [], 'life': []}
            current_street = current_street.next
    else:
        print(f'You cannot "{action}". Choose correct action.\n\
To see all available actions, enter "actions".')

    if current_street.next is None:
        print('Congrats, you have won the game. Good luck.')
        DEAD = True
