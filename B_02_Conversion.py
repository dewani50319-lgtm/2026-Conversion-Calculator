# Generates headings (eg: ----- Heading -----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
    To use this program simply enter a form of measurement. 
    The program will convert your measurement.

    To exit the program, please type 'xxx'.

        ''')

distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

mass_dict = {
    "mg": 100000,
    "g": 100,
    "kg": 0.1,
}

time_dict = {
    "seconds": 3600,
    "minutes": 60,
    "hours": 1,
}


def dict_checker():
    """ Checks valid domain has been chosen and returns dictionary to be used """

    error = "Please choose from distance / time / mass."
    valid_dicts = ["distance", "time", "mass", "xxx"]

    while True:
        response = input("What domain are you using (distance / time / mass)?").strip().lower()
        print()

        for item in valid_dicts:
            if response == item or response == item[0]:
                return item

        print(error)


# Define domains
valid_type = ["mass", "distance", "time"]


# Main routine goes here
statement_generator("Instructions", "-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                              "or any key to continue")

if want_instructions == "":
        instructions()


while True:
    calc_type = dict_checker()
    if calc_type == "xxx":
        print("Thank you for using the conversion calculator!!!^-^")
        break
    elif calc_type == "mass":
        use_dictionary = mass_dict
    elif calc_type == "distance":
        use_dictionary = distance_dict
    else:
        use_dictionary = time_dict


    amount = float(input("how much? "))
    from_unit = input("From Unit? ")
    to_unit = input("To Unit? ")

    # Multiply to get to our standard value...
    multiply_by = distance_dict[to_unit]
    standard = amount * multiply_by

    # Divide to get to our desired value
    divide_by = distance_dict[from_unit]
    answer = standard / divide_by

    print(f"There are {answer} {to_unit} in {amount} {from_unit} ")



