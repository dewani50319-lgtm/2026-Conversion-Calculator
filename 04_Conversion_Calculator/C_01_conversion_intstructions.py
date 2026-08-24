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


# Main routine goes here
statement_generator("Instructions", "-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions"
                              "or any key to continue")

if want_instructions == "":
        instructions()






