from turtle import Turtle, Screen
import random

#Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_Positions = [(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_Positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_on = True
while game_on:
    for seg in new_segment:
        seg.forward(20)












screen.exitonclick()