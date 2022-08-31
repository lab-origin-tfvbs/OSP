#       *       *       *       *       *       *       *       *       +
# D-EJ-ORG-OSP-202
#       *       *       *       *       *       *       *       *       +
"""
- The Programming Cookbook -
Book 2 of 2
Taking your first order!
Demo Project - Random Names Picker

EJI Nia, 0.0.2+A22829
ISM and EduX Lab, Lab Origin
Released under the SIIF 33 License
AIT ID: D-EJ-ORG-OSP-202
"""

# -- These are "helpers" that I will use throughout this book.
# -- You should be able to read some of them after this book.
# -- Try to understand how it works if you want!
_, INPUT, PRINT = None, input, print

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

class Writable:
    def __init__(self, body = ""):
        self.body = ""
        
    def write(self, any_):
        self.body += str(any_)

def trap_io_and_run(f, inputs, file = None, allow_overflow = True):
    global PRINT
    globals()["input"] = fill_input(inputs, allow_overflow)

    def _print(*args, **kwargs):
        kwargs.update({"file": file})
        PRINT(*args, **kwargs)

    globals()["print"] = lambda *args, **kwargs: _print(*args, **kwargs)

    try:
        result = f()
    except KeyboardInterrupt:
        PRINT("\n", "[#] So you have decided to kill...")
        PRINT("\n", "Just in case, this information may be handy: ")
        PRINT("%s" % repr(f.__dict__))
        raise
    except Exception as e:
        return PRINT("\n",
                     "[!] Can't grade as %s is broken..." % f.__name__,
                     "\n", "Before its death, it said...",
                     "\n", "%s" % repr(e)) or NotImplementedError
    
    finally:
        del globals()["input"]
        del globals()["print"]
    
    return result

def run_function_pretest(f_name, test, silent = False):
    if globals().get(f_name, None) is None:
        return silent or print("[X] Couldn't find %s..." % f_name) or False
    
    f = globals().get(f_name)
    if test.get("args", tuple()) != \
       f.__code__.co_varnames[:len(test.get("args", tuple()))]:
        return silent or print(
            "[X] %s is accepting strange things..." % f_name) or False
    
    return True

def run_function_test(f, test, silent = False):
    args, kwargs = test.get("args", tuple()), test.get("kwargs", {})
    inputs, writable = test.get("inputs", tuple()), Writable()
    
    return_ = trap_io_and_run(lambda: f(*args, **kwargs), inputs, writable, False)
    if return_ == NotImplementedError:
        return False

    if (return_ != test.get("return", None)):
        expected = repr(test.get("return", None))
        expected_type = type(test.get("return", None)).__name__
        got, got_type = repr(return_), type(return_).__name__
        return silent or print("\n",
                     "[X] Expecting %s (%s)," % (expected, expected_type),
                     "\n", "but got %s (%s)..." % (got, got_type)) or False

    if (writable.body != test.get("output", "")):
        expected_lines = test.get("output", "").split("\n")
        got_lines = writable.body.split("\n")
        max_line_number = max(map(len, (expected_lines, got_lines)))
        max_line_number_len = len(str(max_line_number))
        longest_expected_len = max(map(len, expected_lines))

        line_formatter = "%%%ii|" % max_line_number_len
        expected_formatter = "%%-%is|" % longest_expected_len
        got_formatter = "%s"
        actual_formatter = line_formatter + expected_formatter + got_formatter
        
        silent or print("[X] The output looks a bit strange... Take a look. *")
        for line in range(max_line_number):
            expected_line = "" if line >= len(expected_lines) else expected_lines[line]
            got_line = "" if line >= len(got_lines) else got_lines[line]
            ref_line = (actual_formatter % (line + 1, expected_line, got_line))
            ref_line = ref_line + "\t[+]" if line >= len(expected_lines) else ref_line
            ref_line = ref_line + "\t[X]" if expected_line != got_line else ref_line
            silent or print(ref_line)
        return False
    
    return True

