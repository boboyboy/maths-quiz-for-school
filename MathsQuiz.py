import time
import random


count = 0
rightqs = 0
counts = count + points

def display_menu():
    menu_list = ["1. Easy", "2. Hard", "Results"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(str(" = ")))
    return result


def check_solution(user_solution, solution, counts):
    if user_solution == solution:
        counts = count + 1
        print("Correct.")
        return counts
    else:
        print("Incorrect.")
        return counts


def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index is 1:
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
    elif index is 2:
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
    elif index is 3:
        print(counts)


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep = "")


def main():
    display_menu()
    option = get_user_input()
    totals = 0
    correct = 0
    while option != 5:
        total = totals + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_result(total, correct)

main()