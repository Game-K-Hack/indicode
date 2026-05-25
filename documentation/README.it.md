<div align="center">

![banner di indicode](banner.png)

**Inserimento automatico dei codici trucco per _LEGO Indiana Jones: Le avventure originali_**

[English](../README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md) · **Italiano** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [中文](README.zh.md)

</div>

## Cos'è indicode?

In _LEGO Indiana Jones: Le avventure originali_, i codici trucco si inseriscono su una
ruota di 6 caratteri, nell'aula del Barnett College, scorrendo ogni carattere verso
l'alto o verso il basso uno alla volta. Farlo a mano è lento e soggetto a errori.

**indicode** lo fa al posto tuo. Scegli i codici che vuoi, calcola il percorso più breve
tra ogni carattere e poi simula la pressione dei tasti per inserirli automaticamente,
un codice dopo l'altro.

## Demo

[▶ Guarda la demo](demo.mp4)

## Funzionalità

- **Inserimento in una volta sola** — seleziona più codici e lascia che li digiti tutti di seguito.
- **Navigazione sul percorso più breve** — sceglie su o giù per ogni carattere per ridurre i movimenti.
- **Mappatura tasti personalizzabile** — configura i tuoi tasti per su / destra / giù / sinistra / conferma.
- **Ritardo di avvio e conto alla rovescia** — ti dà il tempo di tornare nel gioco.
- **9 lingue** — inglese, francese, tedesco, spagnolo, italiano, giapponese, coreano, russo, cinese (rilevamento automatico).

## Requisiti

- Python 3.10+
- [`pynput`](https://pypi.org/project/pynput/) e [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## Utilizzo

```bash
python main.py
```

1. Seleziona i codici che vuoi (`a` per selezionarli tutti, `v` per confermare).
2. Configura i tuoi tasti (su, destra, giù, sinistra, conferma).
3. Imposta un ritardo di avvio, poi torna al gioco con la lavagna che mostra `(A) A A A A A`.
4. Rilassati mentre indicode inserisce tutto.

> Forza la lingua con la variabile d'ambiente `INDICODE_LANG` (es. `INDICODE_LANG=it`).
