from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

name_list = {}

is_race_on = False

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Who will win the race?Enter a color: blue, pink,red, green, yellow, purple",
)


def create_players(name, list_of_names={}):
    # Assign the name as a key and create a turtle object as the value
    list_of_names[name] = Turtle(shape="turtle")

    # Use the turtle object to set penup
    list_of_names[name].penup()

    # print(f"check list of names: {list_of_names}")
    return list_of_names


# color list with total of 6
colors = ["blue", "pink", "red", "green", "yellow", "purple"]


def assign_colors(list_of_names):
    x = -230
    y = 100

    # Assign a color to each turtle object
    for name, turtle in list_of_names.items():
        color = random.choice(colors)
        turtle.color(color)  # turn the turtle object to the assigned color
        colors.remove(
            color
        )  # remove the assigned color from the list to avoid duplicates
        turtle.goto(x, y)
        y -= 40


create_players(name="daniel", list_of_names=name_list)
create_players(name="eliza", list_of_names=name_list)
create_players(name="mei", list_of_names=name_list)
create_players(name="ken", list_of_names=name_list)
create_players(name="tim", list_of_names=name_list)
create_players(name="tom", list_of_names=name_list)

assign_colors(name_list)


if user_bet:
    is_race_on = True

while is_race_on:
    for key, turtle in name_list.items():
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > (250 - (40 / 2)):
            is_race_on = False
            winner = turtle.pencolor()  # winner pencolor
            if user_bet == winner:  # check if the winner's color matches the user's bet
                print("Congratulations! You won the race!")
                print(f"You're input was {user_bet}, the winner's color is {winner}.")

            else:
                print("Sorry, you lost the race.")
                print(f"You're input was {user_bet}, the winner's color is {winner}.")

screen.exitonclick()
