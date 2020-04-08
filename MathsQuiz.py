import time
import random

gameisrunning = True


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
    is_int(bad_input) == False
    if is_int(bad_input) != False:
        user_input = int(bad_input)
        while user_input > 3 or user_input <= 0:
            print("Invalid menu option.")
            get_user_input()
        else:
            return user_input
    else:
        print('Invalid menu option')
        get_user_input()


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(str(" = ")))
    return result


def check_solution(user_solution, actual_solution, count):
    if user_solution == actual_solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count



def display_result(totalqs, amntcorrect):            #the fucntion for getting the points and amount correct
    amntcorrect = 0
    if totalqs > 0:
        result = int(amntcorrect) * 10
        points = result
    if totalqs == 0:
        points = 0
    print("You answered", totalqs, "questions with", amntcorrect, "correct.")
    print("Your score is ", points, "%. Thank you.")
    return points


def questions(count, totalqs, amntcorrect):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)

   # print(result, points, total)
    user_input = get_user_input()
    
    if user_input == 1:#the selection criteria for easy questions
        randnum2 = (1, 2)#randomises the chances of getting addition and subtraction problems
        if random.choice(randnum2) == 1:
            problem = str(number_one) + " + " + str(number_two)#gives us the addition  problems
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count        
    else:
        if user_input == 2: #the selection criteria for hard questions
            randnum = (1, 2) #randomises the chances of getting division and multiplication problems
            if (random.choice(randnum)) == 1:
                problem = str(number_one) + " * " + str(number_two)
                solution = number_one * number_two
                user_solution = get_user_solution(problem)
                count = check_solution(user_solution, solution, count)
                return count
            else:
                problem = str(number_one) + " // " + str(number_two)
                solution = number_one * number_two // number_two
                user_solution = get_user_solution(problem)
                count = check_solution(user_solution, solution, count)
                return count



def main():#this is what actually appears in the terminal when the program is run
    totalqs = 0
    amntcorrect = 0
    count = 0 
    while gameisrunning == True:
        display_menu()
        menu_option = get_user_input()
        totalqs = totalqs + 1
        amntcorrect = questions(count, totalqs, amntcorrect)

        if menu_option == 3:
            gameisrunning == False
            print("Exit the quiz.")              #prints the results and how many points you have gotten right
            display_result(totalqs, amntcorrect)



main()
