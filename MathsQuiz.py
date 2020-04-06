import time
import random


rightqs = 0


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


def get_user_input(): #invalidates incorrect inputs, rather than have the program crash
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


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count



def display_result(total, correct):            #the fucntion for getting the points and amount correct
    if total > 0:
        result = int(correct) * int(10)
        points = result
    if total == 0:
        points = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", points, "%. Thank you.")


def option(count, total, correct, get_user_input):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if get_user_input is 1:#the selection criteria for easy questions
        randnum2 = (1, 2)#randomises the chances of getting addition and subtraction problems
        if (random.choice(randnum2)) == 1:
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
        else get_user_input is 2:#the selection criteria for hard questions
        randnum = (1, 2) #randomises the chances of getting division and multiplication problems
        if (random.choice(randnum)) == 1:
            problem = str(number_one) + " * " + str(number_two)
            solution = number_one * number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            problem = str(number_one) + " // " + str(number_two)
            solution = number_one // number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count



def main():                  #this is what actually appears in the terminal when the program is run
    display_menu()
    menu_option = get_user_input()
    total = (0)
    correct = (0)
    count = (0)
    while option != 3:
        total = total + 1
        correct = menu_option(count, total, correct, get_user_input)
        

    print("Exit the quiz.")              #prints the results and how many points you have gotten right
    display_result(total, correct)



main()