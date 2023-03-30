"""
Proyecto:           Snake
Archivo:            snake.py
Autor:              Alberto Sánchez Barona
Fecha inicio:       06/12/2022
"""
# Importamos librería turtle.
import turtle

# Importamos librería time.
import time
POSPONER = 0.08

# Importamos librería random.
import random

# Marcadores.
puntuacion = 0
record = 0

# Creamos la ventana del juego y la modificamos.
ventana = turtle.Screen()
ventana.title("Snake v0.3 | Alberto Sánchez")
ventana.bgcolor("black")
ventana.setup(width = 600, height = 600)
ventana.tracer(0)

# Creamos la cabeza de la serpiente.
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Creamos la comida.
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# Creamos el cuerpo de la serpiente.
segmentos = []

# Crear puntuación.
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntuación: 0   Récord: 0", align = "center", font = ("Courier", 24, "bold"))

# Crear texto para salir.
texto_salir = turtle.Turtle()
texto_salir.speed(0)
texto_salir.color("white")
texto_salir.penup()
texto_salir.hideturtle()
texto_salir.goto(0,-280)
texto_salir.write("Pulsa Esc para salir", align = "center", font = ("Courier", 12, "bold"))

# Funciones
def arriba():
    if cabeza.direction == "down":
        pass
    else:
        cabeza.direction = "up"


def abajo():
    if cabeza.direction == "up":
        pass
    else:
        cabeza.direction = "down"


def izquierda():
    if cabeza.direction == "right":
        pass
    else:
        cabeza.direction = "left"


def derecha():
    if cabeza.direction == "left":
        pass
    else:
        cabeza.direction = "right"


def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def salir():
    global encendido
    encendido = False

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Iniciamos interruptor para acabar el juego.
encendido = True

ventana.onkeypress(salir, "Escape")

# Bucle principal
while encendido:
    ventana.update()

    # Colisiones bordes.
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        # Esconder segmentos.
        for segmento in segmentos:
            segmento.goto(5000,5000)

        # Limpiar lista de segmentos.
        segmentos.clear()
        
        # Resetear marcador.
        puntuacion = 0
        texto.clear()
        texto.write("Puntuación: {}   Récord: {}".format(puntuacion, record), align = "center", font = ("Courier", 24, "bold"))


    # Colisiones comida.
    if cabeza.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        # Nuevos segmentos.
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # Aumentar marcador.
        puntuacion += 1

        if puntuacion > record:
            record = puntuacion
        
        texto.clear()
        texto.write("Puntuación: {}   Récord: {}".format(puntuacion, record), align = "center", font = ("Courier", 24, "bold"))

    # Mover el cuerpo de la serpiente.
    total_segmentos = len(segmentos)
    for index in range(total_segmentos -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    
    if total_segmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    movimiento()

    # Colisiones con el cuerpo.
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            # Esconder segmentos.
            for segmento in segmentos:
                segmento.goto(5000,5000)

            # Limpiar lista de segmentos.
            segmentos.clear()

            # Resetear marcador.
            puntuacion = 0
            texto.clear()
            texto.write("Puntuación: {}   Récord: {}".format(puntuacion, record), align = "center", font = ("Courier", 24, "bold"))

    time.sleep(POSPONER)

turtle.bye()