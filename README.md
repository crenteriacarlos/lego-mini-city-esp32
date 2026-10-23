# Leo City — Ciudad LEGO Automatizada (ESP32 + MicroPython)

Una ciudad diseñada e impresa en 3D, automatizada con ESP32 y programada en MicroPython. Las únicas piezas LEGO reales son los personajes ("monitos") que la habitan — todo lo demás (calles, edificios, semáforos, soportes) está diseñado desde cero e impreso en 3D.

Este repositorio documenta el código y las conexiones de cada episodio de la serie, para que cualquiera pueda seguir el proceso, replicarlo, o probarlo sin necesitar el hardware físico (ver la sección de Wokwi más abajo).

## Sobre el proyecto

La idea nace de querer automatizar una ciudad completa — con lógica real de tráfico, luces y sensores — algo imposible de hacer a escala real por costo y espacio. La escala LEGO permite construir esa ciudad funcional en un espacio pequeño, con el mismo nivel de automatización que tendría una ciudad de verdad.

## Estructura del repositorio

```
episodio-00-intro/           → sin código, introducción al proyecto
episodio-01-primer-led/      → primer contacto con el ESP32, un LED controlado por código
episodio-02-semaforo/        → semáforo de 3 LEDs con lógica de tiempos
episodio-03-planeacion/      → sin código, la base, los pilares y la caja de electrónica
episodio-04-primera-esquina/ → el semáforo impreso e instalado en la ciudad
```

Cada carpeta incluye un `notas.md` con los componentes, los pines usados, las
decisiones de diseño y los problemas encontrados. Los episodios con código
llevan además:

- `codigo.py` — el código en MicroPython de ese episodio
- `diagram.json` — el circuito completo, listo para cargar en Wokwi

## Pruébalo sin hardware (Wokwi)

[Wokwi](https://wokwi.com) es un simulador de ESP32 y MicroPython que corre directo en el navegador. Puedes armar y correr estos circuitos sin comprar nada.

Para cargar cualquier episodio:

1. Crea un proyecto nuevo de **ESP32 / MicroPython** en Wokwi
2. Abre la pestaña `diagram.json` y reemplaza su contenido por el `diagram.json` de la carpeta del episodio
3. Pega el `codigo.py` en `main.py`
4. Dale play

El diagrama ya trae los componentes, los valores de las resistencias y el cableado a los pines correctos.

## Hardware usado

Toda la serie corre sobre una **ESP32-C3-DevKitM-1** con MicroPython.

Ojo con los números de pin: no significan lo mismo en todas las variantes de ESP32. En la C3 los GPIO 0, 1 y 3 están libres, pero en un ESP32 clásico (WROOM-32) los GPIO 1 y 3 son el serial por USB. Cada `notas.md` lo aclara para su circuito.

## Sobre el código

El código de esta serie está escrito **en cascada a propósito**: paso a paso, de arriba hacia abajo, sin estructuras que agrupen lo que se repite.

No es por descuido. Estoy aprendiendo MicroPython desde cero y quiero entender qué hace cada línea antes de empezar a optimizar. Más adelante, cuando el proyecto lo exija, el código se va a reescribir — y cuando eso pase se van a conservar **las dos versiones** en el repositorio, para poder comparar qué cambió y por qué.

## Nota sobre los diseños 3D

El código de este repositorio es de uso libre.

Los archivos de diseño 3D (Fusion 360 / STL) de piezas específicas **no se incluyen aquí** — algunas están contempladas como posible producto o kit a futuro. El proceso de diseño e impresión sí se documenta completo en los videos.

## La serie

- **YouTube:** [Mini ciudad de Leonel](https://www.youtube.com/@MiniciudaddeLeonel)

## Licencia

Ver el archivo [LICENSE](LICENSE).
