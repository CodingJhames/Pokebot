import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Hello, Parchita!')

parchita = turtle.Turtle()
parchita.color('blue')
parchita.pensize(3)

parchita.forward(50)
parchita.left(120)
parchita.forward(50)

wn.mainloop()
