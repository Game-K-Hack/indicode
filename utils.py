import os
import time
import platform
from colorama import Fore
from pynput.keyboard import Key, Listener

from display import affichage_colonne, display_banner
from i18n import t



ALPHABET_CHIFFRES = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [str(i) for i in range(10)]


def chemin(depart, arrivee) -> list[str]:
    idx_dep = ALPHABET_CHIFFRES.index(str(depart))
    idx_arr = ALPHABET_CHIFFRES.index(str(arrivee))
    n = len(ALPHABET_CHIFFRES)

    droite = (idx_arr - idx_dep) % n
    gauche = (idx_dep - idx_arr) % n

    return ["↑"] * droite if droite <= gauche else ["↓"] * gauche


def next_move(depart: str, arrivee: str, index: int = 0) -> str:
    if depart[index] == arrivee[index]:
        return depart
    else:
        move = chemin(depart[index], arrivee[index])[0]
        index_letter = (ALPHABET_CHIFFRES*3).index(depart[index], len(ALPHABET_CHIFFRES)-1)
        sens = (1 if move == "↑" else -1)
        new_letter = (ALPHABET_CHIFFRES*3)[index_letter + sens]
        res = list(depart)
        res[index] = new_letter
        return "".join(res)


def configurer_touches() -> dict:
    actions_a_configurer = ["↑", "→", "↓", "←", "Valider"]
    # Libellés affichés (les clés internes restent inchangées)
    labels = {a: a for a in actions_a_configurer}
    labels["Valider"] = t("action_validate")
    key_mapping = {}

    print(Fore.CYAN + t("config_title") + Fore.RESET)
    print(t("config_instruction") + "\n")

    for action in actions_a_configurer:
        label = labels[action]
        print(t("config_choose", action=Fore.CYAN + label + Fore.RESET), end="\r")
        touche_detectee: Key = None

        def on_press(key: Key):
            nonlocal touche_detectee
            touche_detectee = key
            return False

        with Listener(on_press=on_press) as listener:
            listener.join()

        key_mapping[action] = touche_detectee
        print("\x1b[2K" + t("config_assigned",
            action=Fore.CYAN + label + Fore.RESET,
            keybind=Fore.CYAN + touche_detectee.name + Fore.RESET))

        time.sleep(0.3)

    print(Fore.CYAN + "\n" + t("config_done") + Fore.RESET)
    return key_mapping


def selection(data: list[str]) -> list[str]:
    ok = True
    selecteds = []
    while ok:
        os.system("cls") if platform.system().lower() == "windows" else os.system("clear") # effacer ecran
        display_banner()
        affichage = ["\n" + t("header_character_codes") + "\n"]
        affichage += affichage_colonne(data[:59], selecteds)
        affichage.append("\n\n" + t("header_extra_codes") + "\n")
        affichage += affichage_colonne(data[59:], selecteds, colonne=3, sep=16, start_to=len(data[:59]))
        prompt = t("selection_prompt")
        print("\n".join(affichage) + "\n\n" + prompt, end="")
        choix = input().lower()
        match choix:
            case "v":
                ok = False
                break
            case "a":
                selecteds = [] if len(data) == len(selecteds) else list(range(len(data)))
            case _:
                if choix.isnumeric():
                    choix = int(choix) - 1
                    if 0 <= choix < len(data):
                        if choix in selecteds: 
                            selecteds.remove(choix)
                        else: 
                            selecteds.append(choix)
    print("\033[1A\033[J" + Fore.CYAN + t("selected_title") + "\n" + Fore.RESET)
    return [data[i] for i in selecteds]
