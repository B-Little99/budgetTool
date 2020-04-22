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
print("There are several basic 'bills' we want to include by default. These are: " + stringKeys + ".")


# Need a expenses dictionary. One can be neccessities and the other can be non-n
# Add to each dictionary using a loop asking if they would like to add another in a while loop


