import turtle
from colorsys import hsv_to_rgb

rules = {
    "F":"F-H",
    "H":"F+H"
}

actions = {
    "-": turtle.right,
    "+": turtle.left
}

stretch = 5
max_path_size = 100000
colors = ["red", "blue", "green", "yellow", "brown", "pink"]

starting_chain = ["F", "-", "H"]

def make_new_chain(temp):
    if len(temp) > max_path_size:
        return temp
    new_chain = []
    for elem in temp:
        if elem in rules:
            new_chain.extend(rules[elem])
        else:
            new_chain.extend(elem)
    return make_new_chain(new_chain)

chain = make_new_chain(starting_chain)

turtle.ht()
turtle.penup()
turtle.goto(150, -150)
turtle.pendown()
turtle.speed("fastest")
turtle.forward(stretch)

for i, char in enumerate(chain):
    turtle.color(hsv_to_rgb(i/max_path_size*10, 0.75, 0.75))
    if char in actions:
        actions[char](90)
        turtle.forward(stretch)


