"""
Leo City — Episodio 1: Primer contacto con el ESP32
----------------------------------------------------
Enciende y apaga un LED conectado al pin 0, con un segundo
de espera entre cada cambio.

Es la pieza más simple de todo el proyecto, y la base de
todo lo que viene después: el mismo principio de activar
un pin es el que después controla el semáforo.

Video: https://www.youtube.com/@MiniciudaddeLeonel
"""

from machine import Pin
import time

# El LED va al pin 0, con su resistencia en serie
led = Pin(0, Pin.OUT)

while True:
    led.value(1)      # enciende
    time.sleep(1)     # espera 1 segundo
    led.value(0)      # apaga
    time.sleep(1)     # espera 1 segundo
