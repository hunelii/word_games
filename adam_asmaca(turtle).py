import turtle
from random_word import RandomWords

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("Hangman Game")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_gallows():
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.forward(200)
    pen.penup()
    pen.goto(0, -50)
    pen.left(90)
    pen.pendown()
    pen.forward(200)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)

def draw_head():
    pen.penup()
    pen.goto(74, 74)
    pen.pendown()
    pen.circle(25)

def draw_body():
    pen.penup()
    pen.goto(99, 49)
    pen.pendown()
    pen.forward(50)

def draw_left_arm():
    pen.penup()
    pen.goto(99, 40)
    pen.pendown()
    pen.left(40)
    pen.forward(40)

def draw_right_arm():
    pen.penup()
    pen.goto(99, 40)
    pen.pendown()
    pen.right(40)
    pen.forward(40)

def draw_left_leg():
    pen.penup()
    pen.goto(99, -1)
    pen.pendown()
    pen.left(45)
    pen.forward(40)

def draw_right_leg():
    pen.penup()
    pen.goto(99, -1)
    pen.pendown()
    pen.right(40)
    pen.forward(40)

def draw_hangman(attempts):
    if attempts == 1:
        draw_head()
    elif attempts == 2:
        draw_body()
    elif attempts == 3:
        draw_left_arm()
    elif attempts == 4:
        draw_right_arm()
    elif attempts == 5:
        draw_left_leg()
    elif attempts == 6:
        draw_right_leg()

def ciz(attempts):
    if attempts == 1:
        draw_head()
        draw_body()
        draw_left_arm()
        draw_right_arm()
        draw_left_leg()
        draw_right_leg()
    elif attempts == 2:
        draw_body()
        draw_left_arm()
        draw_right_arm()
        draw_left_leg()
        draw_right_leg()
    elif attempts == 3:
        draw_left_arm()
        draw_right_arm()
        draw_left_leg()
        draw_right_leg()
    elif attempts == 4:
        draw_right_arm()
        draw_left_leg()
        draw_right_leg()
    elif attempts == 5:
        draw_left_leg()
        draw_right_leg()
    elif attempts == 6:
        draw_right_leg()

# Get a random word
r = RandomWords()
rand_word = r.get_random_word()
while " " in rand_word:  # Ensure the word has no spaces
    rand_word = r.get_random_word()
array_rand_word = list(rand_word)
guessed_word = ["_"] * len(array_rand_word)
print(guessed_word)

current_attempts = 0
max_attempts = 6

# Draw the gallows
draw_gallows()

while current_attempts < max_attempts:
    print(" ".join(guessed_word))
    x = input("Enter a character: ").lower()
    
    found = False
    for i in range(len(array_rand_word)):
        if x == array_rand_word[i]:
            guessed_word[i] = x
            found = True
            
    if found:
        print("Correct!")
    else:
        print("Character not found in the word.")
        current_attempts += 1
        draw_hangman(current_attempts)
    
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", "".join(guessed_word))
        break

if "_" in guessed_word:
    ciz(current_attempts)
    print("Out of attempts. The word was:", "".join(array_rand_word))

# Close the turtle graphics window on click
screen.exitonclick()
