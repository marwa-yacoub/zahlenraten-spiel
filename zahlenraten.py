import random

geheimzahl = random.randint(1, 100)
versuche = 0

print("Willkommen beim Zahlenraten!")
print("Ich denke an eine Zahl zwischen 1 und 100.")

while True:
    eingabe = input("Dein Tipp: ")
    if not eingabe.isdigit():
        print("Bitte gib eine Zahl ein.")
        continue
    tipp = int(eingabe)
    versuche += 1
    if tipp < geheimzahl:
        print("Zu klein!")
    elif tipp > geheimzahl:
        print("Zu groß!")
    else:
        print(f"Richtig! Du hast {versuche} Versuche gebraucht.")
        break