def run_function_tests(f, tests, silent=False):
    for test in tests:
        if not run_function_test(f, test, silent):
            return False
    return True

# (?) Before continuing...
"""
    You should have read Book 1 before continuing,
    as that book contains important fundamentals.

    The AIT ID of that book is D-EJ-ORG-OSP-201
    (EJI Nia, 0.0.5).

    Check if you have the prerequisites met with this checklist.
"""
BOOK_1_CHECKLIST = \
[
    [_], "IPO - Input, Process, Output Cycle",
    [_], ("How to get user input", input),
    [_], ("How to get program output", print),
    [_], {"Knowing these": [None, str, int, bool and list]},
    [_], "Variables and knowing how to assign and modify them",
]

# a. Instructions for using this book
"""
    This book is designed to be opened in IDLE running Python 3.7+,
    with a monospace font, with Tab Size = 4 (\t = 4 * " "),
    and a screen width of at least 73 characters.
"""

# -- To check for tab size and monospace, check if ↓ and ↑ matches.
#   ↓iIl1{';↓           Also, If you can't distinguish the first
#   ↑       ↑           4 characters, you should use another font.
# -- Finally, if you can see the end symbol, your window is wide enough. @

"""
    This book is an actual program that could be run.
    If you are experiencing SyntaxError-s, you might have removed
    or added something that you shouldn't have.
    
    Replace that section with the original and try again.
"""

# b. Page formatting used in this book
"""
    #       *       +       This is a new page.
    # ...                   This is the end of a page.
    
    # ↓                     If you see these arrows, you should
    # ↑                     type within these arrows.
                            
    _                       This is a placeholder where you should
                            replace it with your answer.
    
    Fire? ▌Sure.            What comes after the little block ▌
                            are simulated user inputs.
                            For example, simulating user entered "Sure".
"""

# -- Have fun playing around with the book!

# ...



#       *       *       *       *       *       *       *       *       +
# 5. Functions - "Learn to boil yourself, pot!"
print("\n", "Section 5 - Functions")
#       *       *       *       *       *       *       *       *       +

"""
    There are many appliances in a kitchen - stoves, pots, mixers... 
    They are here to help us do our jobs, while being fully reusable.

    The equivalent in programs are functions,
    and they have A LOT in common...
    basically use them like how you would use a pot!
    
    Let's see an example - see if you could spot their similarities.
"""

# 5.1. Function Demo
print("Section 5.0 - Function Demo")

random_desk = "This is some garbage in the kitchen"

# -↓- The "Slice Equal Pieces" Chopping Board -↓- #

# They have a name      and specific inputs...
def slice_equal_pieces(flat_list, piece_size):
    random_desk = []    # They work "contained"...
    
    for start_index in range(0, len(flat_list), piece_size):
        start, stop = start_index, start_index + piece_size
        random_desk.append(flat_list[start:stop])
    
    return random_desk  # They could "return" something processed,
                        # without burning themselves...
                
# -↑- The "Slice Equal Pieces" Chopping Board -↑- #

# -- When we use it...
LONG_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("slice_equal_pieces(LONG_LIST, 2)\n",
      slice_equal_pieces(LONG_LIST, 2))     #   ↰ 
print("slice_equal_pieces(LONG_LIST, 4)\n", # They are reusable
      slice_equal_pieces(LONG_LIST, 4))     #   ↲

print("random_desk\n",  # and they work without touching anything outside
      random_desk)      # and making the kitchen dirty. (contained!)


"""
    In fact, functions are so useful that a lot of programs
    that we write today are functions that others could use.
    We call them Libraries (Library).

    Here is a good example - a "program" that people made
    with a lot of useful and reusable functions.
    
    [Underscore, @jashkenas and open-source contributors]
    - Project Homepage
        https://github.com/jashkenas/underscore
    - Code
        https://github.com/jashkenas/underscore/tree/master/modules
"""



