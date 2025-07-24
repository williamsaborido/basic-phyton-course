# Dictionatries
phonebook = {}

phonebook["William"] = "11986364674"
phonebook["Marluce"] = "11986364675"
phonebook["Melissa"] = "11986364676"

print(phonebook)

print(phonebook["Melissa"])

# initialize with values
phonebook2 = {
    "William": "11986364674",
    "Marluce": "11986364675",
    "Melissa": "11986364676",
}

#remove a value
del phonebook["William"]
phonebook.pop("Marluce")

# iterate index and values
for name, number in phonebook.items():
    print("%s number: %s" % (name, number))



