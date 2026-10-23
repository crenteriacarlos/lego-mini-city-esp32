# Episodio 1 — Primer contacto con el ESP32

## Qué hace el circuito

Un LED conectado al **pin 0** del ESP32. El código lo enciende, espera un
segundo, lo apaga, espera un segundo, y repite el ciclo indefinidamente.

Es el equivalente al "Hola mundo" de los microcontroladores.

## Componentes

| Componente | Detalle |
|---|---|
| Placa | ESP32-C3-DevKitM-1 |
| LED | 1 de 5mm, cualquier color |
| Resistencia | 1 × 220 Ω |
| Protoboard | 1 |
| Cables jumper | macho-macho |

**Sobre la resistencia:** no es opcional. Un LED no limita la corriente que
pasa por él; conectado directo al pin jala toda la que puede y termina
quemando el LED, el pin, o los dos.

## Conexiones

- **Ánodo del LED (pata larga)** → resistencia → **Pin 0** del ESP32
- **Cátodo del LED (pata corta)** → **GND** del ESP32

## Simulación en Wokwi

*(agregar aquí el link del proyecto guardado)*

## Nota sobre los pines

Los números de pin no significan lo mismo en todas las variantes de ESP32.
En el **ESP32-C3** el GPIO 0 es de propósito general y está libre, por eso
este código funciona tal cual.

Si lo replicas en otra placa y ves comportamiento raro, revisa el diagrama
de pines de tu modelo y cambia el número en la línea del `Pin()`.

## Estado

- ✅ Probado en hardware físico
- ✅ Probado en Wokwi

## Notas del proceso

Primera vez programando un ESP32 y usando MicroPython. El circuito es
intencionalmente simple porque es la base de todo lo que viene después.
