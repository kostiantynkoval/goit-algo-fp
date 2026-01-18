import turtle

def draw_pythagoras_tree(t, branch_len, level):
    if level == 0:
        return

    t.forward(branch_len)

    pos = t.pos()
    ang = t.heading()

    t.right(45)
    draw_pythagoras_tree(t, branch_len * 0.7, level - 1)

    t.penup()
    t.setposition(pos)
    t.setheading(ang)
    t.pendown()

    t.left(45)
    draw_pythagoras_tree(t, branch_len * 0.7, level - 1)

    t.penup()
    t.setposition(pos)
    t.setheading(ang)
    t.pendown()


def main():
    try:
        level = int(input("Please enter the level of the tree: "))
    except ValueError:
        print("Input must be an integer.")
        return

    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(1)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.color("navy")

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()