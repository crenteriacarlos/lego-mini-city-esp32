# Episodio 2 — El primer semáforo

## Qué hace el circuito

Tres LEDs (verde, amarillo, rojo) controlados desde el ESP32, siguiendo la
secuencia de un semáforo real:

1. **Verde** encendido 5 segundos
2. **Amarillo** parpadeando 3 veces (medio segundo encendido, medio apagado)
3. **Rojo** encendido 5 segundos
4. Repite

El amarillo va **entre el verde y el rojo**, avisando que viene el alto. Es
el orden que usa un semáforo de verdad.

## Componentes

| Componente | Detalle |
|---|---|
| Placa | ESP32-C3-DevKitM-1 |
| LEDs | 3 de 5mm: rojo, amarillo y verde |
| Resistencias | 3 × 220 Ω |
| Protoboard | 1 |
| Cables jumper | macho-macho |

Firmware de MicroPython usado en la simulación: **v1.28.0**.

## Conexiones

| LED | Pin del ESP32 |
|---|---|
| Verde | 0 |
| Amarillo | 1 |
| Rojo | 3 |

Cada LED va con su resistencia en serie: **ánodo** → resistencia → pin,
y **cátodo** → GND.

## Simulación en Wokwi

Puedes correr este circuito completo en el navegador, sin comprar nada.

**Opción 1 — el link directo:**
*(agregar aquí el link del proyecto guardado)*

**Opción 2 — desde el archivo de esta carpeta:**

1. Abre [wokwi.com](https://wokwi.com) y crea un proyecto nuevo de
   **ESP32 / MicroPython**
2. Abre la pestaña `diagram.json` y reemplaza todo su contenido por el del
   [`diagram.json`](diagram.json) de esta carpeta
3. Pega el contenido de [`codigo.py`](codigo.py) en `main.py`
4. Dale play

El diagrama ya incluye las tres resistencias, los tres LEDs y el cableado a
los pines correctos.

## Sobre el estilo del código

Este código está escrito **en cascada a propósito**, como parte de aprender
paso a paso. El bloque del amarillo aparece tres veces seguidas en vez de
estar dentro de un bucle.

Es deliberado: la prioridad ahorita es entender cada línea, no escribir lo
más corto posible.

**Pendiente:** reescribirlo en una versión más eficiente y estructurada
cuando el proyecto lo exija. Cuando eso pase, las dos versiones se van a
conservar aquí (`codigo_v1_cascada.py` y `codigo_v2_optimizado.py`) para
poder compararlas.

## Limitación conocida

`time.sleep()` **bloquea** el ESP32 por completo. Mientras el verde está
encendido 5 segundos, la placa no puede hacer absolutamente nada más.

Funciona bien con un solo semáforo. Va a dejar de funcionar cuando el mismo
ESP32 tenga que atender varios sistemas a la vez — y esa va a ser la razón
real para reescribir el código.

## Nota sobre los pines (importante si usas otra placa)

Los números de pin **no significan lo mismo en todas las variantes de
ESP32**, y esta combinación es un buen ejemplo de por qué.

En el **ESP32-C3** los GPIO 0, 1 y 3 son de propósito general y están
libres: la comunicación serial va por otros pines. Por eso este código
funciona.

En un **ESP32 clásico** (WROOM-32, el más común) los GPIO 1 y 3 son el
TX y RX del puerto serial. Si cargas este código tal cual en una de esas
placas, los LEDs del amarillo y el rojo van a interferir con la conexión
por USB.

Si replicas esto en otra placa, revisa primero el diagrama de pines de tu
modelo y cambia los números en las tres líneas de arriba del código.

## Estado

- ✅ Probado en hardware físico
- ✅ Probado en Wokwi
