"""
Basic Rule-Based Chatbot
CodeAlpha Python Programming Internship - Task 4

A simple console chatbot that responds to predefined user inputs
using if-elif logic. Concepts used: if-elif, functions, loops, input/output.
"""

import random


def get_bot_response(user_input):
    """
    Takes the user's message, cleans it up, and returns a matching
    reply based on simple keyword rules.
    """
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm CodeBot, a simple rule-based chatbot built in Python."

    elif "help" in text:
        return "Sure! You can say hello, ask how I am, ask my name, or say bye to exit."

    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day."

    elif "thank" in text:
        return random.choice(["You're welcome!", "No problem at all!", "Anytime!"])

    elif "weather" in text:
        return "I can't check live weather yet, but I hope it's sunny where you are!"

    elif text == "":
        return "Please type something so I can respond."

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    """
    Main loop: keeps asking the user for input and printing bot replies
    until the user decides to exit.
    """
    print("=" * 50)
    print(" CodeBot - Basic Rule-Based Chatbot")
    print("=" * 50)
    print("Type 'help' to see available commands, or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("CodeBot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    run_chatbot()
