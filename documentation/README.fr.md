<div align="center">

![bannière indicode](banner.png)

**Saisie automatique des codes de triche pour _LEGO Indiana Jones : La Trilogie originale_**

[English](../README.md) · **Français** · [Deutsch](README.de.md) · [Español](README.es.md) · [Italiano](README.it.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [中文](README.zh.md)

</div>

## Qu'est-ce qu'indicode ?

Dans _LEGO Indiana Jones : La Trilogie originale_, les codes de triche se saisissent
sur une roue de 6 caractères, dans la salle de classe du Barnett College, en faisant
défiler chaque caractère vers le haut ou le bas, un à un. Le faire à la main est lent
et source d'erreurs.

**indicode** s'en charge pour vous. Vous choisissez les codes voulus, il calcule le
chemin le plus court entre chaque caractère, puis simule les frappes clavier pour les
saisir automatiquement — un code après l'autre.

## Démo

<a href="https://youtu.be/N4DFVwdnXN0">
    <img src="demo.gif"/>
</a>

![Démo vidéo](https://youtu.be/N4DFVwdnXN0)

## Fonctionnalités

- **Saisie en une fois** — sélectionnez plusieurs codes et laissez-le tous les taper à la suite.
- **Navigation au plus court** — choisit haut ou bas pour chaque caractère afin de minimiser les déplacements.
- **Touches personnalisables** — configurez vos propres touches pour haut / droite / bas / gauche / valider.
- **Délai et compte à rebours** — vous laisse le temps de revenir dans le jeu.
- **9 langues** — anglais, français, allemand, espagnol, italien, japonais, coréen, russe, chinois (détection automatique).

## Prérequis

- Python 3.10+
- [`pynput`](https://pypi.org/project/pynput/) et [`colorama`](https://pypi.org/project/colorama/)

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
```

1. Sélectionnez les codes voulus (`a` pour tout sélectionner, `v` pour valider).
2. Configurez vos touches (haut, droite, bas, gauche, valider).
3. Définissez un délai de démarrage, puis revenez au jeu avec le tableau affichant `(A) A A A A A`.
4. Détendez-vous pendant qu'indicode saisit tout.

> Forcez la langue avec la variable d'environnement `INDICODE_LANG` (par ex. `INDICODE_LANG=fr`).

![end banner](./end_banner.png)
