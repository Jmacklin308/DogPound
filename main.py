'''
Title: Dog Namer 3000
Description: Ask for the user to supply dog names (no numbers or special characters)
Reason for creating: 



'''


#create a class of what a dog is
import random
import re

#class creation 
class Dog:
    species = "k9"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Print out object info if called
    def __str__(self):
        return f"-------- \nName: {self.name} \nAge:{self.age} \nSpecies: {self.species} \nMemory Address: {hex(id(self))}\n------  "

#Start
print("--------Dog inventory tracking-----")
print("Hello! Please supply dog name(s)\n")


#function to create dog objects and store them in a list
listOfDogs = []
def createDoggos(names):
    for name in names:
        # create an newDog instance with supplied and random data
        newDog = Dog(name, random.randint(1, 13))
        #prints out the object info that i overwrote (line 25)
        print(newDog)  
        listOfDogs.append(newDog)  # add the dog to the list of dog list



#app loop
listOfDogNames = [] 
appEnd = False
while not appEnd:
    #initialize a list of dog names
    name = input("Enter a name here: ")
    #returns none if name contains numbers or characters
    noGo = re.match(r'^[a-zA-Z]+$', name)
    
    #check if name has numbers
    if noGo == None:
        print("Please don't use Numbers or special characters")
    
    elif name == "exit":
        print("\n\n\nDisplaying your doggos:\n")
        print(createDoggos(listOfDogNames))
        appEnd = True
        
    else:
        listOfDogNames.append(name) # add user input to dog name list
        print(f"{name} added! (type exit to close)")


userQuestion = input("Would you like to see the list of dog objects?")

if userQuestion == "Y":
    print(listOfDogs)




