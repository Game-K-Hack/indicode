import time
from pickle import load as pkload
from pynput.keyboard import Key, Controller
from colorama import Back, Fore, deinit, init

from utils import chemin, configurer_touches, next_move, selection
from i18n import t



init()

with open("cheatcodes.db", "rb") as dbfile:
    c:dict = pkload(dbfile)
    codes: dict = c["character"]
    codes.update(c["extra"])

selecteds = selection(list(codes.keys()))

mapping = configurer_touches()

last_code = "A"*6
direction = "→"
selecteds_codes: list[str] = [codes[i] for i in selecteds]
moves = []

for code in selecteds_codes:
    move = []
    for i, letter in enumerate(list(code)):
        move.append("".join(chemin(last_code[i], letter)))
    # inverser la liste ou pas, suivant le sens
    move = direction.join(move[::-1] if direction == "←" else move)
    # inverser le sens
    direction = "←" if direction == "→" else "→"
    # ajouter à la liste des mouvements
    moves.append(move)
    last_code = code

print(t("intro_delay") + "\n")
while True:
    dalay = input("\033[1A\033[J" + t("prompt_delay"))
    if dalay.isnumeric():
        break

print(Fore.RED + "\n" + t("warning_position") + Fore.RESET + "\n")
input(Fore.CYAN + t("start_now") + Fore.RESET)

for i in range(int(dalay)):
    r = int(dalay) - i
    s = Fore.YELLOW + str(r) + Fore.CYAN if r > 1 else Fore.RED + "1" + Fore.CYAN
    countdown = t("countdown_one", s=s) if r == 1 else t("countdown_many", s=s)
    print("\033[1A\033[J" + Fore.CYAN + countdown + Fore.RESET)
    time.sleep(1)

def press(key: Key) -> None:
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)

display = lambda lc, li: (Fore.YELLOW + lc[:li] + Fore.RESET) + \
                         (Back.YELLOW + lc[li] + Back.RESET) + \
                         (Fore.YELLOW + lc[li+1:] + Fore.RESET)

last_code = "A"*6
livecode, liveindex = str(last_code), 0
keyboard = Controller()
for i, move in enumerate(moves):
    print("\033[1A\033[J" + Fore.GREEN + last_code + Fore.RESET +  " → " + Fore.CYAN + selecteds_codes[i] + Fore.RESET + "\n")
    for char in list(move):
        if char in ["→", "←"]:
            liveindex += 1 if char == "→" else -1
            time.sleep(0.1)
            press(mapping[char])
            time.sleep(0.2)
        else:
            livecode = next_move(livecode, selecteds_codes[i], liveindex)
            print("\033[1A\033[J" + display(livecode, liveindex))
            press(mapping[char])
            time.sleep(0.1)
    press(mapping["Valider"])
    print("\033[1A\033[J" + Fore.GREEN + livecode + Fore.RESET)
    time.sleep(1.5)
    last_code = str(selecteds_codes[i])

deinit()
