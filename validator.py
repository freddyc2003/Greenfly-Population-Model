def intValidator(inputMessage):
    while True:
        try:
            x = int(input(inputMessage))
            return x
            break
        except ValueError:
            print("Value entered is not an integar")
            

def survivalRateValidator(inputMessage):
     while True:
        try:
            x = float(input(inputMessage))
            if(x <= 1 and x >= 0):
                return x
                break
            else:
                print("Value is not between 1 and 0")
                continue
        except ValueError:
            print("Value entered is not a float")


def generationValidator(inputMessage):
    while True:
        try:
            x = int(input(inputMessage))
            if(x <= 25 and x >= 5):
                return x
                break
            else:
                print("Value is not between 5 and 25")
                continue
        except ValueError:
            print("Value entered is not a integar")


    







