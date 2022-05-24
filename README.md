# Permanente_2a
Juego de Ping Pong Básico
from ctypes import alignment
import turtle

#Ventana-------------------------------------------------La ventana es el grafico donde se ejecutara el juego, el modulo turtle esta basado en el plano cartesiano
wn= turtle.Screen()
wn.title("PingPong")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0)

#MARCADOR-------------------------------Comienza en 0, luego se va sumando 1 segun quien meta un gol, en el modulo
marcador1=0
marcador2=0

#JUGADOR A---------------------------------------------Estas son las caracteristicas del Jugador 1, el Jugador 1 es igual al jugador a, en el modulo
jugador_a= turtle.Turtle()
jugador_a.speed(0)
jugador_a.shape("square")
jugador_a.color("white")
jugador_a.penup()
jugador_a.goto(-450,0)
jugador_a.shapesize(stretch_wid=5, stretch_len=1)

#JUGADOR B-------------------------------------------Estas son las caracteristicas del jugador 2, el jugador 2 es igual al jugador b, en el modulo
jugador_b=turtle.Turtle()
jugador_b.speed(0)
jugador_b.shape("square")
jugador_b.color("white")
jugador_b.penup()
jugador_b.goto(450,0)
jugador_b.shapesize(stretch_wid=5, stretch_len=1)

#PELOTA-----------------------------------------------Estas son las caracteristicas de la Pelota en el modulo
pelota=turtle.Turtle()
pelota.speed(-10)
pelota.shape("square")
pelota.color("red")
pelota.penup()
pelota.goto(0,0)
pelota.dx=2
pelota.dy=2

#CANCHA-----------------------------------------------Esta es la linea que divide a la mitad el mapa 
division= turtle.Turtle()
division.color("blue")
division.goto(0,500)
division.goto(0,-500)

#PEN----------------------------------------------------Este es el lapicero, es lo que se escribe en la parte superior del modulo, o sea el marcador
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador 1: {}     Jugador 2:  {} ".format(marcador1,marcador2), 
align = "center", font=("Times New Roman",30, "normal"))


#FUNCIONES JUEGO------------------------------------------------------------Funciones de cada movimiento, arriba y abajo, de cada jugador
def jugador_a_UP():
    y= jugador_a.ycor()
    y+=20----------------------------Se le suma 20 a las cordenadas del jugador 1 en el eje y, PARA MOVIMIENTO UP
    jugador_a.sety(y)

def jugador_a_DOWN():
    y= jugador_a.ycor()
    y-=20---------------------------Se le resta 20 a las cordenadas del jugador 1 en el eje y, PARA EL MOVIMIENTO DOWN 
    jugador_a.sety(y)

def jugador_b_UP():
    y= jugador_b.ycor()
    y+=20---------------------------Se le suma 20 a las cordenadas del jugador 2 en el eje y, PARA EL MOVIMIENTO UP
    jugador_b.sety(y)

def jugador_b_DOWN():
    y= jugador_b.ycor()
    y-=20----------------------------Se le  resta 20 a las coordenadas del jugador 2 en el eje y, PARA EL MOVIMIENTO DOWN
    jugador_b.sety(y)

#TECLADO
wn.listen()---------------------------------El programa escucha las teclas que presionas 
wn.onkeypress(jugador_a_UP, "w"or"W")-------onkeypress hace que cuando presiones la tecla de adentro del parentesis se ejecute la funcion
wn.onkeypress(jugador_a_DOWN, "s"or"S")-----onkeypress hace que se ejecute la funcion dentro del parentesis cuando se presione la telca s, es la misma funcion que el de la linea anterior
wn.onkeypress(jugador_b_UP, "Up")----------se ejecuta la funcion, cuando se oprime la tecla de la derecha
wn.onkeypress(jugador_b_DOWN, "Down")

while True:-----------------------------------Esto es para que el juego al ejecutarse no se detenga
    wn.update()-------------------------------El update actualiza el modulo cada vez que surja un cambio

    pelota.setx(pelota.xcor()+pelota.dx)------Establece las coordenadas y el movimiento de la pelota en el eje x
    pelota.sety(pelota.ycor()+pelota.dy)------Establece las coordenadas y el movimiento de la pelota en el eje y

    #EXTREMOS DEL JUEGO ARRIBA, ABAJO
    if pelota.ycor()>289:------------si las coordenadas del eje y de la pelota son >289(el borde superior del mapa)
        pelota.dy *= -1--------------se le multiplica *-1 para cambiar su sentido
    if pelota.ycor()<-289:------------ es lo mismo de arriba, peroo para el borde inferior de mapa
        pelota.dy *= -1
    
    
    #EXTREMOS DERECHA
    if  pelota.xcor()>490:------------ si la coordenada en el eje x es > 490, o se si la pelota llega al extremo de la derecha 
        pelota.goto(0,0)---------------la pelota se reincia en el centro, (0,0)
        pelota.dy *= -1----------------y se le cambia el sentido para que salga disparada en la direccion contraria
        marcador1 += 1-----------------y se le suma uno al marcador del jugador 1, poroque ensesto en la derecha
        pen.clear()-------------------- esto borra el marcador
        pen.write("Jugador 1:{}Jugador 2:{}".format(marcador1, marcador2), align="center",font=("Times New Roman", 30,"normal"))--------y se escribe el marcador actualizado
    #EXTREMOS IZQUIERDA
    if pelota.xcor()<-490:-------------Es la misma logica del extremo derecho, pero con los datos cambiados
        pelota.goto(0,0)
        pelota.dy *= -1
        marcador2 += 1
        pen.clear()
        pen.write("Jugador 1:{}Jugador 2:  {}".format(marcador1, marcador2), align="center",font=("Times New Roman", 30,"normal"))
        

    if ((pelota.xcor()>440 and pelota.xcor()<450)------------Esta parte es para los rebotes en los palos de los jugadores, en este caso es el jugadorb, el jugador 2
            and(pelota.ycor()<jugador_b.ycor()+50
            and pelota.ycor()>jugador_b.ycor()-50)):
        pelota.dx *=-1

    if ((pelota.xcor()<-440 and pelota.xcor()>-450)---------Esta parte es para los rebotes en los palos de los jugadores, en este caso es el jugador a, el jugador 1
            and(pelota.ycor()<jugador_a.ycor()+50
            and pelota.ycor()>jugador_a.ycor()-50)):
        pelota.dx *=-1
#LIMITES UP AND DOWN
    if jugador_a.ycor()>300:-------------------Limites, para que los palos no se salgan del tablero, por arriba, ni por abajo, del jugador a, jugador 1
        jugador_a.goto(-450,290)
    if jugador_a.ycor()<-300:
        jugador_a.goto(-450,-290)

    if jugador_b.ycor()>300:-----------------Limites para que los palos no se  salgan del tablero, por arriba, ni por abajo, del jugador b, jugador 2
        jugador_b.goto(450,290)
    if jugador_b.ycor()<-300:
        jugador_b.goto(450,-290)