# 5.2. Using a function
print("\n", "Section 5.2 - Using Functions")
"""
    Back to the boiling pot - how would you use it?
    Most likely, you'll throw things into the pot, wait a bit,
    until the pot throws something back to you.

    Same for functions. Really -
    You just throw your ingredients into the "pot" → (),
    and when it finishes, it will magically become the product...
    and if you have done maths - you are certainly familiar with it.

    Does this look familiar to you?
        cos( tan( 0 ) )
         |   | |  |
         |   | |  +-----------  Pot of Appliance 2
         |   | +--------------  Appliance 2
         |   +----------------  Pot of Appliance 1
         +--------------------  Appliance 1

    and when it runs... it runs from in, to out -
    while magically transforming itself to the product...
    like this.
        cos( tan( 0 ) ) → cos ( 0 ) → 1.0 (Final product, a float!)

    Finally becoming something that you could use or further process.
    You could   - put it on a plate (with the left arrow =),
                - throw it out (by doing nothing with it)...
                - put it on another appliance (by wrapping it...)
"""

"""
    Notice the colors when we are working with data types?
    They are also in fact Functions - which are used to
    convert one type to another.
    Try using them in the following exercise!
"""

# 5.2.1. Data Type Conversion
print("Section 5.2.1 - Type Conversion")

# -- As a starter, let's try using types as functions.
NUMBER_FROM_USER_INPUT = "2.1314"

# Q5.2.1
# Try changing the input string to a number format, then add 0.87 to it.
# ↓ Try it out on this line.

# ↑ It should only take 1 line. Don't go over here.

# --- Time to check your answers!
if NUMBER_FROM_USER_INPUT == 2.1314 + 0.87:
    print("[O] You did well!")
else:
    print("[X] Didn't quite got it, you are having a %r (%s)" %
          (NUMBER_FROM_USER_INPUT,
          NUMBER_FROM_USER_INPUT.__class__.__name__))
# -- and then... you know the drill. If not, go back to Book 1. or F5.

# ...


#       *       *       *       *       *       *       *       *       +
# 5. Functions - Cont.
#       *       *       *       *       *       *       *       *       +

# 5.3. Making your own function
print("\n", "Section 5.3 - Defining Functions")

"""
    Although there are a lot of pre-made functions,
    as engineers, we usually have to make our own.
    Let's try it out!
"""

# -- Let's make our own function!

# --- Step 1. Make the case.
"""
    The first line of every function tells you everything
    about it... Just like the text on the appliance's case.
"""

# It has three parts...
#
# +------------- 1. "def", short for "define"
# |  +---------- 2. The function's name (that you will refer to later)
# |  |      +-------+--- 3. A list of things that you want it to take.
# |  |      |       |
def mixer(ingr1, ingr2):


# --- 2. Fill it with Dark Magic ™.
    """
    To be honest, you won't be reading this again after
    you have gotten it work. You can even hide this.
    It is really Dark Magic™.
    
    But this is where you'll tell it what and how it should work.
    Just write it like you're writing a new program. But --

    They are supposed to be contained.    
    To prevent it from touching things that it shouldn't,
    we will put a little "AT Field" gap on its contents (at the start),
    which we call "Indent (v, n)" or "Indentation (n)".
    
    In Python, the standard is 4 spaces. [    ] ← this much
    
    You can also use other gaps sizes like 3 or 2,
    but keep it consistent across the WHOLE FILE,
    or the computer will not take it. (OCD at its finest.)
    """
# ↙ This is the gap that we're talking about.
    return ingr1 + ingr2
    # Finally, when you are done processing,
    # return something back with the "return" keyword.
    # The pot will basically shut down at this point.


# --- 3. Profit!

# Q5.3.1 Function Declaration
print("Section 5.3.1 - Function Declaration")

"""
    Now, it's your time to finally make something.
        0. Try making the "ask_int" function,
        1. that gets a "prompt",
        2. Wait for the user to "input" a number with the "prompt",
        3. and return an "int"eger number.
    Hint: 0-1 is 1 line only, 2-3 are within 4 lines.
"""

# ↓ Try it out. It should not take more than 5 lines. ↓





# ↑ You shouldn't go across here. ↑

