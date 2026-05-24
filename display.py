import re
import math
from colorama import Fore



def affichage_colonne(data: list[str], selecteds: list[int] = [], colonne: int = 4, sep: int = 3, start_to: int = 0) -> list[str]:
    # 1. Vérifications de sécurité
    if not data or colonne < 1:
        raise ValueError(Fore.RED + "[ERROR] Problème d'affichage : données vides ou colonnes invalides" + Fore.RESET)

    total_elements = len(data)
    # Calcul du nombre de lignes nécessaires
    lignes = math.ceil(total_elements / colonne)
    
    # 2. Trouver la chaîne la plus longue sans compter les codes couleur
    longueur_plus_grand_str = max(len(v) for v in data) if data else 0

    # 3. Préparer les éléments formatés (sans mélange de couleur dans le calcul de taille)
    elements_colores = []
    for i, v in enumerate(data):
        # Formatage de base de l'élément : "[  1 ] MonTexte   "
        espaces = " " * (longueur_plus_grand_str - len(v))
        item_str = f"[ {(start_to + i + 1):2d} ] {v}{espaces}"
        
        # Application de la couleur si sélectionné
        if start_to + i in selecteds:
            item_str = f"{Fore.GREEN}{item_str}{Fore.RESET}"
        elements_colores.append(item_str)

    # 4. Construction de l'affichage par ligne
    affichage = []
    for l in range(lignes):
        items_ligne = []
        for c in range(colonne):
            # Calcul de l'index de l'élément pour une distribution verticale
            index = l + (c * lignes)
            if index < total_elements:
                items_ligne.append(elements_colores[index])
        
        # Jointure de la ligne avec le séparateur
        affichage.append((" " * sep).join(items_ligne))
    
    return affichage


def multiplier_caracteres(texte: str) -> str:
    def remplacement(match):
        chiffre = int(match.group(1))
        caractere = match.group(2)
        return caractere * chiffre
    return re.sub(r'(\d+)(.)', remplacement, texte)


def ascii_art(ascii_art, start_rgb, end_rgb, angle_degrees):
    """
    Affiche un texte ASCII avec un dégradé dont on peut choisir l'angle (en degrés).
    0° = Horizontal (gauche à droite)
    90° = Vertical (haut en bas)
    45° = Diagonale descendante
    """
    lines = ascii_art.splitlines()
    if not lines:
        return

    max_rows = len(lines)
    max_cols = max(len(line) for line in lines)

    # Conversion de l'angle en radians
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)

    # Pour calibrer le dégradé (du minimum au maximum), on doit calculer 
    # la projection des 4 coins du texte pour trouver l'amplitude de l'axe du dégradé.
    # Formule de projection : P = col * cos(α) + row * sin(α)
    corners = [
        0 * cos_a + 0 * sin_a,                      # Top-Left
        (max_cols - 1) * cos_a + 0 * sin_a,          # Top-Right
        0 * cos_a + (max_rows - 1) * sin_a,          # Bottom-Left
        (max_cols - 1) * cos_a + (max_rows - 1) * sin_a # Bottom-Right
    ]
    min_p = min(corners)
    max_p = max(corners)
    range_p = max_p - min_p if max_p != min_p else 1

    sr, sg, sb = start_rgb
    er, eg, eb = end_rgb

    for row, line in enumerate(lines):
        line_str = ""
        for col, char in enumerate(line):
            # Projection du point actuel sur l'axe de l'angle
            current_p = col * cos_a + row * sin_a
            
            # Normalisation entre 0.0 et 1.0
            t = (current_p - min_p) / range_p
            # Sécurité pour rester dans les clous [0, 1]
            t = max(0.0, min(1.0, t))
            
            # Interpolation des couleurs
            r = int(sr + (er - sr) * t)
            g = int(sg + (eg - sg) * t)
            b = int(sb + (eb - sb) * t)
            
            line_str += f"\033[38;2;{r};{g};{b}m{char}"
            
        print(line_str + "\033[0m")


def display_banner():
    print("\n")
    with open("banner", "r", encoding="utf8") as file:
        ascii_art(
            multiplier_caracteres(file.read().replace("\\n", "\n")), 
            (237, 53, 34), (255, 225, 117), angle_degrees=85)
    ascii_art(
        "\n\n  by Harlock\n      → GitHub: Game-K-Hack" + "\n"*5, 
        (240, 50, 50), (30, 130, 240), angle_degrees=45)
