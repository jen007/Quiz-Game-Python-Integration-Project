"""A quiz game based on my favorite show"""
__author__ = "Jennifer Lopez"
# An integration project created from the material I learned.


# A list of multiple questions within a variable.
questions = ["How many cast members are currently active on Running Man?"
             "\nA. 9\nB. 7\nC. 8\nD. 5",
             "Running Man celebrated their 10 anniversary on which episode?"
             "\nA. 512\nB. 300\nC. 410\nD. 511 ",
             "What year was Running Man almost cancelled?"
             "\nA. 2017\nB. 2012\nC. 2019\nD. 2015 ",
             "Which two hollywood actor appeared in Running Man?"
             "\nA. Jack Black and Angelina Jolie"
             "\nB. Tom Cruise and Ryan Reynolds "
             "\nC. Ryan Reynolds and Hugh Jackman"
             "\nD. none of the above",
             ]

# A variable with a list of all possible answers.
answers = [{"C", "c", "8"},
           {"D", "d", "511"},
           {"A", "a", "2017"},
           {"B", "b", "Tom Cruise and Ryan Reynolds"}
           ]

# The variable that contains the explanation of each question.
explanations = ["Running man consist of 8 members.",
                "Running Man celebrated their 10 anniversary on episode "
                "511 via live stream.",
                "Running Man was schedule to cancelled on February 2017",
                "Both Tom Cruise and Ryan Reynold appeared on Running",
                ]


# Function definition
# Create a variable that will increase when the user types the correct choice
# A loop with a zip()function that iterates over the three lists
# The print statement will print each question
# The variable will store the user input
# The user answer will be compared with the list of answers
# If the user answer is true a point is awarded.
# If the answer is wrong no point is awarded.
# The last printed statement calculates the total amount of correct answer
# str = convert the string into a number
# len = returns the number of items in an object.
# float are numbers written with a decimal point
# + is a string operators that is found on the last printed statement
def running_man_knowledge_quiz():
    """The purpose of the function is to quiz the user's knowledge of how well
    they know the variety show by providing multiple choice."""
    score = 0
    for question, answer, explanation in zip(questions, answers, explanations):
        print(question)
        user_answer = input("Answer: ")
        if user_answer in answer:
            print("Correct",
                  end="\n\n")  # end="\n" adds a blank line at the end
            score += 1
        else:
            print("Incorrect", explanation, end="\n\n")
    print("You got" + " " + str(score) + " " + "out of", len(questions),
          ", equivalent to ", float(score / len(questions)) * 100, "%", "\n")


# A variable that contains a list of questions.
math_questions = ["What is 15 ** 2?",
                  "What is 30 * 5 ?",
                  "What is 60 / 6 ?",
                  "What is 6 + 7 ?",
                  "What is 20 - 8 ?",
                  "What is 10 // 4 ?",
                  "What is 100 % 5 ?",
                  ]

# A variable that contains a list of math answers.
math_answers = [{15 ** 2},  # exponent
                {30 * 5},  # multiplication
                {60 / 6},  # division
                {6 + 7},  # addition
                {20 - 8},  # subtraction
                {10 // 4},  # Floor division
                {100 % 5},  # Modulus
                ]

# A variable that contains a list of math explanation.
math_explanations = [(15 ** 2),
                     (30 * 5),
                     (60 / 6),
                     (6 + 7),
                     (20 - 8),
                     (10 // 4),
                     (100 % 5)
                     ]


# The function definition for a math quiz.
# Checks out the user answers and compares it with the correct answer key.
# Points are awarded if the user got the answer correct.
# The last printed statement will show the amount of correct answer the user.
# Amount of correct answers divided by total and the grade percentage.
def math_quiz():
    """The purpose of this function is to test the user's ability on how well
    they can solve math problems."""
    score = 0
    for math_question, math_answer, math_explanation in zip(math_questions,
                                                            math_answers,
                                                            math_explanations):
        print(math_question)
        user_answer = float(input("Answer:"))
        if user_answer in math_answer:
            print("Correct", end="\n\n")
            score += 1
        else:
            print("Incorrect", math_explanation, end="\n\n")
    print("You got" + " " + str(score) + " " + "out of", len(math_questions),
          ", equivalent to ", float(score / len(math_questions)) * 100, "%",
          "\n")


# A variable with a list of true and false questions inside brackets.
true_or_false_questions = ["Lee Kwang Soo is the Prince of Asia?",
                           "Running Man number 7012?",
                           "Running Man came to North America?",
                           "The giraffe is the tallest animal in the world?",
                           "7000 is greater than 7020?",
                           "BTS and BlackPink appeared on Running Man"
                           ]

# A variable with all the possible correct choices.
solutions = [{"True", "true", "T", "t"},
             {"True", "true", "T", "t"},
             {"False", "false", "F", "f"},
             {"True", "true", "T", "f"},
             {"False", "false", "F", "f"},
             {"True", "true", "T", "t"}
             ]

# A variable that contains a list of explanation.
true_false_explanations = ["Lee Kwang Soo was named the Prince of Asia for "
                           "his popularity",
                           "The number 7012 became a symbol for the show",
                           "Running Man has never been to America",
                           "The giraffe is the tallest animal in the world",
                           "7000 is smaller than 7020",
                           "BTS and BlackPink had appeared on the show"
                           ]


# the function definition for true and false.
# checks out the user answers and compares it with the correct answer key.
# points are awarded if the user got the answer correct.
# the last printed statement will show the amount of correct answer the user.
# got correct and the grade percentage.
def true_false():
    """The purpose of this function is to provide the user with questions that
    are either true or false."""
    score = 0
    for true_or_false_question, solution, true_false_explanation in zip(
            true_or_false_questions, solutions, true_false_explanations):
        print(true_or_false_question)
        user_answer = input("True or False:")
        if user_answer in solution:
            print("Correct", end="\n\n")
            score += 1
        else:
            print("Incorrect", true_false_explanation, end="\n\n")
    print("You got" + " " + str(score) + " " + "out of",
          len(true_or_false_questions), ", equivalent to ",
          float(score / len(true_or_false_questions)) * 100, "%", "\n")


# function definition
# printed statements
# If the program continues than it's true.
# A while loop, states "when the program continues, type the options you want
# if, elif, and else are standard conditional structures / statements"
# when the program is false the game ends
# main_menu() is the call function

def main_menu():
    """The purpose of this function is to provide the user with the main menu
    that contains a list of options for the user to select."""

    print("**************************************************************")
    print("*            Welcome to the Running Man Quiz Game!           *")
    print("**************************************************************")
    print("* Select an option to start the game:                        *")
    print("* 1. Test your knowledge on the show?                        *")
    print("* 2. Simple M.A.T.H                                          *")
    print("* 3. True of False                                           *")
    print("* 0. Quit the game                                           *")
    print("**************************************************************")
    continue_program = True
    while continue_program:
        choice = int(input("Enter a number: "))
        if choice == 1:
            running_man_knowledge_quiz()
        elif choice == 2:
            math_quiz()
        elif choice == 3:
            true_false()
        elif choice == 0:
            print("Thank you for playing!", "You have exited the game.",
                  sep="\n")  # separate into two-line
            continue_program = False
        else:
            print("Invalid" + "." + "Please, try again", end="\n\n")
            # end="\n\n" adds a space line after the sentence


main_menu()
