#################### Int Validator ####################
def intValidator(inputMessage):
    # while the input is wrong
    while True:
        # ask the user for an input 
        try:
            x = int(input(inputMessage))
            return x
            # if no value error occurs then break the while loop
            break
        # if there is a value error print error then loop back up to the top
        except ValueError:
            print("Value entered is not an integar")
            

#################### Survival Rate Validator ####################
def survivalRateValidator(inputMessage):
     # while the input is wrong
     while True:
        # ask the user for an input
        try:
            x = float(input(inputMessage))
            # if value is between 0 and 1 then return the value
            if(x <= 1 and x >= 0):
                return x
                # if no value error occurs and the input meets the condition then break the while loop
                break
            else:
                # if value is not in tange then print the error
                print("Value is not between 1 and 0")
                continue
        except ValueError:
            print("Value entered is not a float")


#################### Generation Validator ####################
def generationValidator(inputMessage):
    # while the input is wrong
    while True:
        # ask the user for an input
        try:
            # ask user for an input
            x = int(input(inputMessage))

            # if the value is between 5 and 25
            if(x <= 25 and x >= 5):
                # return value x to the main code
                return x

                # input is correct break the loop
                break
            else: # else value is not between 5 and 25
                print("Value is not between 5 and 25")
                continue
        # if there is a value error print error then loop back up to the top
        except ValueError:
            print("Value entered is not a integar")


#################### Filename Validator ####################
def filenameValidator(inputMessage):

    # valid input == false
    valid = False

    # while the input is invalid
    while valid == False:

        # ask user for an input
        x = input(inputMessage)

        # split the input up into individual words
        temp = tuple(x)

        # list of invalid characters
        invalidCharacters = ['.' , ',' , '/' , '\\', '`' , ';' , '[' ,  ']' , '-', '_', '*', '&', '^',
'%', '$', '#', '@', '!', '~', '+', '(', ')', '|', '{', '}', '<', '>', '?', ':', '"', '=']

        # for i in the letters in the input
        for i in temp:
            # if the character is equal to one of the invalid characters
            if(i in invalidCharacters):
                # the input is not valid
                valid = False

                # print error to the user
                print("Invalid Filename...")
                # break the loop and ask user for another file name
                break

            # else the filename is valid
            else:
                valid = True

                # return the value x to the main code
                return x


#################### Option Validator ####################
def optionValidator(inputMessage):
    # while the input is wrong
    while True:
        # ask the user for an input
        try:
            x = int(input(inputMessage))

            # if the value is equal to 1  
            if(x == 1):
                # break the loop as value is correct
                break
                # return the input value to the main code
                return x
            # else if the value is equal to 2
            elif(x == 2):
                # break the loop as value is correct
                break
                # return the input value to the main code
                return x
            # else the input is invalid
            else:
                print("Option invalid...")
        # catch value errors and loop back to the start of the loop
        except ValueError:
            print("Value entered is not an integar")



            

    







