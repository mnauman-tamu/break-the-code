import numpy as np
import tkinter as tk
import pandas as pd
# import random

questions = [
    'What\'s the difference between your highest and lowest tiles?',
    'What is the sum of your three leftmost tiles?',
    'What is the sum of your three rightmost tiles?',
    'What is the sum of your central tiles? (2-3p: B+C+D; 4p: B+C)',
    'What is the sum of your tiles?',
    'What is the sum of your black tiles?',
    'What is the sum of your white tiles?',
    'How many of your tiles have a black number?',
    'How many of your tiles have a white number?',
    'How many of your tiles have a white number? ',
    'Is the tile in the C-position (the third tile) higher than 4?',
    'Where is 5?',
    'Where is 1 or 2?',
    'Where is 8 or 9?',
    'Where is 0?',
    'Where is 6 or 7?',
    'Where do you have neighboring tiles of the same color?',
    'Where do you have tiles in sequential order? / Which neighboring tiles have consecutive numbers?',
    'How many odd tiles do you have?',
    'How many even tiles do you have? (0==even)',
    'How many of your tiles have the same number?'
]
nums = [f'{i}b' for i in range(5)] + [f'{i}w' for i in range(5)] + ['5g','5g'] + [f'{i}w' for i in range(6, 10)] + [f'{i}b' for i in range(6, 10)]

np.random.shuffle(nums)
np.random.shuffle(questions)
print(nums)
print(questions[np.random.randint(len(questions))])

p1nums= nums[0:5]
p2nums= nums[5:10]
p1nums.sort(key=lambda x: (int(x[0]), x[1]))
p2nums.sort(key=lambda x: (int(x[0]), x[1]))

p1nums += ['a','b','c','d','e']
p2nums += ['a','b','c','d','e']

initialQuestions = questions[0:6]
questions = questions[6:]


######GUI#####
root = tk.Tk()
frame = tk.Frame(root)
root.title("Break the Code")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


lblLine0 = tk.Label(frame, text = "***")
lblLine0.grid(row=0, column=0, columnspan=5)

frame.grid(row=0, column=0, sticky="news")
grid = tk.Frame(frame)
grid.grid(sticky="news", column=0, row=7, columnspan=2)
frame.rowconfigure(7, weight=1)
frame.columnconfigure(0, weight=1)

# INITIAL QUESTION LIST
questionList = []
for i, q in enumerate(initialQuestions):
    button = tk.Button(frame, text=q, height=10, width=20, wraplength=120, command = lambda i = i : replaceQuestion(i))
    questionList.append(button)

for row in range(0,2):
    for col in range(0,3):
        questionList[row*3+col].grid(row=row+1, column=col+1, sticky="news")

lblLine1 = tk.Label(frame, text = "***")
lblLine1.grid(row=3, column=0, columnspan=5)

# Guess Button
guessButton = tk.Button(frame, text="Guess")
guessButton.grid(row=4, column=0, columnspan=5)

lblLine2 = tk.Label(frame, text = "***")
lblLine2.grid(row=5, column=0, columnspan=5)

# Tiles
buttons=[]
for n1 in p1nums:
    button = tk.Button(frame, text=n1, state=tk.DISABLED, width=20)
    buttons.append(button)

for i in range(0,5):
    # TODO: Change Row
    buttons[i].grid(row=6, column=i, sticky="news")
    buttons[i+5].grid(row=7, column=i, sticky="news")

def replaceQuestion(i):
    global questions, questionList
    if questions == []:
        # Disabled
        questionList[i]["text"] = ""
        questionList[i]["state"] = tk.DISABLED
    else:
        q = questions.pop()
        questionList[i]["text"] = q

def handleGuess():
    pass

# TODO: Work on a chat engine
# Work on client server communication/disabling etc.
# Handle Guess
# Maybe implements an answer helper that answers the asked question
# Make the GUI better; customtkinter?

frame.mainloop()

# if __name__ == "__main__":
#     Main()

# print("Hello World!")