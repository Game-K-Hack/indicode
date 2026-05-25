<div align="center">

![banner de indicode](banner.png)

**Introducción automática de códigos de trucos para _LEGO Indiana Jones: La trilogía original_**

[English](../README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · **Español** · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [中文](README.zh.md)

</div>

## ¿Qué es indicode?

En _LEGO Indiana Jones: La trilogía original_, los códigos de trucos se introducen en
una rueda de 6 caracteres, en el aula del Barnett College, desplazando cada carácter
hacia arriba o hacia abajo de uno en uno. Hacerlo a mano es lento y propenso a errores.

**indicode** lo hace por ti. Eliges los códigos que quieras, calcula el camino más corto
entre cada carácter y luego simula las pulsaciones de teclas para introducirlos
automáticamente, uno tras otro.

## Demo

<a href="https://youtu.be/N4DFVwdnXN0">
    <img src="demo.gif"/>
</a>
![Demo en vídeo](https://youtu.be/N4DFVwdnXN0)

## Características

- **Introducción de una sola vez** — selecciona varios códigos y deja que los escriba todos seguidos.
- **Navegación por el camino más corto** — elige arriba o abajo para cada carácter y minimiza los movimientos.
- **Asignación de teclas personalizada** — configura tus propias teclas para arriba / derecha / abajo / izquierda / confirmar.
- **Retardo de inicio y cuenta atrás** — te da tiempo para volver al juego.
- **9 idiomas** — inglés, francés, alemán, español, italiano, japonés, coreano, ruso, chino (detección automática).

## Requisitos

- Python 3.10+
- [`pynput`](https://pypi.org/project/pynput/) y [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## Uso

```bash
python main.py
```

1. Selecciona los códigos que quieras (`a` para seleccionar todos, `v` para confirmar).
2. Configura tus teclas (arriba, derecha, abajo, izquierda, confirmar).
3. Define un retardo de inicio y vuelve al juego con el tablero mostrando `(A) A A A A A`.
4. Relájate mientras indicode lo introduce todo.

> Fuerza el idioma con la variable de entorno `INDICODE_LANG` (p. ej. `INDICODE_LANG=es`).

![end banner](./end_banner.png)
