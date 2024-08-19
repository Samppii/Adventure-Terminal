'''
A classic mini-RPG (role-playing game) with hp health points, 
character moves like attack/block/heal,
and NPCs (non-player characters) that attacks based on a random number generator.

You have 100 health points and the monster has 200 health points.
Both of you can overheal and block attacks.

^
|
|
|

Story for the game:
- Your character just woke up and boom! It's a boss fight!
- The monster is a Giant with 200 health points
- You can attack the monster with a sword
- You can block the monster's attack with a shield
- You can heal yourself with a potion
- The monster can attack you with a club
- The monster can block the hero's attack with thick skin and can overheal itself by eating a meat

'''

import random

your_hp = 100
monster_hp = 200
print("**************************************************")
print("* Welcome to a lowquality Baldur's Gate ripoff!  *")
print("* You are a Swordsman fighting a monster!        *")
print("* You have 100 health points.                    *")
print("* The monster has 200 health points.             *")
print("* The monster can block your attack and overheal *")
print("* Good luck!                                     *")
print("**************************************************")

while your_hp > 0 and monster_hp > 0:

    print(f"\nYour health = {your_hp}")
    print(f"Monster's health = {monster_hp}")
    print("\nWhat would you like to do?\n 1) Attack\n 2) Block\n 3) Heal\n")
    choice = int(input("Enter your choice: "))
    monster_choice = random.randint(1, 3)
    #dmg var for normal damage
    if choice == 1:
        dmg = random.randint(10, 20)
        if monster_choice == 2:
            blck_dmg = random.randint(3, 4) #blck_dmg var for blocked damage inflicted by the user
            monster_hp -= blck_dmg
            print(f"\nYou dealt {dmg} damage, Wait a sec what? The monster blocked and only took {blck_dmg} damage!")
        else:
            monster_hp -= dmg
            print(f"\nYou just sliced the heck out of the giant and it took {dmg} damage!")

    elif choice == 2:
        if monster_choice == 1:
            block_dmg = random.randint(0, 5) #block_dmg var for blocked damage inflicted by the monster
            your_hp -= block_dmg
            print(f"\nThe monster hit you but you blocked it and only took {block_dmg} damage!")
        else:
            print("\nNothing happend the monster is looking at you tho!")
   
    elif choice == 3:
        heal = random.randint(10, 15)
        your_hp += heal
        print(f"\nYou healed yourself for {heal} health points!")

    else:
        print("\nBruh you only have 3 options. Yes this is a fourth wall break.")

    if monster_choice == 1 and choice != 2:
        dmg = random.randint(10, 20)
        your_hp -= dmg
        print(f"\nThe monster clubbd you and you took {dmg} damage!")
        
    elif monster_choice == 3:
        heal = random.randint(1, 6)
        monster_hp += heal
        print(f"\nThe monster took out a meat and starts eating it. It gained {heal} hp!")

    else:
        print("\nMoster got lost in his thoughts.")

    if your_hp <= 0:
        print("\nYou died! Game over!")
        break
    elif monster_hp <= 0:
        print("\nYou defeated the monster! You win!")
        break