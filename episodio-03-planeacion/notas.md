# Episodio 3 — Planeando Leo City

Este episodio no lleva código. Es el de las decisiones de infraestructura que
sostienen todo lo que viene después.

## La base

Seis placas impresas que, unidas, forman la superficie completa de la ciudad.

| Dato | Valor |
|---|---|
| Número de placas | 6 |
| Medida de cada placa | *(agregar)* |
| Medida total armada | *(agregar)* |
| Altura de capa | *(agregar)* |
| Colores | 3, dos placas de cada uno |

### Los pernos huecos

**La decisión más importante del proyecto.** Cada perno de la base está
perforado de lado a lado.

El problema que resuelve: todo lo que se construye encima lleva cables. La
solución obvia sería perforar la base donde va cada pieza, pero eso obliga a
decidir las posiciones de forma permanente — y si después quieres mover algo,
te queda el agujero viejo a la vista.

Con todos los pernos huecos no hay una posición buena y muchas malas: **todas
las posiciones son buenas.** Donde sea que vaya una pieza, el cable ya tiene
por dónde bajar.

En el Episodio 8 esto se cobra en grande: la ciudad entera se reacomoda
alrededor de un cruce nuevo sin perforar nada.

### Unión entre placas

*(agregar: cómo embonan las placas entre sí)*

**Nota sobre tolerancias:** antes de imprimir el juego completo conviene medir
seis placas armadas contra seis veces una sola placa. Los errores de tolerancia
se acumulan y a la sexta placa pueden ser visibles.

## Los pilares

Van debajo de la base y levantan toda la ciudad de la mesa.

| Dato | Valor |
|---|---|
| Altura | *(agregar)* |
| Cantidad | *(agregar)* |

No son decorativos: el espacio que dejan debajo es donde vive la caja de
electrónica. El cable que baja por un perno tiene que llegar a algún lado.

## La caja de electrónica

Vive debajo de la base, en el espacio que dejan los pilares.

- El protoboard va **montado adentro**, fijo en su lugar
- El ESP32 también va adentro
- De la caja solo salen los cables que alimentan la ciudad

Con eso, toda la electrónica queda en un solo bloque. Mover la ciudad de lugar
no implica volver a cablear nada.

### Cierre magnético

La caja se abre levantándola, y las dos mitades se mantienen juntas con
**imanes**. Sin tornillos.

| Dato | Valor |
|---|---|
| Tipo y medida de imán | *(agregar)* |
| Cantidad | *(agregar)* |
| Cómo van fijados | *(agregar: pegados, a presión, atrapados en la impresión)* |

**Por qué imanes y no tornillos:** esta caja se va a abrir decenas de veces a
lo largo del proyecto. Unos tornillos en plástico impreso se barren a la décima
o la vigésima vez. Los imanes se abren con una mano, sin herramienta, y no se
desgastan.

**Advertencia al montarlos:** verifica la polaridad antes de fijar cada imán.
Si uno queda al revés, la caja no cierra, y sacarlo de una pieza impresa es
molesto.

## Cableado subterráneo: una decisión, no una imitación

En México y en buena parte de Latinoamérica el cableado urbano va por arriba:
postes, cables cruzando las calles, nudos en cada esquina.

Leo City va al revés — todo por abajo. No es por realismo; es lo contrario del
entorno real. Es porque una ciudad donde el cableado está resuelto desde el
primer día es una ciudad que alguien pensó completa, en vez de una que fue
creciendo y resolviendo sobre la marcha.

## Modularidad

Estas seis placas no son la ciudad: son el **primer módulo**.

Todo el sistema está diseñado para extenderse. Las placas se agregan, las
piezas de calle embonan entre sí, y nada queda fijado de forma permanente. El
proyecto no tiene una fecha de entrega — tiene módulos.

## Orden de construcción

1. La esquina del semáforo
2. El alumbrado
3. Las calles completas
4. El acceso: pluma, reja y puerta
5. El edificio
6. Los locales
7. La plaza

## Cuenta de pines

La placa de todo el proyecto es una **ESP32-C3-DevKitM-1**. Saca 15 GPIO al
conector: IO0 a IO10, más IO18, IO19, IO20 e IO21.

De esos:
- **IO18 / IO19** — USB
- **IO20 / IO21** — UART0 (serial)
- **IO2, IO8, IO9** — pines de arranque (strapping), usables con cuidado

Quedan **8 pines cómodos**: IO0, IO1, IO3, IO4, IO5, IO6, IO7, IO10.

| Episodio | Sistema | Pines | Acumulado |
|---|---|---|---|
| 2 / 4 | Semáforo | IO0, IO1, IO3 | 3 / 8 |
| 5 | Alumbrado | *(agregar)* | |
| 6 | Sensor de luz | *(agregar)* | |

Esta tabla se actualiza en cada episodio. Cuando el límite se rompa, va a
contar la historia completa.

## Nota sobre los diseños 3D

Los archivos de las placas, los pilares y la caja **no se incluyen** en este
repositorio — ver la nota del README. Las medidas y las decisiones de diseño
sí están documentadas aquí, que es lo que de verdad sirve para replicar el
enfoque en un proyecto propio.
