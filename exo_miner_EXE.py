import turtle
import random
import time
import tkinter as tk

screen = turtle.Screen()
screen.setup(700, 500)
screen.title("EXO-MINER-Lite")
screen.bgpic('img/main_img.gif')
head= turtle.Turtle()
head.hideturtle()
head.penup()
head.color("white")
head.setpos(-152,150)
head.write('Ｅ Ｘ Ｏ      Ｍ Ｉ Ｎ Ｅ Ｒ',font=("Arial", 20, "bold"))

with open("high", "r") as f:
    high_score = f.read()
high = turtle.Turtle()
high.hideturtle()
high.penup()
high.color("white")
high.setpos(-340, 210)
high.write(f"Highest Mined: {high_score}", font=("Arial", 10, "bold"))

menu = turtle.Turtle()
menu.hideturtle()
menu.penup()
menu.color("white")
menu.setpos(-120, -215)
menu.write(f"                         START\nTask : Mine as much rock as possible\n                      ESC - EXIT", font=("Arial", 11, "bold"))

copy_right = turtle.Turtle()
copy_right.hideturtle()
copy_right.penup()
copy_right.color("white")
copy_right.setpos(280, -240)
copy_right.write('@RikuZavi', font=('Arial',9,'bold'))

b=10
s=0
a=0
c='❤❤❤❤❤❤'
def START():
    global b,head,s,a
    head.clear()
    head.hideturtle()
    menu.clear()
    menu.hideturtle()
    screen.bgpic('img/star.gif')
    p=turtle.Screen()
    p.addshape('img/ship.gif')
    player = turtle.Turtle()
    player.hideturtle()
    player.penup()
    player.setheading(90)
    player.shape('img/ship.gif')
    player.shapesize(1, 1, 0)
    player.setposition(0,-220)
    player.color('red')
    player.showturtle()

    w = turtle.Screen()
    w.addshape('img/rock.gif')
    enemy = turtle.Turtle()
    enemy.hideturtle()
    enemy.shape("img/rock.gif")
    enemy.shapesize(2, 2, 0)
    enemy.color("white")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(random.randint(-330, 330), 230)
    enemy.showturtle()

    bullet = turtle.Turtle()
    bullet.hideturtle()
    bullet.shape('square')
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.setposition(-240,-232)
    bullet.shapesize(0.5, 0.1, 0)
    bullet.showturtle()

    bullet_count= turtle.Turtle()
    bullet_count.hideturtle()
    bullet_count.penup()
    bullet_count.color("white")
    bullet_count.setpos(-345, -240)
    bullet_count.write(f"Bullets Left :{b}",font=("Arial", 10, "bold"))

    score_count = turtle.Turtle()
    score_count.hideturtle()
    score_count.penup()
    score_count.color("white")
    score_count.setpos(205, 225)
    score_count.write(f"MINING SCORE :{s}", font=("Arial", 10, "bold"))

    health = turtle.Turtle()
    health.hideturtle()
    health.penup()
    health.color("red")
    health.setpos(-345, 225)
    health.write(f"{c}", font=("Arial", 18, "bold"))


    def update_score():
        global high_score
        score_count.clear()
        score_count.write(f"MINING SCORE :{s}", font=("Arial", 10, "bold"))
        if s > int(high_score):
            high_score = s
            high.clear()
            high.write(f"Highest Mined: {high_score}", font=("Arial", 10, "bold"))
            with open("high", "w") as fr:
                fr.write(str(high_score))

    def update_health():
        global a,c
        a += 1
        H=c[:-a]
        health.clear()
        health.write(f"{H}", font=("Arial", 18, "bold"))
        if H=='':
            game_over_health()
    def fire():
        global b
        b-=1
        bullet_count.clear()
        bullet_count.write(f"Bullets Left :{b}",font=("Arial", 9, "bold"))
        bullet.goto(player.xcor(), player.ycor())
        if bullet.ycor() <= 300:
            for i in range(20):
                bullet.goto(bullet.xcor(),bullet.ycor()+30)
        if b<=0:
            game_over_bullet()

    def move_right():
        if player.xcor()<=320:
            player.setx(player.xcor()+20)
    def move_left():
        if player.xcor()>=-330:
            player.setx(player.xcor()-20)

    def move_enemy():
        global b,s
        speed=6
        if s>=30:
            speed=7.5
        if s>=40:
            speed=9
        if s>=50:
            speed=10
        if enemy.ycor() > -300 :
            enemy.goto(enemy.xcor(), enemy.ycor() - speed)
            if enemy.distance(bullet) <= 38:
                enemy.setposition(random.randint(-330, 330), 250)
                b += 1
                s += 1
                update_score()
            if enemy.distance(player)<=35:
                enemy.setposition(random.randint(-330, 330), 250)
                update_health()
        else:
            enemy.setposition(random.randint(-330, 330), 250)
        screen.ontimer(move_enemy, 15)
    move_enemy()

    def game_over_bullet():
        global head
        screen.onkey(None,'space')
        screen.onkey(None, "space")
        player.hideturtle()
        enemy.hideturtle()
        head.clear()
        head.setposition(-120,0)
        head.write(f"Bullets Left : {0}\nGAME OVER\nPress ESC to Exit and RERUN the program", font=("Arial", 13, "bold"))
        head.hideturtle()
        head.hideturtle()
        screen.onkey(exit,"Escape")
    def game_over_health():
        global head
        screen.onkey(None, 'space')
        screen.onkey(None, "space")
        player.hideturtle()
        enemy.hideturtle()
        head.clear()
        head.setposition(-120, 0)
        head.write(f"Heath : 0, SPACE SHIP DESTROYED\nGAME OVER\nPress ESC to Exit and RERUN the program",font=("Arial", 13, "bold"))
        head.hideturtle()
        head.hideturtle()
        screen.onkey(exit, "Escape")

    screen.onkeypress(move_right,"Right")
    screen.onkeypress(move_left, "Left")
    screen.onkey(fire, "space")
    screen.listen()

screen.onkeypress(START,"Return")
screen.onkey(exit,"Escape")
screen.listen()
screen.mainloop()
