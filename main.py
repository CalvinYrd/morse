from os import (
	name as os_name,
	system
)
from string import (
	ascii_uppercase as string_ascii_uppercase,
	digits as string_digits
)
from sys import exit

# retourne une création de couleur rgb
def rgb(colors):
	# vérification des paramètres
	for p in (colors[:-1]):
		if (type(p) != int):
			raise Exception('La valeur "'+p+'" doit être de type <int>')
		elif (p > 255 or p < 0):
			raise Exception('La valeur "'+p+'" est trop petite ou trop grande: les paramètres "r", "g" et "b" doivent tous être compris entre 0 et 255')

	if (colors[-1] not in ("color", "background")):
		raise Exception('Le dernier paramètre est invalide, il doit être soit "color" ou "background"')
	else:
		x = str([38 if colors[-1] == "color" else 48][0])
		return f'\x1b[{x};2;{colors[0]};{colors[1]};{colors[2]}m'

if (os_name == "nt"):
	clear = lambda: system("cls")
else:
	clear = lambda: system("clear")

chars = tuple(string_ascii_uppercase + string_digits + " ")
morse_chars = ('.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
	'.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
	'..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
	'...--', '....-', '.....', '-....', '--...', '---..', '----.', "/"
)
white = rgb((255, 255, 255, "color"))
green = rgb((0, 255, 0, "color"))
msg_list = ("Traduire morse vers alphabet", "Traduire alphabet vers morse", "Quitter")
msg = ""

for i in range(len(msg_list)):
	msg += green + str(i + 1) + ". " + white + msg_list[i] + "\n"

msg += "> "

while (True):
	while (True):
		try:
			clear()
			trad_action = int(input(msg))

			if (trad_action not in range(1, len(msg_list) + 1)): raise AssertionError
			else: break

		except (AssertionError, ValueError):
			continue

	if (trad_action == 3):
		clear()
		exit(0)

	clear()
	while (True):
		print("--------------------------")
		if (trad_action == 1): print(green + "Traduction" + white + " : morse - alphabet")
		else: print(green + "Traduction" + white + " : alphabet - morse")
		print("--------------------------")

		txt = input("\nSaisissez le texte à traduire :\n> ")

		if (txt.strip() == ""):
			clear()
			print(rgb((255, 0, 0, "color")) + "Erreur de saisie" + white)
			continue

		if (trad_action == 1): txt, joiner = txt.split(" "), ""
		else: txt, joiner = list(txt.upper()), " "

		try:
			for i in range(len(txt)):
				if (trad_action == 1):
					index = morse_chars.index(txt[i].strip())
					txt[i] = chars[index]

				else:
					tmp = [txt[i] if txt[i] == " " else txt[i].strip()][0]
					index = chars.index(tmp)
					txt[i] = morse_chars[index]

			txt = joiner.join(txt)
			input("\n" + green + "Résultat" + white + " :\n\n" + txt)
			break

		except ValueError:
			clear()
			print(rgb((255, 0, 0, "color")) + "Erreur de saisie" + white)
			continue