# --- Time to check your answers! ---
if not run_function_pretest("ask_int", {"args": ("prompt", )}):
    print("\n", "[X] The first line isn't going quite well. Try again!")
else:
    print("[i] Nice work on casing! Moving on...")
    if not run_function_tests(ask_int, (
        {"args": ("How old are you?", ), "inputs": ("16", ),
         "output": "How old are you?▌16\n", "return": 16},

        {"args": ("What do you think you are?", ), "inputs": ("0", ),
         "output": "What do you think you are?▌0\n", "return": 0},
    )):
        print("\n", "[X] Something is off. Try again!")
    else:
        print("[O] As intended. Well done!")
# --- As usual.

#...



#       *       *       *       *       *       *       *       *       +
# 6. IFTTT! E-L-S-E! - Control Flow Chants
print("\n", "Section 6 - Control Flow")
#       *       *       *       *       *       *       *       *       +

"""
    "Cogito, ergo sum" - "I think, therefore I am."
    Choosing where to eat, what to eat, how to order...
    Life is full of decisions - our invaluable skill.
    
    Same for every program - The value of it lies in its decision-making.

    How does a program decides what to do next?
    It all lies under a simple chant:
    "IFTTT! E-L-S-E!", or
    "IF This Then That, Else".
"""

# 6.1. Demostrating the IFTTT flow
print("Section 6.1 - If Condition Demo")

# It is very similiar to writing a function that runs under a condition -
# Take a look:
#               We use 2 = s because 1 = is a ← for plates.
#           ↙   Only in pairs, we have true equality. 
if 1 + 1 == 3:
    print("1 + 1 == 3 q.e.d.")
# ↖ Just like functions, we need the "AT Field Gap" to contain those

# ↙ elif is the short form of "el"se "if"
elif 2 + 2 == 4 and 4 - 1 == 3:
    print("2 + 2 == 4, - 1 that's 3 quick maths!")

else:       # You almost ALWAYS have to complete the story with else -
    pass    # but if you have nothing to say, just "pass".


# There wasn't really much to say, so let's try it out!

# Q6.2 - If Condition
print("\n", "Section 6.2. - If Condition")

# You will need these in this exercise:

("A") in ("B")
# which will return a bool (True / False) if A is in B's collection.
# For example -
1 in [1, 2, 3, "daisuki"] is True#, while
4 in [1, 2, 3, "daisuki"] is False#.

len( ("B") )
# which is a function, returning the "len"gth of a collection.
# For example -
len([1, 2, 3, "daisuki"]) == 4#.


"""
    For this exercise:
    0. Try making the "allow_i" function,
    1. that accepts a "chosen" collection, and two ints "i" and "n".

    2. The function should return   True if "i" is allowed,
                                    False if "i" is not allowed,
                                    None if no more "i"s can be chosen.

    You can think about this yourself, or follow along -
    2a. if "chosen" already has "n" or more numbers: return None.
    2b. else if "i" is in "chosen": return False.
    2c. else: return True!
"""

# ↓ Try it out. It should not take more than 10 lines. ↓











# ↑ You shouldn't go across here. ↑

# --- Time to check your answers! ---
if not run_function_pretest("allow_i", {"args": ("chosen", "i", "n")}):
    print("\n", "[X] The first line isn't going quite well. Try again!")
else:
    print("[i] Nice declaration! Moving on...")
    if not run_function_tests(allow_i, (
        {"args": ([1, 2, 3], 4, 5), "return": True},
        {"args": (["w", "t", "f"], "f", 5), "return": False},
        {"args": ([1, 2], 2, 2), "return": None},
    )):
        print("\n", "Something is off. Try again!")
    else:
        print("[O] Nice decision! Well done!")
# --- As usual.

#...



#       *       *       *       *       *       *       *       *       +
# 7. Yume kara takusan mita! - Loops
print("\n", "Section 7 - Loops")
#       *       *       *       *       *       *       *       *       +
"""
    Kitchen work is mundane... like chopping...
    you keep doing the same things...
    ...until it is completed.
    Some work is pure brainless work.
    and brainless work ought to be brainless - as well!

    Here is where loops come into play -
    Repeating the same work, without writing more.
"""

