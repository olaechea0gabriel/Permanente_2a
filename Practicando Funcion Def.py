

total= int(input("Ingrese el Puntaje Máximo"))



from ctypes import alignment
from decimal import DivisionImpossible
from re import X
from tkinter import CENTER, Y
import turtle

#Ventana
screen= turtle.Screen()
screen.title("PingPong")
screen.bgcolor("white")
screen.setup(width=1000, height=700)
screen.tracer(0)

#MARCADOR
marcador1=0
marcador2=0

#JUGADOR A
jugador_a= turtle.Turtle()
jugador_a.speed(0)
jugador_a.shape("square")
jugador_a.color("black")
jugador_a.penup()
jugador_a.goto(-450,0)
jugador_a.shapesize(stretch_wid=5, stretch_len=1)

#JUGADOR B
jugador_b=turtle.Turtle()
jugador_b.speed(0)
jugador_b.shape("square")
jugador_b.color("black")
jugador_b.penup()
jugador_b.goto(450,0)
jugador_b.shapesize(stretch_wid=5, stretch_len=1)

#PELOTA
pelota=turtle.Turtle()
pelota.speed(-10)
pelota.shape("square")
pelota.color("red")
pelota.penup()
pelota.goto(0,0)
pelota.dx=2
pelota.dy=2

#CANCHA
division= turtle.Turtle()
division.color("blue")
division.goto(0,500)
division.goto(0,-500)
division.goto(1,500)
division.goto(1,-500)
division.goto(2,500)
division.goto(-2,-500)
division.goto(3,500)
division.goto(-3,-500)
#PEN
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador 1: {}     Jugador 2:  {} ".format(marcador1,marcador2), align = "center", font=("Times New Roman",30, "normal"))


#FUNCIONES JUEGO
def jugador_a_RIGHT():
    x= jugador_a.xcor()
    x+=20
    jugador_a.setx(x)

def jugador_a_LEFT():
    x=jugador_a.xcor()
    x-=20
    jugador_a.setx(x)

def jugador_a_UP():
    y= jugador_a.ycor()
    y+=20
    jugador_a.sety(y)

def jugador_a_DOWN():
    y= jugador_a.ycor()
    y-=20
    jugador_a.sety(y)

def jugador_b_UP():
    y= jugador_b.ycor()
    y+=20
    jugador_b.sety(y)

def jugador_b_DOWN():
    y= jugador_b.ycor()
    y-=20
    jugador_b.sety(y)

#def jugador_a_CLOSE():
    

#TECLADO
screen.listen()
screen.onkeypress(jugador_a_RIGHT, "d"or"D")
screen.onkeypress(jugador_a_LEFT, "a"or "A")
screen.onkeypress(jugador_a_UP, "w"or"W")
screen.onkeypress(jugador_a_DOWN, "s"or"S")
screen.onkeypress(jugador_b_UP, "Up")
screen.onkeypress(jugador_b_DOWN, "Down")
#screen.onkeypress(jua)

while True:
    screen.update()

    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)

    #EXTREMOS DEL JUEGO ARRIBA, ABAJO
    if pelota.ycor()>340:
        pelota.dy *= -1
    if pelota.ycor()<-340:
        pelota.dy *= -1
    
    
    #EXTREMOS IZQUIERDA Y DERECHA
    if  pelota.xcor()>490:
        pelota.goto(0,0)
        pelota.dy *= -1
        marcador1 += 1
        pen.clear()
        pen.write("Jugador 1: {}        Jugador 2:  {}".format(marcador1, marcador2), align="center",font=("Times New Roman", 30,"normal"))

    if pelota.xcor()<-490:
        pelota.goto(0,0)
        pelota.dy *= -1
        marcador2 += 1
        pen.clear()
        pen.write("Jugador 1: {}        Jugador 2:  {}".format(marcador1, marcador2), align="center",font=("Times New Roman", 30,"normal"))
        
#REBOTES EN LOS PALOS

    if ((pelota.xcor()>440 and pelota.xcor()<450)
            and(pelota.ycor()<jugador_b.ycor()+50
            and pelota.ycor()>jugador_b.ycor()-50)):
        pelota.dx *=-1

    if ((pelota.xcor()<-440 and pelota.xcor()>-450)
            and(pelota.ycor()<jugador_a.ycor()+50
            and pelota.ycor()>jugador_a.ycor()-50)):
        pelota.dx *=-1
#LIMITES UP AND DOWN
    if jugador_a.ycor()>300:
        jugador_a.goto(-450,300)
    if jugador_a.ycor()<-300:
        jugador_a.goto(-450,-300)

    if jugador_b.ycor()>300:
        jugador_b.goto(450,300)
    if jugador_b.ycor()<-300:
        jugador_b.goto(450,-300)
    
    #GANO JUGADOR 1 ACABA JUEGO
    
    if marcador1 >= total:
        pen.clear()
        pelota.goto(0,0)
        pelota.dx=0
        pelota.dy=0
        pen.write("Ganó jugador 1 por {} puntos ".format(marcador1),align="center",font=("Times New Roman", 35, "normal"))

    #GANA JUGADOR 2 ACABA JUEGO
    
    if marcador2 >= total:
        pen.clear()
        pelota.goto(0,0)
        pelota.dx=0
        pelota.dy=0
        pen.write("Ganó jugador 2 por {} puntos ".format(marcador2),align="center",font=("Times New Roman", 35, "normal"))

        
        #pen.write("GANÓ JUGADOR 1", format.marcador1)
            #elif
    
    #if jugador_a_RIGHT:
    #    break
