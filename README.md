# lego-mini-city-esp32
Ciudad LEGO Automatizada (ESP32 + MicroPython)

Una ciudad diseñada e impresa en 3D, automatizada con ESP32 y programada en MicroPython. Las únicas piezas LEGO reales son los personajes ("monitos") que la habitan — todo lo demás (calles, edificios, semáforos, soportes) está diseñado desde cero e impreso en 3D.

Este repositorio documenta el código y las conexiones de cada episodio de la serie, para que cualquiera pueda seguir el proceso, replicarlo, o probarlo sin necesitar el hardware físico (ver sección de Wokwi abajo).

Sobre el proyecto

La idea nace de querer automatizar una ciudad completa — con lógica real de tráfico, luces, y sensores — algo imposible de hacer a escala real por costo y espacio. La escala LEGO permite construir esa ciudad funcional en un espacio pequeño, con el mismo nivel de automatización real que tendría una ciudad de verdad.

Estructura del repositorio
episodio-00-intro/          → sin código, video de introducción al proyecto
episodio-01-primer-led/     → primer contacto con el ESP32, un LED controlado por código
episodio-02-semaforo/       → semáforo de 3 LEDs con lógica de tiempos real
episodio-03-planeacion/     → sin código, planeación del mapa completo de la ciudad
mini-caja-3d/               → diseño de la caja protectora para el protoboard (solo proceso, sin archivos de diseño descargables)

Cada carpeta de episodio con código incluye:

codigo.py — el código en MicroPython de ese episodio
notas.md — qué pines se usaron, decisiones tomadas, problemas encontrados (si los hubo)
Link al proyecto correspondiente en Wokwi
Pruébalo sin hardware (Wokwi)

Cada episodio con circuito tiene su propio proyecto en Wokwi, un simulador de ESP32 + MicroPython que corre directo en el navegador. Los links a cada proyecto específico están en el notas.md de cada carpeta.

Video de la serie
YouTube: [[YouTube]](https://www.youtube.com/@MiniciudaddeLeonel)

