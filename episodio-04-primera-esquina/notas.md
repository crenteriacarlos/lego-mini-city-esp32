# Episodio 4 — La primera esquina de Leo City

El semáforo deja el protoboard y se instala en una esquina real, con carcasa
impresa y el cableado escondido.

## El código

**Es el mismo del Episodio 2**, sin cambios. Lo que cambió es el hardware, no
el programa.

→ [`../episodio-02-semaforo/codigo.py`](../episodio-02-semaforo/codigo.py)

Pines, igual que antes:

| LED | Pin |
|---|---|
| Verde | IO0 |
| Amarillo | IO1 |
| Rojo | IO3 |

Cada LED con su resistencia de 220 Ω en serie: **ánodo** → resistencia → pin,
**cátodo** → GND.

## La pieza

| Dato | Valor |
|---|---|
| Tiempo de impresión | 18 min 08 s |
| Material | 5.44 g |
| Colores | 1 |
| Altura de la pieza | *(agregar)* |
| Altura de capa | *(agregar)* |
| Soportes | *(agregar sí / no)* |

El desglose del slicer muestra puentes y pared en voladizo, así que hay
geometría que se está salvando en el aire.

### El dato interesante: tiempo vs. tamaño

| | Semáforo | Carretera lisa |
|---|---|---|
| Material | 5.44 g | 7.35 g |
| Tiempo | **18:08** | **11:59** |
| min/g | 3.33 | 1.63 |

La pieza más chica y más ligera tarda **50% más** en imprimirse.

La razón está en el desglose por tipo de línea: casi la mitad del tiempo del
semáforo se va en las paredes (interior y exterior), y el relleno interior es
menos del 1% de la impresión.

Una carretera es una plancha maciza — el nozzle recorre poco y deposita mucho.
El semáforo son paredes delgadas con huecos para los LEDs — el nozzle recorre
muchísimo y deposita poquito.

**La regla:** en impresión 3D el tiempo no lo define el tamaño, lo define el
detalle. Para piezas con detalle en esta impresora, el factor es de unos
**3.3 minutos por gramo**; para planchas, **1.6**.

### Versión 2

La primera versión de la carcasa no funcionó.

*(agregar: qué falló exactamente — medidas de los huecos de LED, grosor de
pared, espacio para el cableado, lo que haya sido)*

Es un recordatorio útil: Fusion te deja diseñar cosas que no se pueden
imprimir, o que se imprimen pero no sirven. La pieza no está terminada cuando
el modelo se ve bien en pantalla.

## El cableado

Primera vez que se cobra la base del Episodio 3.

El cable de cada LED baja **por dentro de la carcasa**, sale por un perno
hueco de la placa base, y cruza por debajo hasta la caja de electrónica. Por
arriba no se ve un solo cable.

Sin perforar nada y sin fijar la posición del semáforo de forma permanente —
en el Episodio 8 se mueve a un cruce nuevo sin costo.

## Estado

- ✅ Pieza impresa e instalada
- ✅ Semáforo funcionando en su esquina
- ⬜ Posición definitiva — se reubica en el Episodio 8

## Nota sobre los diseños 3D

El archivo de la carcasa del semáforo **no se incluye** en este repositorio —
ver la nota del README. Las medidas, los tiempos y las decisiones de diseño sí
están aquí.
