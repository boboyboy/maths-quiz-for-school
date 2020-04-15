import time
import random

gameisrunning = True
amntcorrect = 0
count = 0
def changea(tof):
    global gameisrunning
    gameisrunning = tof

def is_int(val): #invalidates str inputs
    try:
        num = int(val)
    except ValueError:
        return False
    return True

def display_menu():    #the function for the main menu
    menu_list = ["1. Easy", "2. Hard", "Results"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])


def get_user_input(): 
    #this function takes the input, determines if it is an int or str and returns it if it is a usable int
    bad_input = input("Enter your choice: ") 
    if is_int(bad_input) == True:
        user_input = int(bad_input)
        if user_input > 3 or user_input <= 0:
            print("Invalid menu option.")
            get_user_input()
        else:
            return user_input
    else:
        print('Invalid menu option')
        get_user_input()


def get_user_solution(problem):
    print("Enter your answer")
    print(problem)
    result = input(" = ")
    if is_int(result) == True:
        print(type(result))
        return result
    
    else: 
        print('invalid answer')
        #get_user_solution(problem)
        return 0



def check_solution(user_solution, actual_solution, count):
    print(user_solution, actual_solution, type(user_solution), type(actual_solution), user_solution != actual_solution)

    if int(user_solution) == actual_solution:
        count = count + 1
        print("Correct.")
        return count
    else: 
        print("Incorrect.")
        return count



def display_result(totalqs, count, user_solution, actual_solution):            #the fucntion for getting the points and amount correct
    if totalqs > 0:
        points = int(count) * 10

    elif totalqs == 0:
        points = 0
    if int(user_solution) != actual_solution:
        points = int(points) - 5
    print("You answered", totalqs, "questions with", count, "correct.")
    print("Your score is ", points, " points. Thank you.", sep = "")
    return points


def questions(count, totalqs):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)


   # print(result, points, total)
    user_input = get_user_input()
    
    if user_input == 1:#the selection criteria for easy questions
        randnum2 = (1, 2)#randomises the chances of getting addition and subtraction problems
        if random.choice(randnum2) == 1:
            problem = str(number_one) + " + " + str(number_two)#gives us the addition  problems
            actual_solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, actual_solution, count)
            return count
        else:
            problem = str(number_one) + " - " + str(number_two)
            actual_solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, actual_solution, count)
            return count        
    elif user_input == 2: #the selection criteria for hard questions
        randnum = (1, 2) #randomises the chances of getting division and multiplication problems
        if (random.choice(randnum)) == 1:
            problem = str(number_one) + " * " + str(number_two)
            actual_solution = number_one * number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, actual_solution, count)
            return count
        else:
            problem = str(number_one) + " // " + str(number_two)
            actual_solution = number_one // number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, actual_solution, count)
            return count
    elif user_input == 3:
        #print("Exit the quiz.")              #prints the results and how many points you have gotten right
        #display_result(totalqs, amntcorrect)
        changea(False)


def main():#this is what actually appears in the terminal when the program is run
    totalqs = 0
    count = 0 
    user_solution = 0
    actual_solution = 0
    while gameisrunning == True:
        display_menu()
        totalqs = totalqs + 1
        count = questions(count, count)
        print(totalqs)
        print(count)
        print(display_result(totalqs, count, user_solution, actual_solution))

    if gameisrunning == False:
        print("Exit the quiz.")              #prints the results and how many points you have gotten right
        display_result(totalqs, amntcorrect, user_solution, actual_solution)


main()