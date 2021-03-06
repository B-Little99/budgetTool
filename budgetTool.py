# Different dictionaries for different types of bill categories:
householdBills = {
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

# This function is used to list all the dictionaries keys to show the user each bill dictionary and it's various bills
def stringBills(dictionary):
    separator = ", "
    stringDictionaryBills = separator.join(dictionary)
    return str(stringDictionaryBills)


# The comma function is used to provide better readability to users. 
def comma(number):
    if isinstance(number, str) == True:
        if '.' in number:
            number = float(number)
            x = '{:,}'.format(number)
            return x
        else:
            number = int(number)
            x = '{:,}'.format(number)
            return x
    else:
        x = '{:,}'.format(number)
        return x

# Function that totals the cost of the dictionary by looping through the dictionary, determining if it is an Int or Float and then adding it.
def categoryCost(billDict):
    cost = 0 
    for x in billDict:
        if isinstance(x, int) == True:
            cost += int(billDict[x])
        else:
            cost += float(billDict[x])
    return cost

# This function returns the total cost of the different categories.
def totalCost(dict1, dict2, dict3, monthlyAnnualCost):
    totalValue = categoryCost(dict1) + categoryCost(dict2) + categoryCost(dict3) + monthlyAnnualCost
    # totalValue = comma(totalValue)
    return totalValue

# This is used in the budget breakdown section and will lust the key and value in the dictionaries.
def listCategoryBills(dictionary):
    for x, y in dictionary.items():
        print(str(x.title()) + ": £" + str(comma(y)))
    print("Total: £" + str(comma(categoryCost(dictionary))))
    print("")


print("Welcome to this simple monthly budget tool! Let's start with your monthly post-tax income:")
monthlyIncome = input()
# The below if else statement enables the user to input either a float or int without error.
if isinstance(monthlyIncome, int) == True:
    monthlyIncome = int(monthlyIncome)
else:
    monthlyIncome = round(float(monthlyIncome), 2)
print("There are several basic 'bills' we want to include by default. If you do not pay anything for these bills, leave them blank.")

loop = True

# This loop is used separate from the other categories because I didn't want users to add anything to the household bills category.
while loop == True:
    print("Please write out one of the bills you would like to update from one of the following: " + stringBills(householdBills) + ".")
    billKey = input()
    if billKey.lower() in householdBills:
        print("Please input the cost of your " + str(billKey.lower()) + " in GBP:")
        billCost = input()  
    else: 
        print("Oops! It looks like what you entered is not on the list!")
        loop = False
        break

    householdBills[billKey.lower()] = billCost
    print("Now your " + str(billKey.lower()) + " costs £" + str(comma(billCost)) + " per month!")

    print("Would you like to add another cost? Yes or no.")
    userDecision = input()
    if userDecision.lower() == "yes" or userDecision.lower() == "y":
        loop = True
    else:
        loop = False

categoriesLoop = True

yearlyMonthlyStatement = " per month!"

while categoriesLoop == True:
    categoryLoop = True

    print("Please enter a category to continue: household bills, non-essential bills, travel bills, and annual bills. If you want to see a breakdown of bills, hit enter.")
    categoryDecision = input()

    # If statement to convert cateogry decision to correct text which is used in statements and enables the user to type different variations of the categories.
    if categoryDecision.lower() == "non-essential bills" or categoryDecision.lower() == "non-essential"     or categoryDecision.lower() == "non essential" or categoryDecision.lower() == "non essential bills":
        categoryDecision = nonEssentials
        categoryText = "non-essential"
    elif categoryDecision.lower() == "travel bills" or categoryDecision.lower() == "travel"                 or categoryDecision.lower() == "travel-bills" :
        categoryDecision = travelBills
        categoryText = "travel"
    elif categoryDecision.lower() == "annual bills" or categoryDecision.lower() == "annual"                 or categoryDecision.lower() == "annual-bills":
        categoryDecision = annualBills
        categoryText = "annual"
        yearlyMonthlyStatement = " per year!"
    elif categoryDecision.lower() == "household bills" or categoryDecision.lower() == "household" or categoryDecision.lower() == "household-bills":
        categoryDecision = householdBills
        categoryText = "household"
    else:
        categoryLoop = False
        categoriesLoop = False
    # The below loop will continue to provide the user to update their bills in a specific category as long as the category loop is true
    while categoryLoop == True:
        print("Please write out one of the " + str(categoryText) + " bills you would like to update: " + stringBills(categoryDecision) + " or write a new bill if it is not listed.")
        categoryKey = input()
        if categoryKey.lower() in categoryDecision:
            print("Please input the cost of your " + str(categoryKey.lower()) + " in GBP:")
            costValue = input()  
            categoryDecision[categoryKey.lower()] = costValue
            print("Now your " + str(categoryKey.lower()) + " bills are £" + str(comma(costValue)) + str(yearlyMonthlyStatement))
        else: 
            print("Oops! It looks like what you entered is not on the list! \nWould you like to add " + str(categoryKey) + " to " + str(categoryText) + " bills?")
            addUserBill = input()
            if addUserBill.lower() == "yes" or addUserBill.lower() == "y":
                print("Great, let's get that added. Please input the cost of your " + str(categoryKey.lower()) + " in GBP: ")
                costValue = input()
                categoryDecision[categoryKey.lower()] = costValue
                print("Now your " + str(categoryKey.lower()) + " bills are £" + str(comma(costValue)) + str(yearlyMonthlyStatement))
            else:
                print("Okay, not a problem.")

        print("Would you like to add another cost in " + str(categoryText) + " bills? Yes or no.")
        userDecision = input()
        if userDecision.lower() == "yes" or userDecision.lower() == "y":
            categoryLoop = True
        else:
            categoryLoop = False
            print("Please enter 'Yes' if you like to enter costs from a different category.")
            userInput = input()
            if userInput.lower() == "yes" or userInput.lower() == "y":
                categoriesLoop = True
            else:
                categoriesLoop = False

print("Would you like to see the breakdown of your expenses?")
breakdownDecision = input()

# Calculations used for the breakdown budget
yearlyCost = categoryCost(annualBills)
monthlyAnnualBillsPayment = round((yearlyCost / 12), 2)
totalCostsPCM = totalCost(householdBills, travelBills, nonEssentials, monthlyAnnualBillsPayment)
disposableMonthlyIncome = monthlyIncome - totalCostsPCM

# This prints out the breakdown for the user
if breakdownDecision.lower() == "yes" or breakdownDecision.lower() == "y":
    print("""*************************************
    MONTHLY BUDGET BREAKDOWN    
    """)
    print("Income: £" + str(comma(monthlyIncome)))
    print("""     
    -----Household bills-----
    """)
    listCategoryBills(householdBills)

    print("""     
    -----Non essential bills-----
    """)
    listCategoryBills(nonEssentials)

    print("""     
    -----Travel bills-----
    """)
    listCategoryBills(travelBills)

    print("""     
    -----Annual bills-----
    """)
    for x, y in annualBills.items():
        print(str(x.title()) + ": £" + str(comma(y)))
    print("Total yearly bills: £" + str(comma(yearlyCost)))
    print("Monthly cost: £" + str(comma(monthlyAnnualBillsPayment)))
    print("")
    print("----------------------------")
    print("Total monthly bills: £" + str(comma(totalCostsPCM)))
    print("Disposable monthly income: £" + str(comma(round(disposableMonthlyIncome, 2))))
    print("")
    print("*****************************************")
    print("")
    # This provides users with some advice based on their disposable income if they decide they want it.
    print("Would you like some advice based on your disposable income?")
    userAdviceDecision = input()
    if userAdviceDecision.lower() == "y" or userAdviceDecision == "yes":
        if str(disposableMonthlyIncome).find("-") != -1:
            print("You have a negative disposable income! This means that you are spending more than you make each month. You have to get this under control. \nPlease seek help if you are in a significant amount of debt.")
        elif disposableMonthlyIncome > 500:
            print("You have a high disposable income each month and likely have a well paying job or budget well, congratulations! \nThat is a lot of money and it is worth creating an emergency fund or hiring a financial advisor to discuss investing.")
        elif disposableMonthlyIncome > 300 and disposableMonthlyIncome <= 500:
            print("You have a decent amount of disposable income. Considering the amount of extra cash you have you should set up an emergency fund for 6 - 9 months expenses. \nIf you already have this in place then it it might be worth researching how you can invest your money.")
        elif disposableMonthlyIncome > 100 and disposableMonthlyIncome <= 300:
            print("You have disposable income. You might want to consider setting up an emergency fund for  a rainy day!")
        elif disposableMonthlyIncome >= 50 and disposableMonthlyIncome <= 100:
            print("After all your expenses you are low on cash. It is worth putting a strong budget system in place to monitor and improve your situation.")
        elif disposableMonthlyIncome >= 0 or disposableMonthlyIncome >= 0.0 and disposableMonthlyIncome < 50:
            print("You have seriously low (or no) money after your monthly expenses. You should cut back and create a strong budget. If you do not have an emergency fund then one big expense could seriously hurt you financially.")
        else:
            print("")
    else:
        print("Thanks for stopping by! I hope you found this useful!")

else:
    print("Thanks for stopping by!")
