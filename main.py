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
        if(not population):
            print("You must first enter the generation 0 values")
            time.sleep(1)
            mainMenu()
        elif(diseaseFactor == 0):
            runModel()
        else: 
            diseaseModel()
    elif(choice == 4): # if choice is 4 then run func export
        if(not population):
            print("You must first enter the generation 0 values and run the model")
            time.sleep(1)
            mainMenu()
        else:
            exportData()
    elif(choice == 5):
        diseaseControl()
    elif(choice == 6): # if choice is 5 exit from the program
        sys.exit()
    else:
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
    print("generation 0 : ", population[0], " Total: ", totalPopulation[0])
    
    for generation in range(0, generations):
        for i in range(0, 2):
            
            population[generation][i] = population[generation][i] * survivalRate[i]

        tempAdult = population[generation][0]

        tempSenile = population[generation][1]

        juvenile = population[generation][1] * birthRate
            
        population.append([juvenile, tempAdult, tempSenile])

        total = population[generation + 1][0] + population[generation + 1][1] + population[generation + 1][2]

        totalPopulation.append(total)

        print("generation", (generation + 1), ": ", population[generation + 1], " Total: ", totalPopulation[generation + 1])

                
    print("\n")

    print(totalPopulation)

    print("\n")
    
    mainMenu()


def diseaseModel():
    print("\n")
    print("generation 0 : ", population[0], " Total: ", totalPopulation[0])
    for generation in range(0, generations):
        if(totalPopulation[generation] > triggerPoint):
            for i in range(0, 2):
                
                population[generation][i] = population[generation][i] * survivalRate[i] * diseaseFactor

            tempAdult = population[generation][0]

            tempSenile = population[generation][1]
            
            juvenile = population[generation - 1][1] * birthRate * diseaseFactor
                
            population.append([juvenile, tempAdult, tempSenile])

            total = population[generation + 1][0] + population[generation + 1][1] + population[generation + 1][2]

            totalPopulation.append(total)

            print("generation", (generation + 1), ": ", population[generation + 1], " Total: ", totalPopulation[generation + 1])
        else:
            for i in range(0, 2):
            
                population[generation][i] = population[generation][i] * survivalRate[i]

            tempAdult = population[generation][0]

            tempSenile = population[generation][1]

            juvenile = population[generation][1] * birthRate
            
            population.append([juvenile, tempAdult, tempSenile])

            total = population[generation + 1][0] + population[generation + 1][1] + population[generation + 1][2]

            totalPopulation.append(total)

            print("generation", (generation + 1), ": ", population[generation + 1], " Total: ", totalPopulation[generation + 1])
            

                
    print("\n")

    print(totalPopulation)

    print("\n")
    
    mainMenu()


#################### Display Generation 0 Values ####################
def displayGeneration():
    print("Juvenile Survival Rate: ", survivalRate[0])
    print("Adult Survival Rate: ", survivalRate[1])
    print("Senile Survival Rate: ", survivalRate[2])

    print("\n")

    print("Juvenile Population Numbers: ", population[0][0])
    print("Adult Population Numbers: ", population[0][1])
    print("Senile Population Numbers: ", population[0][2])

    print("\n")
    
    print("Birth Rate: ", birthRate)

    mainMenu()


#################### Export Data ####################
def exportData():
    filename = input("What would you like the file to be called? ")

    if(os.path.isfile(filename + ".csv")):
        option = int(input("This file name already exists would you like to overwrite it [1] or change the file name [2]: "))
        if(option == 1):
            with open(filename + '.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile)
                for i in population:
                    spamwriter.writerow(i)
            
        else:
            filename = input("What would you like the file to be called? ")
            
    else:
        with open(filename + '.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for i in population:
                spamwriter.writerow(i)
        
    
    mainMenu()


#################### Disease Control ####################
def diseaseControl():
    global triggerPoint, diseaseFactor

    triggerPoint = validator.intValidator("What do you want the population trigger point to be: ")

    diseaseFactor = random.randint(50, 80) / 100

    mainMenu()

   
mainMenu()



