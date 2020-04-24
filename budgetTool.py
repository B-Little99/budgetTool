basicBills = {
    "rent": 0,
    "mortgage": 0,
    "electricity": 0,
    "gas": 0,
    "council tax": 0,
    "water": 0,
    "internet": 0,
    "food": 0,
}

nonEssentials = {
    "gym": 0,
    "tv": 0,
    "spotify": 0,
    "netflix": 0,
    "hobbies": 0,
    "holidays": 0,
}

travelBills = {
    "petrol": 0,
    "diesel": 0,
    "car finance": 0,
    "public transport": 0,
}

annualBills = {
    "car insurance": 0,
    "car tax": 0,
    "car mot": 0,
    "breakdown cover": 0,
    "tv license": 0,
}



def stringBills(dictionary):
    separator = ", "
    stringDictionaryBills = separator.join(dictionary)
    return str(stringDictionaryBills)

print("Welcome to this simple monthly budget tool! Let's start with your monthly post-tax income:")
monthlyIncome = int(input())
print("There are several basic 'bills' we want to include by default. If you do not pay anything for these bills, leave them blank.")

loop = True

while loop == True:
    print("Please write out one of the bills you would like to update from one of the following categories: " + stringBills(basicBills) + ".")
    billKey = input()
    if billKey.lower() in basicBills:
        print("Please input the cost of your " + str(billKey.lower()) + " in GBP:")
        billCost = input()  
    else: 
        print("Oops! It looks like what you entered is not on the list!")
        loop = False
        break

    basicBills[billKey.lower()] = billCost
    print("Now your " + str(billKey.lower()) + " costs £" + str(billCost) + " per month!")

    print("Would you like to add another cost? Yes or no.")
    userDecision = input()
    if userDecision.lower() == "yes" or userDecision.lower() == "y":
        loop = True
    else:
        loop = False

def totalCost(billDict):
    cost = 0 
    for x in billDict:
        cost += int(billDict[x])
    return cost

categoriesLoop = True



print("Would you like to add expenses in other categories?")
userInput = input()
if userInput == "yes" or userInput == "y":
    categoriesLoop = True
else:
    categoriesLoop = False

while categoriesLoop == True:

    print("Please enter a category to continue: non-essential bills, travel bills, and annual bills.")
    categoryDecision = input()

# If statement to convert cateogry decision to correct input.
    if categoryDecision.lower() == "non-essential bills" or categoryDecision.lower() == "non-essential"     or categoryDecision.lower() == "non essential" or categoryDecision.lower() == "non essential bills":
        categoryDecision = nonEssentials
        categoryLoop = True
        categoryText = "non-essential"
    elif categoryDecision.lower() == "travel bills" or categoryDecision.lower() == "travel"                 or categoryDecision.lower() == "travel-bills" :
        categoryDecision = travelBills
        categoryLoop = True
        categoryText = "travel"
    elif categoryDecision.lower() == "annual bills" or categoryDecision.lower() == "annual"                 or categoryDecision.lower() == "annual-bills":
        categoryDecision = annualBills
        categoryLoop = True
        categoryText = "annual"
    else:
        categoryLoop = False

# May need another loop here for individual cats
    # if categoryDecision != "":
    while categoryLoop == True:
        print("Please write out one of the " + str(categoryText) + " bills you would like to update: " + stringBills(categoryDecision) + ".")
        categoryKey = input()
        if categoryKey.lower() in categoryDecision:
            print("Please input the cost of your " + str(categoryKey.lower()) + " in GBP:")
            costValue = input()  
        else: 
            print("Oops! It looks like what you entered is not on the list!")
            categoryLoop = False
            break

        categoryDecision[categoryKey.lower()] = costValue
        print("Now your " + str(categoryKey.lower()) + " bills are £" + str(costValue) + " per month!")

        print("Would you like to add another cost in " + str(categoryText) + " bills with categories of: " + stringBills(categoryDecision) + "? Yes or no.")
        userDecision = input()
        if userDecision.lower() == "yes" or userDecision.lower() == "y":
            categoryLoop = True
        else:
            categoryLoop = False
            print("Please enter 'Yes' if you like to enter costs from a different category? (These are: non-essential bills, travel bills and annual bills)")
            userInput = input()
            if userInput.lower() == "yes" or userInput.lower() == "y":
                categoriesLoop = True
            else:
                categoriesLoop = False

# Need to have a loop for each of the categories so that they can keep inputting costs if they please.
# Need to input the cateogry into the function to then take it to the correct one.


def printTotal(dictionary):
    for x, y in dictionary.items():
        print(str(x.title()) + ": £" + str(y))
    print("Total household bills: £" + str(totalCost(dictionary)))
    print("""
    """)


print("Would you like to see the breakdown of your expenses?")
breakdownDecision = input()

if breakdownDecision.lower() == "yes" or breakdownDecision.lower() == "y":
    print("""*************************************
    MONTHLY BUDGET BREAKDOWN    

    """)
    print("Income: £" + str(monthlyIncome))
    print("""     
    
    -----Household bills-----
    """)
    printTotal(basicBills)

    print("""     
    
    -----Non essential bills-----
    """)
    printTotal(nonEssentials)

    print("""     

    -----Travel bills-----
    """)
    printTotal(travelBills)


    print("Total monthly costs: £" + str(totalCost(basicBills)))
    print("Disposable monthly income: £" + str(monthlyIncome - totalCost(basicBills)))
    print("")
    print("*****************************************")

else:
    print("Thanks for stopping by!")



# Need a expenses dictionary. One can be neccessities and the other can be non-n
# Add to each dictionary using a loop asking if they would like to add another in a while loop

# Put them in separate lists and then use indexing to match them up in a loop
