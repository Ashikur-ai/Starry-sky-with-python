import turtle as t
import random as r

# defining screen
win = t.getscreen()
win.bgcolor("black")

# defining turtle
rock = t.Turtle()
rock.color("yellow")
rock.speed(0)




# get random cordinate
for i in range(50):
    x = r.randint(-300, 300)
    y = r.randint(-300, 300)

    # Turtle up down and filling the color
    rock.begin_fill()
    rock.up()
    rock.goto(x, y)
    rock.down()
    for i in range(5):
        rock.fd(20)
        rock.lt(144)

    rock.end_fill()

# looping the screen
win.mainloop()