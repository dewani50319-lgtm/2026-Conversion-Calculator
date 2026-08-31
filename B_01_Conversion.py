# Decorates statements
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Please enter the amount. Followed by the units you currently 
 have and the units you need to convert to.

The program will automatically calculate your amount in the new unit.  

    ''')


# checks user has entered a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero"

    while True:

        # Ask user for number / exit code
        response = input(question).lower()
        if response == "xxx":
            return "xxx"

        try:

            # ask user to enter a number
            response = float(response)

            # checks number is more than 0
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# converts valid units to correct abbreviation
def units_abbreviations(question):
    # list of most possible units
    possible_units = [
        ["mm", "millimeters", "millimetres", "millimeter", "millimetre"],
        ["cm", "centimeters", "centimeter", "cms", "centimetres", "centimetre"],
        ["m", "meters", "metres", "meter", "metre"],
        ["km", "kilometers", "kilometres", "kilometer", "kilometre"],
        ["ms", "milliseconds", "millisecond"],
        ["s", "seconds", "secs", "second", "sec"],
        ["min", "mins", "minutes", "minute"],
        ["h", "hr", "hrs", "hour", "hours"],
        ["d", "days", "day"],
        ["y", "years", "year"]
        ["kilogrammes", "kilograms", "kgs", "kg", "kilogramme", "kilograms", "kilo", "kilos"]
        ["milligramme", "mg", "milligram", "milligrammes", "milligrams"]
        ["gram", "grams", "gramme", "grammes", "g", "gs", "gm"]
        ["tonne", "tonnes", "ton", "tons", "t"]

    ]

    while True:
        response = input(question)

        for item in possible_units:
            if response in item:
                return item[0]

        else:
            print("That unit is invalid / not supported by this program")


# checks user has entered valid units (ie: can't choose cm and hrs)
def unit_checker(possible_lists):
    # possible units lists...

    invalid_holder = []
    to_unit = ""

    while True:
        from_unit = units_abbreviations("Enter the unit you have: ")

        for item in possible_lists:

            if from_unit in item:
                to_unit = units_abbreviations("Enter the unit you want to convert into: ")

                if to_unit in item:
                    return [from_unit, to_unit]

            else:
                invalid_holder.append(item)

        if len(invalid_holder) <= len(possible_lists):
            print("Please enter a valid unit to convert from")
        else:
            print(f"Try again, it is not possible to convert between {to_unit} and {from_unit}")


# if float ends in .0, changes it to an integer
def display_int(var_int):
    if var_int % 1 == 0:
        return int(var_int)

    # checks if number has more than six digits after the decimal point.
    elif var_int % 1 != 0 and len(str(var_int).split('.')[1]) > 6:
        return f"{var_int:.2f}"

    else:
        return var_int


# Main Routine goes here

# *** Units Dictionaries ****
distance = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": 0.001
}

time = {
    "ms": 3600 * 1000,
    "s": 3600,
    "min": 60,
    "h": 1,
    "d": 1/24,
    "y": 1 / (24 * 365 + 6 + 9/60)    # accounts for the leap years
}

mass = {
    "mg": 1000,
    "g": 1,
    "kg": 0.001,
    "t": 0.000001
}


# combines all the dictionaries so that we can look up conversion factors in one place
combined_units = distance | time

# List of dictionaries for use in unit checker
all_dicts = [distance, time]

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()


while True:

    # ask user to enter amount
    amount = num_check("\nEnter the amount you want to convert (or 'xxx' to quit): ")

    # Check for exit code
    if amount == "xxx":
        break

    # ask user for units (what they have and what they want)
    # function checks that units are valid
    get_units = unit_checker(all_dicts)
    convert_from = get_units[0]
    convert_to = get_units[1]

    # Do conversion
    to_standard = amount * combined_units[convert_to]
    converted = to_standard / combined_units[convert_from]

    # display whole number results as an integer
    amount = display_int(amount)
    converted = display_int(converted)

    # Output result

    print()
    print(f"{amount} {convert_from} is {converted} {convert_to}\n")


print("\nThank you for using The Conversion Calculator :)")