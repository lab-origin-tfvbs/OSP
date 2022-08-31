         #       *       *       *       *       *       *       *       *       +
# D-EJ-ORG-OSP-201
#       *       *       *       *       *       *       *       *       +
"""
- The Programming Cookbook -
Book 1 of 2
Python Kitchen's Safety Training

EJI Nia, 0.0.6+A22831
ISM and EduX Lab, Lab Origin
Released under the SIIF 33 License
AIT ID: D-EJ-ORG-OSP-201
"""

# -- These are "helpers" that I will use throughout this book,
# -- and you'll learn how to write them in the next book.
# -- You may guess what they do if you are interested!
None, INPUT, PRINT = None, input, print

def run_iife(ready, *args, **kwargs):
    if ready is not True: return (lambda *args, **kwargs: None)
    def _run_once(f):
        res = f(*args, **kwargs)
        del f
        return res
    return _run_once

def fill_input(values, allow_overflow = True):
    CURSOR = 0
    def input_(prompt = ""):
        nonlocal CURSOR
        if CURSOR >= len(values):
            if allow_overflow:
                return input(prompt)
            else:
                return print("[?] input() but I have nothing more...") or ""
        res, CURSOR = values[CURSOR], CURSOR + 1
        return print("%s▌%s" % (prompt, res)) or res
    return input_

# a. Instructions for using this book
"""
    This book is designed to be opened in IDLE running Python 3.7+,
    with a monospace font, with Tab Size = 4 (\t = 4 * " "),
    and a screen width of at least 73 characters.
"""

# -- To check for tab size and monospace, check if ↓ and ↑ matches.
#   ↓iIl1{';↓   p.s.    If you can't distinguish the first 4 characters,
#   ↑       ↑           you should also use another font.
# -- Finally, if you can see the end symbol, your window is wide enough. @

"""
    This book is an actual program that could be run.
    If you are experiencing SyntaxError-s, you might have removed
    or added something that you shouldn't have.
    
    Replace that section with the original
    if you are experiencing problems.
"""

# b. Page formatting used in this book
"""
    #       *       *       This is a new page.
    # ...                   This is the end of a page.
    # ↓ ↑                   If you see these arrows, you should
                            type something within these arrows.
                            
    _                       This is a placeholder where you should
                            replace your answer.
    
    Fire? ▌ Sure.           What comes after the little block
                            are simulated user inputs.
                            For example, simulating user entered "Sure".
"""

# -- Have fun playing around with the book!

# ...



#       *       *       *       *       *       *       *       *       +
# 0. What is a program and what does it do?
#       *       *       *       *       *       *       *       *       +

"""
    A program takes input, processes it, and outputs something useful.
    Just like a kitchen: Get ingredients, processes, and delivers
    a delicious dish!

    This is what we called the IPO (Input, Process, Output) Cycle,
    and all programs does this.
    
    For example:
    I: A calculator takes an "expression" (1 + 2 * 3)
    P: Calculates (1 + 2 * 3 = 1 + 6 = 7)
    O: Outputs a result (7)
"""

# This is an example of a full program.
# See you you can spot all of the 3 segments!
def hcf_interactive():
    request = input()
    x, y = (int(n) for n in request.split())
    while y:
        x, y = y, x % y
    print(x)

# ...


#       *       *       *       *       *       *       *       *       +
# 1. Outputting - Deliveroo!
print("\n", "Section 1 - Outputting")
#       *       *       *       *       *       *       *       *       +

"""
    Programs are introverts, they don't tell until we ask for it
    Old computers used to print things on a piece of paper,
    That's why we still uses "print" to output something.
"""

# -- This is how you get your computer to talk back to you.
print("Hello World - Delivering my first order!")
# --

"""
    If you are printing plain English, you should use " " (quotes)
    to quote your line. We will talk more about it in Section 2.
    If you are doing things right, the text should turn green -
    Letting you know that the program recognizes that it is text!
"""

# ↓ Now, try it out on this line and write your own name! ↓ "
_
# ↑ It should only take 1 line. Don't go over here. ↑ "
# -- After that, press F5 to save and run the file.

# ...



#       *       *       *       *       *       *       *       *       +
# 2. The Ingredients Box - How do we get our inputs
print("\n", "Section 2 - Getting Inputs")
#       *       *       *       *       *       *       *       *       +

input = fill_input(
    ("Imagine that I typed this by hand, then press enter", ))

"""
    There are many ways that a kitchen could get its ingredients,
    for example ordering, fetching it from a fridge, or opening boxes.
    Same for programs - They get their data from files, databases, and
    most importantly, from us! ('Get me a Tomato!')
"""

# -- Getting input is easy, just use the input keyword, and ask something.
input("Please say something after the beep... beep! ")
# -- Caution: Chefs will wait FOREVER until they get what they need,
# -- So if you think your program is not working, 
# -- maybe its waiting for your words.
# -- (!) It could also prevent program from closing after it ends.
input = INPUT

print("\n", "Section 2.1 - Input Exercise")
print("Please say something after the beep... beep! ")
(lambda:
# Try to ask the program to repeat what you have said.
# Hint: Combine Section 1 and 2.

# ↓ Try it out on this line. ↓ 
_
# ↑ It should only take 1 line. Don't go over here. ↑
 
or None
)()

