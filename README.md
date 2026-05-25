<div align="center">

![indicode banner](documentation/banner.png)

**Automatic cheat-code entry for _LEGO Indiana Jones: The Original Adventures_**

**English** · [Français](./documentation/README.fr.md) · [Deutsch](./documentation/README.de.md) · [Español](./documentation/README.es.md) · [Italiano](./documentation/README.it.md) · [日本語](./documentation/README.ja.md) · [한국어](./documentation/README.ko.md) · [Русский](./documentation/README.ru.md) · [中文](./documentation/README.zh.md)

</div>

## What is indicode?

In _LEGO Indiana Jones: The Original Adventures_, cheat codes are entered on a
6-character wheel in the Barnett College classroom, scrolling each character up or
down one at a time. Doing it by hand is slow and error-prone.

**indicode** does it for you. You pick the codes you want, it computes the shortest
path between each character, then simulates the keystrokes to enter them
automatically — one code after another.

## Demo

<a href="https://youtu.be/N4DFVwdnXN0">
    <img src="documentation/demo.gif"/>
</a>
![Video demo](https://youtu.be/N4DFVwdnXN0)

## Features

- **One-shot entry** — select multiple codes and let it type them all in sequence.
- **Shortest-path navigation** — chooses up vs. down for each character to minimize moves.
- **Custom key mapping** — configure your own keys for up / right / down / left / confirm.
- **Startup delay & countdown** — gives you time to switch back into the game.
- **9 languages** — English, French, German, Spanish, Italian, Japanese, Korean, Russian, Chinese (auto-detected).

## Requirements

- Python 3.10+
- [`pynput`](https://pypi.org/project/pynput/) and [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

1. Select the codes you want (`a` to select all, `v` to confirm).
2. Configure your keys (up, right, down, left, confirm).
3. Set a startup delay, then switch to the game with the board showing `(A) A A A A A`.
4. Sit back while indicode enters everything.

> Set the language manually with the `INDICODE_LANG` environment variable (e.g. `INDICODE_LANG=fr`).

![end banner](./documentation/end_banner.png)