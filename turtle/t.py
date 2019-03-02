
t = turtle.Turtle()
circle = turtle.Turtle()
for c in ['red', 'green', 'yellow', 'blue', 'pink', 'red', 'green', 'yellow', 'blue', 'pink']:
    t.color(c)
    t.forward(100)
    t.left(100)
    t.circle(120)
circle.right(100)    
circle.circle(50)


root.resizable(width = false, height = false)