# -- Press F5 to save and run the program.
# -- You'll see that the program stops and waits for your input,
# -- before it continues to run the rest.

# -- Restore the line with _ after you are done playing.

#...



#       *       *       *       *       *       *       *       *       +
# 3. Ingredients - Let's talk about formats
print("\n", "Section 3 - Data Formats")
#       *       *       *       *       *       *       *       *       +

"""
    Remember the food pyramid? See how we categorize food?
    Sometimes we need to categorize data so that
    working and communicating on them would be easier.

    In the food pyramid, we have 6 main categories -
    Fats, Diary, Meat, Vegetables, Fruits, Grains;

    While in the programming world, we also have 6 main categories.
    - Nothing: None, or null in other worlds
    - Text: We call them 'String'
    - Numbers: Which includes 'Integer' (Whole) and 'Float' (Decimals)
    - Boolean: Either yes (True) or no (False)
    also...    
    - Collections: 'List / Array', 'Dict or Object', 'Set'
    - Bytes: 'bytes'
"""

# -- In Python, these are their representations.
DATA_TYPES = {
    "Nothing": None,
    "Numbers": {int: 1, float: 3.14159},
        # For float whole numbers, use .0, like 1.0
    "Text": {str: ("This is some text", 'These quotes too')},
        # Remember, text has to be quoted!
    "Boolean": {bool: [True, False]},
    "Collections": {
        list: [1, 1, 2, 3, 5, 7],
        # A queue where you could easily visit one by one.

        tuple: (1, 1, 2, 3, 5, 7),
        # Just like a list, but it cannot be changed.

        dict: {"name": "Eji Nia", "age": 2.078,},
        # aka "Key-Value Pairs", ask key, get value.

        set: {1, 2, 3, 4},
        # There could only be one!
     },
    "Bytes": {bytes: b'\x0d\x0a'}, #\r\n
        # See invisible characters.
}

# -- Try it out - See if you could guess their types!
SECTION_3_QUIZ_1 = [
    
    [   # Q1                ↓ Answer here
        "Hello World!",     _
    ,],
    
    
    [   # Q2    ↓ Answer here
        True,   _
     ,],

    
    [       # Q3    ↓ Answer here
            2,      _
     ,],

    
    [   # Q4    ↓ Answer here
        2.0,    _
     ,],

    
    [   # Q5        ↓ Answer here
        b"nyaa!",   _
     ,],

            
    [   # Q6        ↓ Answer here
        [1, 2],     _
      ,],

         
    [#  Q7                      ↓ Answer here
        (1, 2, 3, "daisuki"),   _
      ,],
    
    
    [   # Q8            ↓ Answer here
        "2.1314",       _
     ,],

    
    [   # Q9                            ↓ Answer here
        {"has_??": True, 3.14: 3},      _
     ,],
]


# -- This is the automatic answer checker.
# -- You will learn how to write your own in the next book!
@run_iife(  True   ,   SECTION_3_QUIZ_1)
def check_answers(questions):
    print("\n", "Grading Section 3 Quiz...")
    for q_number, (value, type_) in enumerate(questions, start=1):
        if type(value) != type_:
            message = "[X] Q%i: %s is not of type %s; Try again!"
            return print(message % (q_number, value, type_)) or False
    return print("All correct! You did well!") or True
# -- as usual, press F5 to save and run the file.

# ...


#       *       *       *       *       *       *       *       *       +
# 4. Plates - Where we store our half-baked ingredients
print("\n", "Section 4 - Variables")
#       *       *       *       *       *       *       *       *       +

"""
    Rome was not built in one day, so was every delicious dish.
    In a kitchen, we use plates and tables to store half-made food;
    and in programs, we do the same! (but with a small difference)

    As we are working with text only, we give each of our plates a name.
    Names can include these characters [A-z0-9_],
    BUT CANNOT start with a number! (Computer read them as numbers)
    
    To place (or replace) and item, simply use the = (equal) sign.
    Think of it as a left arrow ←,
    Plate on left containing things on the right, like this -
    [🍽️ ← 🥩] [Plate = Meat]
"""

# ↓ Try putting a number on plate_1 on this line. ↓ 

# ↑ It should only take 1 line. Don't go over here. ↑
print("plate_1 has (( %s ))" % globals().get("plate_1", None))


# Now, try adding another number to the number on plate_1.
# Hint: Combine and replace!
# ↓ Try it on this line. ↓ 

# ↑ It should only take 1 line. Don't go over here. ↑
print("After adding...", "plate_1 has (( %s ))" % \
      globals().get("plate_1", None), sep="\n")

# If you are getting any errors, that means that something is off.
# Try again by removing those lines.

# ...



#       *       *       *       *       *       *       *       *       +
# Book 1 Overview
#       *       *       *       *       *       *       *       *       +
"""
    This is the end of Book 1, and you should have
    acquired your safety training pass!

    Move on to Book 2, where we will do some real dishes.
    Before you move on, make sure that you have these in your head...
"""

# Book 1 Checklist
[
    [_], "IPO (p.s. its not about stocks)",
    [_], "How to get user input",
    [_], "How to get program output",
    [_], {"Knowing these": [None, str, int, bool and list]},
    [_], "Variables and knowing how to assign and modify them",
]

# ...
print("--- End of Book 1 ---")
