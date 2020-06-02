# ------------------------------------------------- #
# Title: Assignment07
# Description: A program that allows a shelter to manage their list of available dogs
# ChangeLog: (Who, When, What)
# AAsgekar,6.1.2020,Created Script
# AAsgekar,6.1.2020,Document pseudocode
# AAsgekar,6.1.2020,Defined functions and finalized script
# ------------------------------------------------- #
import pickle  # This imports the pickle module

# Data -------------------------------------------- #
strFileName = "AvailableDogs.dat"
listOfDogs = None
menu = "\nMenu of Available Actions:\n" \
       "1 - View dogs available for adoption\n" \
       "2 - Add a new dog into the system\n" \
       "3 - Remove a dog from the system\n" \
       "4 - Save your changes and exit the program\n"

# Processing -------------------------------------- #
def readFile(fileName):
    """Pulls data from file into a list

    :param fileName: (string) name of the binary file:
    :return: (list) of dictionary rows
    """
    try:
        objFile = open(fileName,"rb")
        outputList = pickle.load(objFile)
        objFile.close()
    except FileNotFoundError: #executes if the file does not exist
        objFile = open(fileName, "wb")
        outputList = []
        objFile.close()
    except EOFError: #executes if the file exists but is empty
        outputList = []
    return outputList

def saveFile(fileName,list):
    """Pickles data and saves it to a binary file

    :param fileName: (string) name of the binary file:
    :param list: (list) of information to be stored:
    :return: (string) of user feedback
    """
    objFile = open(fileName, "wb")
    pickle.dump(list,objFile)
    objFile.close()
    feedback = "Your data has been saved!"
    return feedback

def removeDog(list):
    """Removes a dog from the list

    :param list: (list) you want to remove data from:
    :return: feedback statement for the user
    """
    i = None #variable to determine which statement to print
    name = input("What is the name of the dog that you would like to remove? ")
    for row in list:
        if row["Name"].lower() == name.lower():
            list.remove(row)
            i = True

    if i == True:
        feedback = ("\nHopefully " + name.title() + " enjoys their new home! "\
                    +"They have been removed from the available for adoption list")
    else:
        feedback = (name.title()+" is not on the available for adoption list.")
    return feedback

def addDog():
    """Pulls data from file into a list

    :return: (list) of dictionary rows
    """
    name = input("\nWhat is the name of the dog? ")
    breed = input("What is the breed of the dog? ")
    age = input("How old is the dog? ")
    dictRow = {"Name":name.title(), "Breed":breed.title(), "Age":age.title()}
    return dictRow

# Presentation ------------------------------------ #
listOfDogs = readFile(strFileName)
while(True):
    print(menu)
    try:
        x = int(input("Which action would you like to perform? "))
    except ValueError: #message displays if the user did not select an integer
        print("Please select a number between 1 and 4.\n")
        input("Press enter to return to the menu.")
        continue

    if x == 1: #displays dogs currently available for adoption
        print("\nDogs currently available for adoption")
        print("{0} | {1} | {2}".format("Name","Breed","Age"))
        for row in listOfDogs:
            print("{0} | {1} | {2}".format(row["Name"],row["Breed"],row["Age"]))
        input("\nPress enter to return to the menu.")
    elif x == 2: #allows the user to add a new dog to the adoption list
        newEntry = addDog()
        listOfDogs.append(newEntry)
        print("\nYour additon was successful!")
        input("Press enter to return to the menu.")
    elif x == 3: #allows the user to remove a dog from the adoption list
        print(removeDog(listOfDogs))
        input("Press enter to return to the menu.")
    elif x == 4: #saves the users data and exits the program
        saveFile(strFileName,listOfDogs)
        break
    else: #displays feedback to the user if they entered a number not on the menu
        print("\nThat was not an option on the menu. Please select a number between 1 and 4")
        input("Press enter to return to the menu.")
