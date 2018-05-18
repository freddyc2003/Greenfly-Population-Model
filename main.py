####################  Imports ####################
import sys
import csv
import os.path
import time
import random
import validator

#################### Assign Variables ####################
survivalRate = []
population = []
totalPopulation = []
typesGreenfly = ['Juvenile','Adult','Senile']
birthRate = 0
generations = 0
triggerPoint = 0
diseaseFactor = 0

#################### Main Menu ####################
def mainMenu():
    print("-"*20, "Main Menu", "-"*20)
    print("""1: Set the Generation 0 values
2: Display the Generation 0 values
3: Run the model
4: Export data
5: Disease Control
6: Quit""")

    print("-"*51)

    # take a number from the user and redirect accordingly
    choice = validator.intValidator("What do you want to do? Enter a number: ")    

    print("-"*51)
    
    if(choice == 1): # if choice is 1 then run func set generation values
        setGenerationValues()
    elif(choice == 2): # if choice is 2 then func display the generation values
        displayGeneration()
    elif(choice == 3): # if choice is 3 then run func that runs the model
        if(not population): # if generation 0 values are not set then don't run the model
            print("You must first enter the generation 0 values")
            time.sleep(1)
            mainMenu() # run the main menu
        elif(diseaseFactor == 0): # if disease factor is not set run the standard model
            runModel()
        else: # if disease factor is set then run the disease model
            diseaseModel()
    elif(choice == 4): # if choice is 4 then run func export
        if(not population): # if generation 0 is not set then don't run export func
            print("You must first enter the generation 0 values and run the model")
            time.sleep(1)
            mainMenu()
        else: # else run the export func
            exportData()
    elif(choice == 5): # if choice is 5 then run func to set disease trigger and generate factor
        diseaseControl()
    elif(choice == 6): # if choice is 5 exit from the program
        sys.exit()
    else: # else invalid menu option
        print("Value is out of range...") 
        time.sleep(1)
        mainMenu()
        


#################### Set Generation Model ####################
def setGenerationValues():
    # import the variables into the functions scope
    global birthRate, generations, survivalRate, population
    
    # ask the user for the population numbers
    populationNumbersJuvenile = validator.intValidator("Enter the Juvenile Population Numbers: ")
    populationNumbersAdult = validator.intValidator("Enter the Adult Population Numbers: ")
    populationNumberSenile = validator.intValidator("Enter the Senile Population Numbers: ")

    # print a dashed line
    print("-"*51)

    # append the population numbers to the population array
    population.append([populationNumbersJuvenile, populationNumbersAdult, populationNumberSenile])
    total = populationNumbersJuvenile + populationNumbersAdult + populationNumberSenile
    totalPopulation.append(total)

    # ask the user for survival rates
    survivalRateJuvenile = validator.survivalRateValidator("Enter the Juvenile Survival Rate: ")
    survivalRateAdult = validator.survivalRateValidator("Enter the Adult Survival Rate: ")
    survivalRateSenile = validator.survivalRateValidator("Enter the Senile Survival Rate: ")

    # print a dashed line
    print("-"*51)

    # append the survival rates to the array
    survivalRate.append(survivalRateJuvenile)
    survivalRate.append(survivalRateAdult)
    survivalRate.append(survivalRateSenile)
    
    # ask user for birth rate
    birthRate = validator.intValidator("Enter the birth rate: ")

    # print a dashed line
    print("-"*51)

    # ask user for the number of generations to model
    generations = validator.generationValidator("Enter the number of generations to model: ")

    # return to main menu by running the main menu function
    mainMenu()
    
        
#################### Run Model ####################
def runModel():
    print("\n")
    # print the gen 0 values
    print("generation 0 : ", population[0], " Total: ", totalPopulation[0])
    
    # for each generation up to the total number of generations to model
    for generation in range(0, generations):
        # for i equal to 0, 1, 2
        for i in range(0, 2):
            # generation i value is equal to the current generation i value * the survival rate for that type of greenfly
            population[generation][i] = population[generation][i] * survivalRate[i]

        # temp adult variable = generation juvenile value
        tempAdult = population[generation][0]

        #temp senile variable = generation adult value
        tempSenile = population[generation][1]

        # new juvenile value = generation adult value * birth rate
        juvenile = population[generation][1] * birthRate

        # append the new generation to the population array
        population.append([juvenile, tempAdult, tempSenile])

        # total population of the generation = total value of generation Juvenile, Adult and Senile values
        total = population[generation + 1][0] + population[generation + 1][1] + population[generation + 1][2]

        # append total to the total array
        totalPopulation.append(total)

        # print the just appended generation
        print("generation", (generation + 1), ": ", population[generation + 1], " Total: ", totalPopulation[generation + 1])

                
    print("\n")

    # print the total population 
    print(totalPopulation)

    print("\n")

    # run main menu func
    mainMenu()


