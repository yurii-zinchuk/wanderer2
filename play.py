import game


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
wine = game.Support('wine')
whiskey = game.Support('whiskey')
beer = game.Support('beer')
hotdog = game.Support('hotdog')
pasta = game.Support('pasta')
kebab = game.Support('kebab')
gun = game.Weapon('gun')
knife = game.Weapon('knife')
riffle = game.Weapon('riffle')


# streets on the route
end = game.Street('End')

krakivska = game.Street('Krakivska st.', end)
krakivska.set_description('This is your final stage. Defeat the boss to win.')
krakivska.add_characters([laydak2, student1])
krakivska.add_items([beer, whiskey, extralife, kebab])

shevchenka = game.Street('Shevchenka st.', krakivska)
shevchenka.set_description('You have almost reached the end, but the real \
challanges are ahead!')
shevchenka.add_characters([student3, kavaler3, batyar3, lotr3, zbui3])
shevchenka.add_items([pasta, whiskey])

franka = game.Street('Franka st.', shevchenka)
franka.set_description('This is your third street. It is too soon to relax!')
franka.add_characters([kavaler2, laydak1, batyar2, lotr2])
franka.add_items([wine, hotdog, riffle])

kozelnytska = game.Street('Kozelnytska st.', franka)
kozelnytska.set_description('Congrats! You have made it to the second street. \
Keep going.')
kozelnytska.add_characters([student2, batyar1, lotr1, zbui2])
kozelnytska.add_items([extralife, whiskey, beer, pasta, kebab])

striyska = game.Street('Striyska st.', kozelnytska)
striyska.set_description('First street on you route. Farewell and stay safe!')
striyska.add_characters([student1, kavaler1, zbui1])
striyska.add_items([wine, gun, knife, hotdog])


current_street = striyska
backpack = []
DEAD = False

while DEAD is False:
    print('\n')
    current_street.get_info()

    print('\n')
    characters = current_street.get_characters()
    for character in characters:
        character.get_info()

    print('\n')
    items = current_street.get_items()
    for item in items:
        if not isinstance(item, game.Life):
            item.get_info()

    print('\n')
    print('Choose action')
    action = input('>>> ')

    if action == 'next':
        enemies_alive = False
        laydak_alive = False

        for character in current_street.get_characters():
            if 'enemy' in character.type and 'laydak' not in character.type:
                print('You have to defeat all enemies to pass!')
                enemies_alive = True
                break
        for character in current_street.get_characters():
            if 'laydak' in character.type:
                laydak_alive = True
                break

        if not enemies_alive:
            if laydak_alive:
                backpack = []
            current_street = current_street.next
    elif action == 'talk':
        print('Who you want to talk to? Enter name.')
        name = input('>>> ')

        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    character.talk()
        else:
            print('No such character here.')
    elif action == 'feed':
        print('Choose who you want to feed.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    if 'student' in character.type:
                        print('Choose what you want to feed him with.')
                        food = input('>>> ')
                        found = False
                        for item in backpack:
                            if item == food and food in ['hotdog', 'pasta', 'kebab']:
                                found = True
                                backpack.remove(item)
                                character.give_hint(current_street)
                                break
                        if not found:
                            print('No such food in backpack.')
                    else:
                        print('You can only feed students.')
        else:
            print('No such character in this street.')
    elif action == 'drink':
        print('Choose who you want to drink with.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    if 'batyar' in character.type:
                        print('Choose what you want to drink wiht him.')
                        drink = input('>>> ')
                        found = False
                        for item in backpack:
                            if item in ['wine', 'beer', 'whiskey'] and item == drink:
                                found = True
                                backpack.remove(item)
                                for one in current_street.characters:
                                    if 'lotr' in one.type:
                                        current_street.characters.remove(one)
                                        print(f'Lotr {one.name} is defeated.')
                                        break
                                break
                        if not found:
                            print('No such drink in backpack.')
                    else:
                        print('You can only drink with batyars.')
        else:
            print('No such character in this street.')
    elif action == 'fight':
        print('Choose who you want to figth.')
        name = input('>>> ')
        if name in [character.name for character in current_street.characters]:
            for character in current_street.characters:
                if character.name == name:
                    print('Now, choose your weapon.')
                    weapon = input('>>> ')
                    if weapon in backpack:
                        if 'zbui' in character.type:
                            if character.fight(weapon):
                                current_street.characters.remove(character)
                                print(f'You defeated {character.name} with a {weapon}')
                            else:
                                print('You lost the fight.')
                                if 'extralife' in backpack:
                                    backpack.remove('extralife')
                                    print('Your luck you had an extra life!')
                                else:
                                    print('You lost.')
                                    DEAD = True
                        elif 'laydak' in character.type:
                            if weapon in ['knife', 'gun', 'riffle']:
                                current_street.characters.remove(character)
                                print(f'You defeated {character.name} with a {weapon}')
                            else:
                                backpack = []
                                print('You lost the fight.')
                                print('Laydak stole everything from backpack.')
                        elif 'lotr' in character.name:
                            print('Only batyar could defeat a lotr.')
                            print('You lost the fight!')
                            if 'extralife' in backpack:
                                backpack.remove('extralife')
                                print('Your luck you had an extra life!')
                            else:
                                print('You lost.')
                                DEAD = True
                        else:
                            print('You can only fight Zbui or Landak.')
                    else:
                        print('No such weapon in your backpack.')
                    break
        else:
            print('No such character here!')
    elif action == 'take':
        print('Choose what to take.')
        item_name = input('>>> ')
        if item_name in [item.name for item in current_street.items]:
            backpack.append(item_name)
            for item in current_street.items:
                if item.name == item_name:
                    current_street.items.remove(item)
                    break
            print(f'You have put {item_name} inside the backpack.')
    else:
        print(f'You cannot "{action}"!')

    if current_street.next is None:
        print('Congrats, you have won the game.')
        DEAD = True
