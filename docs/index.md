# Introduction
In this week’s assignment, the challenge was to create a Python script that incorporated the concepts of pickling and exceptions. In this document I’ll review how I utilized both pickling and exceptions, as well as discuss the purposes of those concepts and the benefits they can provide. The script I wrote functions as a list of dogs available for adoption in a shelter where the user can view, add and remove from the list.

# Writing the Script
I started by writing out pseudocode to get an idea of the structure for the code (Figure 1).
![](https://raw.githubusercontent.com/aasgekar/IntroToProg-Python-Mod07/master/docs/images/pseudocode.JPG)
**Figure 1: Pseudocode**

From here I determined what functions I should create to make the code more organized. I decided to define four different functions—read the current file, save changes to the file, remove a dog from the list and add a dog to the list.

The first function, which read the file is also the first location where I used exceptions and pickling. Since I was only reading the file, I knew that there could be an error if the file didn’t exist so that was my first except clause. I encountered another error while testing my code so I added that as my second except clause. The code can be seen below where it tried to save the contents of the file to a list and if it doesn’t exist, the file and/or list are created (see below).


```python
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
```

I then went on to create the other three functions which were pretty similar to actions we’ve performed in past assignments. I created a lot of local variables within the functions the keep it as simple as possible by minimizing inputs and not using global variables. The code for the functions can be seen below.

```python
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
```

Moving to the main body of the code, I wrote an if statement, very similar to ones for past assignments. I did however, add an exception at the beginning in case the user did not input an integer.

```python
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
```

Lastly, I tested the code in both PyCharm and the Console. I did not check the file where the data was being stored since I knew it wouldn’t be legible to human eyes so instead, I checked that the correct information was saved to the file by running the program again. While I tested all functions in both PyCharm and the Console, Figure two shows a test of adding a dog and printing the current list.

![](https://github.com/aasgekar/IntroToProg-Python-Mod07/blob/master/docs/images/pycharmtest.JPG?raw=true)
**Figure 2: PyCharm Test**

Figure three shows an example of testing the functionality of removing a dog and viewing the updated list in the console.

![](https://github.com/aasgekar/IntroToProg-Python-Mod07/blob/master/docs/images/consoletest.JPG?raw=true)
**Figure 3: PyCharm Test**

# Summary
In this assignment, I tried to use concepts that we have learned in past assignments and incorporate pickling and exceptions. These allowed the code to be much simpler than it has in the past in how things are read and written. It also eliminated the risk of the program ending abruptly due to an error from a missing file or a user input.
