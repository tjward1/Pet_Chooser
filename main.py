# Taylor Ward
# Purpose: Connect to mysql and interact with the pets database
# use object oriented programming to make a pet chooser game

from pets_class import Pet

import pymysql.cursors
from creds import *

def showData():
    # our sql statement, easy to read
    sqlSelect = """
       select pets.id as 'PetID',pets.name as 'PetName',pets.age as 'PetAge',
       types.animal_type as 'AnimalType',owners.name as 'OwnerName' 
       from pets join owners on pets.owner_id = owners.id join types on pets.animal_type_id = types.id;
      """
    # execute select
    cursor.execute(sqlSelect)

    # loop through all the results and print the data nicely
    for row in cursor:
        print(row)
    input("Press [ENTER] to continue. ")


# connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
    exit()

try:
    with myConnection.cursor() as cursor:
        # show initial data
        print("======================")
        # commenting next 2 debugging lines out to make game more user friendly
        # print(f"Initial Data")
        # showData()

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
# close connection
finally:
    myConnection.close()
    # print("Connection to database closed.\n")


# create object instance for each pet from data
pet1 = Pet(1, "Harvey", 4, "rooster", "Steve")
pet2 = Pet(2, "Boo", 2, "fox", "Donald")
pet3 = Pet(3, "Mickey", 5, "chameleon", "Elvis")
pet4 = Pet(4, "Callie", 5, "rat", "Steve")
pet5 = Pet(5, "Max", 3, "giraffe", "Elvis")
pet6 = Pet(6, "Charlie", 3, "tiger", "Rhett")
pet7 = Pet(7, "King", 5, "dingo", "Tatiana")
pet8 = Pet(8, "Tweety", 5, "frog", "Tatiana")
pet10 = Pet(10, "Bingo", 5, "deer", "Tatiana")

# put all objects into a dictionary so we can iterate through it
petList = {1: pet1,
           2: pet2,
           3: pet3,
           4: pet4,
           5: pet5,
           6: pet6,
           7: pet7,
           8: pet8,
           10: pet10}

choose = 0
while choose == 0:
    # tell the user to choose a pet using its ID number
    print("Please choose a pet from the list below using its ID number!")
    print("You can enter the letter 'q' to quit.")
    # print all pet ids and names from the dictionary
    for petKey in petList.keys():
        pets = petList[petKey]
        print(f"[{pets.getPetID()}] {pets.getPetName()}")

    try:
        # let the user specify their pet by the pet id
        petID = input("I choose pet number: ")
        # user can choose to quit playing at any time
        if petID == 'q':
            print("Bye! Thanks for playing!")
            break
        # user enters a valid pet ID
        else:
            myPet = petList[int(petID)]
            # give user all info about the pet chosen
            print(f"You have chosen {myPet.getPetName()}, the {myPet.getAnimalType()}. "
                  f"{myPet.getPetName()} is {myPet.getPetAge()} years old. "
                  f"{myPet.getPetName()}'s owner is {myPet.getOwnerName()}.\n")
            input("Press [ENTER] to continue")

    # catch exceptions so that the user can keep playing until q is entered
    except EOFError as e:
        print(f"Looks like you wanted to leave the game early! Enter q to quit.")
    except Exception as e:
        print(f"Invalid input. Please try again!\n")

