from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
User_Bets = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race")
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle in range(0, 6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-200, y=y_position[turtle])
    all_turtles.append(new_turtle)

if User_Bets:
    is_race_on = True

while is_race_on:
    
    
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == User_Bets:
                print("You've won the {winning_color} turtle is the winner")
            else:
                print("You've lost the {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()