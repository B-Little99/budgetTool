basicBills = {
    "rent": 0,
    "mortgage": 0,
    "electricity": 0,
    "gas": 0,
    "council tax": 0,
    "water": 0,
    "internet": 0,
}

separator = ", "

stringKeys = separator.join(basicBills)

print("Welcome to this simple monthly budget tool! Let's start with your monthly post-tax income:")
monthlyIncome = int(input())
print("There are several basic 'bills' we want to include by default.")


loop = True

while loop == True:
    print("Please write out one of the bills you would like to update from one of the following categories: " + stringKeys + ".")
    billKey = input()
    if billKey.lower() in basicBills:
        print("Please input the cost of your " + str(billKey.lower()) + " in GBP:")    
    else: 
        print("Oops! It looks like what you entered is not on the list!")
    
    billCost = input()

    basicBills[billKey.lower()] = billCost
    print("Now your " + str(billKey.lower()) + " costs £" + str(billCost) + " per month!")

    print("Would you like to add another cost?")
    userDecision = input()
    if userDecision.lower() == "yes" or userDecision.lower() == "y":
        loop = True
    else:
        loop = False


# if breakdownDecision.lower == "yes" or breakdownDecision.lower == "y":


# Need a expenses dictionary. One can be neccessities and the other can be non-n
# Add to each dictionary using a loop asking if they would like to add another in a while loop

# Put them in separate lists and then use indexing to match them up in a loop
