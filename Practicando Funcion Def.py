from ctypes import alignment
import turtle

#Ventana
wn= turtle.Screen()
wn.title("PingPong")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0)

#MARCADOR
marcador1=0
marcador2=0

#JUGADOR A
jugador_a= turtle.Turtle()
jugador_a.speed(0)
jugador_a.shape("square")
jugador_a.color("white")
jugador_a.penup()
jugador_a.goto(-450,0)
jugador_a.shapesize(stretch_wid=5, stretch_len=1)

#JUGADOR B
jugador_b=turtle.Turtle()
jugador_b.speed(0)
jugador_b.shape("square")
jugador_b.color("white")
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

#PEN
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador 1: {}     Jugador 2:  {} ".format(marcador1,marcador2), align = "center", font=("Times New Roman",30, "normal"))


#FUNCIONES JUEGO
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

#TECLADO
wn.listen()
wn.onkeypress(jugador_a_UP, "w"or"W")
wn.onkeypress(jugador_a_DOWN, "s"or"S")
wn.onkeypress(jugador_b_UP, "Up")
wn.onkeypress(jugador_b_DOWN, "Down")

while True:
    wn.update()

    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)

    #EXTREMOS DEL JUEGO ARRIBA, ABAJO
    if pelota.ycor()>289:
        pelota.dy *= -1
    if pelota.ycor()<-289:
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
        jugador_a.goto(-450,290)
    if jugador_a.ycor()<-300:
        jugador_a.goto(-450,-290)

    if jugador_b.ycor()>300:
        jugador_b.goto(450,290)
    if jugador_b.ycor()<-300:
        jugador_b.goto(450,-290)