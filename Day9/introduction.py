programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# print item with key 'Bug'
# print(programming_dictionary["Bug"])


# add new item
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary["Loop"])

# edit item
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])


# print items keys
# for itemKey in programming_dictionary:
#     print(itemKey)

# print value of keys
# for itemKey in programming_dictionary:
#     print(programming_dictionary[itemKey])

for itemKey in programming_dictionary:
    print(f"{itemKey} : {programming_dictionary[itemKey]}")