#################### Disease Model ####################
def diseaseModel():
    
    print("\n")
    
    # print the first generation values
    print("generation 0 : ", population[0], " Total: ", totalPopulation[0])
    
    # for each generation up to the total number of generations to model
    for generation in range(0, generations):
        
        if(totalPopulation[generation] > triggerPoint): # if the total population of the last generation is greater than the trigger point value
            
            # for i equal to 0, 1, 2
            for i in range(0, 2):
                
                # generation i value is equal to the current generation i value * the survival rate for that type of greenfly
                population[generation][i] = population[generation][i] * survivalRate[i] * diseaseFactor

            # temp adult variable = generation juvenile value
            tempAdult = population[generation][0]

            #temp senile variable = generation adult value
            tempSenile = population[generation][1]

            # new juvenile value = generation adult value * birth rate
            juvenile = population[generation - 1][1] * birthRate * diseaseFactor

            # append the new generation to the population array
            population.append([juvenile, tempAdult, tempSenile])

            # total population of the generation = total value of generation Juvenile, Adult and Senile values
            total = population[generation + 1][0] + population[generation + 1][1] + population[generation + 1][2]

            # append total to the total array
            totalPopulation.append(total)

            # print the just appended generation
            print("generation", (generation + 1), ": ", population[generation + 1], " Total: ", totalPopulation[generation + 1])
            
        else: # else if the total population is not greater than the trigger point

            # for i equal to 0, 1, 2
            for i in range(0, 2):

                # generation i value is equal to the current generation i value * the survival rate for that type of greenfly
                population[generation][i] = population[generation][i] * survivalRate[i]

            # temp adult variable = generation juvenile value
            tempAdult = population[generation][0]

            #temp senile variable = generation adult value
            tempSenile = population[generation][1]

            # new juvenile value = generation adult value * birth rate
            juvenile = population[generation - 1][1] * birthRate * diseaseFactor

            # append the new generation to the population array
            population.append([juvenile, tempAdult, tempSenile])

            # total population of the generation = total value of generation Juvenile, Adult and Senile values
            total = population[generation + 1][0] + population[generation + 1][1] + population[generation + 1][2]

            # append total to the total array
            totalPopulation.append(total)

            # print the just appended generation
            print("generation", (generation + 1), ": ", population[generation + 1], " Total: ", totalPopulation[generation + 1])
            

                
    print("\n")

    # print the total population value
    print(totalPopulation)

    print("\n")
    
    # run main menu func
    mainMenu()


#################### Display Generation 0 Values ####################
def displayGeneration():

    # print generation 0 survival rates
    print("Juvenile Survival Rate: ", survivalRate[0])
    print("Adult Survival Rate: ", survivalRate[1])
    print("Senile Survival Rate: ", survivalRate[2])

    print("\n")

    # print generation 0 population numbers
    print("Juvenile Population Numbers: ", population[0][0])
    print("Adult Population Numbers: ", population[0][1])
    print("Senile Population Numbers: ", population[0][2])

    print("\n")

    # print generation 0 birth rate
    print("Birth Rate: ", birthRate)

    # run main menu func
    mainMenu()


#################### Export Data ####################
def exportData():
    # take filenmae input and asign it to a variable 
    filename = validator.filenameValidator("What would you like the file to be called?: ")

    if(os.path.isfile(filename + ".csv")): # if file already exists

        # ask user for a new filename or if they would like to overwrite the current file
        option = validator.optionValidator("This file name already exists would you like to overwrite it [1] or change the file name [2]: ")

        # if option is equal to 1
        if(option == 1):

            # write the data to a file
            with open(filename + '.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                for i in population:
                    spamwriter.writerow(i)

            # notify the user that the file was written successfully
            print("file written succesfully...")
            time.sleep(1)
            
        else: # else ask the user what they would like to rename the file to

            # take filenmae input and asign it to a variable 
            filename = validator.filenameValidator("What would you like the file to be called?: ")
            
    else: # else the file does not exist

        # write the data to a file
        with open(filename + '.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for i in population:
                spamwriter.writerow(i)

        # notify the user that the file was written successfully      
        print("file written succesfully...")
        time.sleep(1)

    # run main menu func
    mainMenu()


#################### Disease Control ####################
def diseaseControl():

    # import the global variables
    global triggerPoint, diseaseFactor

    # ask user for a trigger point value
    triggerPoint = validator.intValidator("What do you want the population trigger point to be: ")

    # generate a random number between 0.5 and 0.8
    diseaseFactor = random.randint(50, 80) / 100

    # run main menu func
    mainMenu()


# run main menu func
mainMenu()



