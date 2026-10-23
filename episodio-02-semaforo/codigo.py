"""
Leo City — Episodio 2: El primer semáforo
------------------------------------------
Semáforo de 3 LEDs con la secuencia real de un semáforo:
verde 5s → amarillo parpadeando 3 veces → rojo 5s → repite.

El amarillo va entre el verde y el rojo, avisando que viene
el alto — igual que un semáforo de verdad.

NOTA SOBRE EL ESTILO DE ESTE CÓDIGO
Está escrito en cascada a propósito: paso a paso, de arriba
hacia abajo, cada instrucción en su línea. El bloque del
amarillo está repetido tres veces en vez de usar un bucle.

No es por descuido. Estoy aprendiendo MicroPython desde cero
y quiero entender qué hace cada línea antes de agrupar nada.
Más adelante este código se va a reescribir — y cuando pase,
las dos versiones van a quedar en el repositorio para poder
compararlas.

Video: https://www.youtube.com/@MiniciudaddeLeonel
"""

from machine import Pin
import time

led_rojo = Pin(3, Pin.OUT)
led_amarillo = Pin(1, Pin.OUT)
led_verde = Pin(0, Pin.OUT)

# Arrancar con todo apagado
led_amarillo.value(0)
led_verde.value(0)
led_rojo.value(0)

while True:
    # VERDE — 5 segundos
    led_verde.value(1)
    time.sleep(5)
    led_verde.value(0)

    # AMARILLO — 3 parpadeos de medio segundo
    led_amarillo.value(1)
    time.sleep(.5)
    led_amarillo.value(0)
    time.sleep(.5)

    led_amarillo.value(1)
    time.sleep(.5)
    led_amarillo.value(0)
    time.sleep(.5)

    led_amarillo.value(1)
    time.sleep(.5)
    led_amarillo.value(0)

    # ROJO — 5 segundos
    led_rojo.value(1)
    time.sleep(5)
    led_rojo.value(0)