# -- There are mainly two main types of loops -

# 7.1.1 While loops
# --- which are pretty self-explanatory...
print("Section 7.1.1 - While Loop Demo")
CHOPS_REMAINING = 3

while CHOPS_REMAINING >= 1 or True: # Give it a condition...
    print("CHOP!")  # Do brainless work...
    CHOPS_REMAINING = CHOPS_REMAINING - 1
    if CHOPS_REMAINING < 1:
        break       # If you need a break, just do "break".
    # ↖ This "AT Field Gap" is for the inner "if pot".
# ↖ The "AT Field Gap" is for the outer "while pot".

print("Chopped~!")

# Let's try it out!

# Q7.1.2. - While Loop
print("\n", "Section 7.1.2 - While loop")

"""
    For this exercise:
    0. Try making the "ask_list" function,
    1. Which will keep asking for name "input"s, (Hint: while...)
    2. Until an empty line "" is found. (Hint: take a break afterwards.)
    
    3. Finally, return a list of names.
"""

"""
    [!] Caution -
    Sometimes you might forget to let the chef off,
    and the program will just be stuck...
    When that happens, press Ctrl-C on your keyboard to force a day off,
    or close the window and "kill the shell". (That hurts)
"""

# ↓ Try it out. It should not take more than 10 lines. ↓









# ↑ You shouldn't go across here. ↑

# --- Time to check your answers! ---
if not run_function_pretest("ask_list", {"args": ()}):
    print("\n", "[X] The first line isn't going quite well. Try again!")
else:
    print("[i] Nice declaration! Moving on...")
    if not run_function_tests(ask_list, (
        {"inputs": ["Taka", ""],
         "output": "\n".join(["▌Taka", "▌", ""]),
         "return": ["Taka"]},
        {"inputs": ["Nia", "Morkilo", "Demonio", ""],
         "output": "\n".join(["▌Nia", "▌Morkilo", "▌Demonio", "▌", ""]),
         "return": ["Nia", "Morkilo", "Demonio"]},
    )):
        print("\n", "Something is off. Try again!")
    else:
        print("[O] Chop chop chop... Well done!")
# --- As usual.

# ...



#       *       *       *       *       *       *       *       *       +
# 7. Loops - Cont.
#       *       *       *       *       *       *       *       *       +

# 7.2 For loops
"""
    Remembered lists? They looked like [1, 2, 3], like things laid
    on a LOOOOOOOOONG table, which we could visit one by one.
    
    Can we transform work that we need to do on each of them
    into Brainless Work™ ?

    Sure we can - here is where the for loop comes into play.
"""

# But first, let's see how do we privately meet a table member.
DINNER_TABLE = ["Morkilo", "Nia", "Momoko", "Demonio"]

# As we are working with tables, we shall also visit in "table" form,
# as in [] square brackets. (You can use this on all collections!)
# and... computers count from 0, so the first member is Number 0 (cry).

# Q7.2.1. Pay a private visit to Nia
print("\n", "Section 7.2.1. List member access")

(lambda a:
 print("[O] You found me ><!") if a == "Nia" \
 else print("[X] I'm missed...")    
)(
# Try visiting me by "table manners"!
# ↓ Try it out on this line.
_
# ↑ It should only take 1 line. Don't go over here.
)


# 7.2.2. Paying visits to the whole table.
print("\n", "Section 7.2.1. For loop Demo")
"""
    Now, let's move on to visiting the whole table.
    For each member in the table,
    We will say "Have a nice meal" to them.

    Writing it as a program is just like writing it out as a sentence...
    like this -
"""
for member in DINNER_TABLE:
    print("Have a nice meal,", member)


