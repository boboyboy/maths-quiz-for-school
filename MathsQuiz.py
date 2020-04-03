import time
import random


rightqs = 0


def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True


def display_menu():
    menu_list = ["1. Easy", "2. Hard", "Results"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])


def get_user_input():
    bad_input = input("Enter your choice: ")
    if is_int(bad_input) == True:
        user_input = int(bad_input)
        while user_input > 3 or user_input <= 0:
            print("Invalid menu option.")
            get_user_input()
        else:
            return user_input
    else:
        print('invalid input')
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



def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.")


def menu_option(index, count, total, correct, get_user_input):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if get_user_input is 1:
        randnum2 = (1, 2)
        if (random.choice(randnum2)) == 1:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
            return count
        else:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution, count)
    elif get_user_input is 2:
        randnum = (1, 2)
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
    elif get_user_input is 3:
        display_result(total, correct)

def main():
    display_menu()
    index = get_user_input()
'''option = get_user_input()
    total = int(0)
    correct = int(0)
    count = int(0)
    while option != 5:
        total = total + 1
        correct = menu_option(index, count, total, correct, get_user_input)
        option = get_user_input()

    print("Exit the quiz.")
    display_result(total, correct)'''



main()