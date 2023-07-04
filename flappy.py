import turtle as t
import random
import keyboard
import time
t.penup()
t.lt(180)
t.fd(700)
t.lt(90)
t.fd(300)
t.lt(90)
t.pendown()
lst = list()
height = 600
height_bird = 60
def pipe(h,direction):
    if direction == "down":
        t.fd(50)
    t.lt(90)
    t.fd(h)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(h)
    t.lt(90)
    if direction == "up":
        t.fd(50)
for i in range(1,11):
    rand = int(random.random()*500)
    lst.append(rand)
    pipe(rand,"up")
t.penup()
t.lt(90)
t.fd(height)
t.lt(90)
t.pendown()
def pipedown(h):
    t.fd(h)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(h)
    t.penup()
    t.rt(90)
    t.fd(50)
    t.right(90)
    t.pendown()
for i in reversed(range(len(lst))):
    pipe(height - height_bird - lst[i],"down")
t.penup()
t.left(90)
t.fd(height/2)
t.left(90)
t.pendown()

def fall():
    y1 = 20
    transfare(y1/10,-y1)
    bird()

def bird():
    t.circle(10)
def transfare(x,y):
    t.penup()
    t.fd(x)
    if y > 0:
        t.lt(90)
    else:
        t.rt(90)
    t.fd(abs(y))
    if y > 0:
        t.rt(90)
    else:
        t.lt(90)
    t.pendown()
bird()
while True:
    print(keyboard.read_key())
    flag = True
    if keyboard.read_key() == "space":
        transfare(50,50)
        bird()
        flag = False
    if(flag):
        fall()
    time.sleep(1)


    

    