# -- Internally, these are the same.
# --        ↓ Change this to True if you wish to compare.
@run_iife(  _   , DINNER_TABLE)
def for_loop_internals(DINNER_TABLE):
    print("- ↓ Ran from for_loop_internals ↓ -")
    i = 0   # a visitor helps you to do your work...
    while i < len(DINNER_TABLE):
        member = DINNER_TABLE[i] # and putting it in the name book.
        print("Have a nice meal,", member)
        i = i + 1


# Let's try it out!

# Q7.2.2 - For loop
print("\n", "Section 7.2.2. For loop")

"""
    For this exercise:
    0. Try making the "print_list" function,
    1. Which accepts a "list" of "names",
    2. and "prints" each name on a new line.
"""

# ↓ Try it out. It should not take more than 5 lines. ↓





# ↑ You shouldn't go across here. ↑

# --- Time to check your answers! ---
if not run_function_pretest("print_list", {"args": ("names", )}):
    print("\n", "[X] The first line isn't going quite well. Try again!")
else:
    print("[i] Nice declaration! Moving on...")
    if not run_function_tests(print_list, (
        {"args": (tuple(DINNER_TABLE), ),
         "output": "\n".join([*DINNER_TABLE, ""]),

         "args": ("Strange table",),
         "output": "\n".join([*"Strange table", ""]),
         },
    )):
        print("\n", "Something is off. Try again!")
    else:
        print("[O] Bon appetite! Well done!")
# ---


#...



#       *       *       *       *       *       *       *       *       +
# 8. Getting external help - Imports
print("\n", "Section 8 - Imports")
#       *       *       *       *       *       *       *       *       +

"""
    We shall join together to fight against the Unbread!
    Let us ride on the shoulders of the giants
    and (freeride and not) work towards our common goal.

    There are a lot of common tasks that we have worked on too often
    and was too lazy to type it out again,
    or just that the problems are too hard for us to solve.

    Here is when imports really shines.
    Import is like hiring a highly-trained superman to work for you.

    Remember Libraries? This is how we use them.
"""

# 8.1 But first, let's talk about name issues...
print("\n", "Section 8.1 - Object Member Access")
"""
    In AIT, every operator has its own base.
    Although we could work basically anywhere across the AIT Network,
    it is still very useful to refer to them by their bases.

    For example,
    (EJI) Nia from Lab Origin and (KOTOHA) Nia from Lab Laurel
    might not be the same guy. Same with Ms Salmons.

    To refer to them (and prevent conflicts), we use . "dots",
    just like 2 people, holding hands - ඞ.ඞ among us
    or dotted chapter numbers in this book -
    1.2.3 (Section 1, Part 2, Item 3).

    Maybe sometime, we would end up like (me.you) (just kidding.)
"""

# Q8.1.1 Member access
print("\n", "Section 8.1.1. List member access")

(lambda a:
 print("[O] __class__: Cool! How may I help?") if a == "str" \
 else print("[X] Says who...?")    
)(
# Try accessing "__name__" under the "str" company!
# ↓ Try it out on this line.
_
# ↑ It should only take 1 line. Don't go over here.
)


# 8.2 Time to hire! Employment methods
print("\n", "Section 8.2 - Import Modes Demo")
# --- There are quite a few import modes that you could adopt...

# --- 1. Borrow from the Network
import time     # This will borrow people from the "time" company
                # without changing their base labs...

# then you could do something like this:
print(time.ctime()) # Ask the "ctime" guy to work for you.

# ---

# --- 2. I want you - Pull from another Lab
from time import asctime    # This will hire that "asctime" guy
                            # from the "time" company,
                            # while changing base labs (not returning!)

# then you could do something like this:
print(asctime())    # as it is already a part of your lab,
                    # the lab prefix is no longer required.

# ---

# --- 3. COMPANY ACQUISITION - I WANT ALL OF IT!
from copy import *      # This will get everyone in the "copy" company
                        # to only work for you ever again.

# then you could do something like this:
print(deepcopy([1, 3, 4]))  # You didn't even know
                            # this guy has ever existed, eh?
                            # so be very careful before you acquire!

# [!]   This will replace everyone in your company in the same name,
#       so use with caution!
# ---

# Now, its your time to be the big boss.

print("\n", "Section 8.2.1 - Fresh hire")
# Try hiring the "randrange" guy from the "random" company,
# while changing his base lab.
# ↓ Try it out on this line.

# ↑ It should only take 1 line. Don't go over here.

# --- HR Checks (Answer Checker) ---
try:
    randrange(1)
except NameError:
    print("[X] That guy still isn't a part of us...")
else:
    print("[O] Welcome to our family, randrange!")
# --- This is our final part of the tutorial!
# --- Here comes the final test!

# ...



#       *       *       *       *       *       *       *       *       +
# 9. Grand Opening
print("\n", "Section 9 - Final Product")
#       *       *       *       *       *       *       *       *       +
# allow_i, ask_int, ask_list, print_list, randrange

"""
    You have gone so far til here.
    You have acquired everything you need to complete this masterpiece.
    It is time... Time for... ALL ASSEMBLE.
"""

READY_FOR_FINALS = (
    lambda a: print("[O] Seems like you are all set.") if all(a) \
    else print("[X] There are still some steps to make...") or all(a))((
# What you have done so far...
        
        # Q5.3: ask_int: Asks for an integer input
        run_function_pretest("ask_int", {"args": ("prompt", )}),
        
        # Q6.2: allow_i: Check if Member i should be chosen
        run_function_pretest("allow_i", {"args": ("chosen", "i", "n")}),

        # Q7.1.2 ask_list: Asks for a list of strings
        run_function_pretest("ask_list", {"args": ()}),

        # Q7.2.2 print_list: Prints a list of strings
        run_function_pretest("print_list", {"args": ("names", )})
    ))

# Also, external hires...
# Q8.2.1 randrange(N): Generates an integer between 0 and N - 1
# For example:
# (0 >= randrange(5) >= 4) is True

# range(N): Generates a list between 0 and N - 1
# For example:
list(range(4)) == [0, 1, 2, 3]


# Now. It is your time to shine.
"""
    For the final test...
    0. Make the "random_names_i" function,
    1. Get user to input a list of names, ending with an empty line,
    2. Prompt with "(N = ?) " to ask for the number of people to generate,
    3. Randomly choose from the name list from #1,
    4. then finally, print all the selected names.

    Hint 1: You should use all the functions above at least once.
    Hint 2: You might need to make these "plates" yourself:
            names, n, s, chosen_names, i, i_s, should_select.
"""

# ↓ All on you. It should not take more than 30 lines. ↓

























# ↑ You shouldn't go across here. ↑

# This will not be automatically graded - when you are ready,
# ↓ run your own function on this line. ↓
_
# ↑ ↑

# --- For the last time, please [F5], save and run.

# ...



#       *       *       *       *       *       *       *       *       +
# Book 2 Overview
#       *       *       *       *       *       *       *       *       +
"""
    This is the end of Book 2, and our endearing programming journey.
    Thanks for paying the time to work through this book!

    You should have acquired most knowledge to write short programs.
    If you are interested, feel free search for more resources online.

    From the Author

    I had a lot of fun writing this book, and I hope this would be
    a future manual, and a fun manual for newcomers interested.
    It was a very hard and hacky writing graders within the same file -
    and I have learnt a lot too - (especially the nonlocal keyword.)

    Thank you - and
    Until next time...
"""

print("--- End of Book 2 ---")
# ...

# This is my solution, by the way.
from random import sample
_s = lambda: print("\n".join(sample(list(iter(input, "")), int(input()))))
# run it with _s().

if run_function_pretest("random_names_i", {"args": ()}, silent=True) and \
   run_function_tests(globals().get("random_names_i", lambda: None), ({
       "inputs": ["You", "", "1"],
       "output": "\n".join(
           ["▌You", "▌", "(N = ?) ▌1", "You", ""])}, ), silent=True):
    print("\n\n", "--- Thanks for       ---")
    print("\n", "You have completed the final test!")
    print("\n", "---     Playing!     ---")
