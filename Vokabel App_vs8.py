import json
import random
import traceback
import sys
import time
import os


def clear_screen():
    os.system('cls')


VOKABELDATEI = "vokabeln.json"

if os.name == "nt":
    VOKABELDATEI = VOKABELDATEI.replace("/", "\\")

# Funktion zum Laden der Vokabeln aus der Datei
def vokabeln_laden():
    try:
        with open(VOKABELDATEI, "r") as f:
            vokabeln = json.load(f)
    except FileNotFoundError:
        vokabeln = []
    return vokabeln

# Funktion zum Speichern der Vokabeln in der Datei
def vokabeln_speichern(vokabeln):
    with open(VOKABELDATEI, "w") as f:
        json.dump(vokabeln, f)
        
#Funktion Vokabeln nach Thema auswählen
def vokabeln_nach_thema(vokabeln, thema):
    return [vokabel for vokabel in vokabeln if vokabel["thema"].lower() == thema.lower()]


# Funktion zum Erfassen neuer Vokabeln
def vokabeln_erfassen(vokabeln):
    while True:
        englisch = input("Englisches Wort: ")
        if not englisch:
            print("Bitte geben Sie ein englisches Wort ein.")
            continue
        
        deutsch = input("Deutsche Übersetzung: ")
        if not deutsch:
            print("Bitte geben Sie eine deutsche Übersetzung ein.")
            continue
        
        thema = input("Thema: ")
        klasse = input("Klasse: ")
        aktuell = input("Aktuelle Vokabel? (ja/nein): ")
        
        vokabeln.append({"englisch": englisch, "deutsch": deutsch, "thema": thema, "klasse": klasse, "aktuell": aktuell})
        
        vokabeln_speichern(vokabeln)
        print(f"{len(vokabeln)} Vokabeln wurden erfasst.")
        
        weitere_vokabel = input("Weitere Vokabel erfassen? (ja/nein): ")
        
        if weitere_vokabel.lower() != "ja" and weitere_vokabel != "":
            break
    
# Funktion zum Starten des Vokabel Quiz

#Berechnung Ergebnis als Note
def punktzahl_zu_note(punktzahl, gesamtpunktzahl):
    prozent = (punktzahl / gesamtpunktzahl) * 100
    
    if prozent >= 95:
        return "1+"
    elif prozent >= 90:
        return "1"
    elif prozent >= 85:
        return "1-"
    elif prozent >= 80:
        return "2+"
    elif prozent >= 75:
        return "2"
    elif prozent >= 70:
        return "2-"
    elif prozent >= 65:
        return "3+"
    elif prozent >= 60:
        return "3"
    elif prozent >= 55:
        return "3-"
    elif prozent >= 50:
        return "4+"
    elif prozent >= 45:
        return "4"
    elif prozent >= 40:
        return "4-"
    elif prozent >= 33:
        return "5+"
    elif prozent >= 27:
        return "5"
    elif prozent >= 20:
        return "5-"
    else:
        return "6"
    
    def vokabel_quiz(vokabeln):
    themen = set(vokabel["thema"] for vokabel in vokabeln)
    if not themen:
        print("Es sind keine Vokabeln vorhanden. Bitte erfassen Sie zunächst Vokabeln.")
        return
    
    print("Themen:")
    for i, thema in enumerate(themen, start=1):
        print(f"{i}. {thema}")
    while True:
        auswahl = input("Bitte wählen Sie ein Thema (1-{}): ".format(len(themen)))
        if not auswahl.isdigit():
            print("Bitte geben Sie eine Zahl ein.")
            continue
        auswahl = int(auswahl)
        if not 1 <= auswahl <= len(themen):
            print("Ungültige Auswahl.")
            continue
        break
    
    thema = list(themen)[auswahl-1]
    aktuelle_vokabeln = [vokabel for vokabel in vokabeln if vokabel["thema"] == thema]
    random.shuffle(aktuelle_vokabeln)
    
    input("Drücke Enter, um das Quiz zu starten...")
    
    richtig = 0
    falsch = 0
    
    for vokabel in aktuelle_vokabeln:
        clear_screen()  # Fkt. um den Bildschirm zu leeren
        deutsch = vokabel["deutsch"]
        englisch = input(f"{deutsch}: ")
        
        if englisch.lower() == vokabel["englisch"].lower():
            print("Richtig!")
            richtig += 1
        else:
            print(f"Falsch. Die richtige Antwort ist: {vokabel['englisch']}")
            falsch += 1
        
        time.sleep(1)  # Pause von 1 Sekunde machen
        input("Drücke Enter, um mit der nächsten Vokabel fortzufahren...")
            
    note = punktzahl_zu_note(richtig, len(aktuelle_vokabeln))
    print(f"Ergebnis: {richtig} von {len(aktuelle_vokabeln)} richtig")
    print(f"Das Ergebnis entspricht einer Note: {note}")
    input("Drücke Enter, um fortzufahren...")


# Funktion zum Behandeln von Fehlern
def excepthook(exc_type, exc_value, tb):
    traceback.print_exception(exc_type, exc_value, tb)
    input("Drücke Enter, um das Programm zu beenden...")

sys.excepthook = excepthook

# Hauptprogramm
vokabeln = vokabeln_laden()

while True:
    print("Bitte wählen Sie eine Option:")
    print("1. Neue Vokabeln erfassen")
    print("2. Vokabel Quiz starten")
    print("3. Programm beenden")
    
    auswahl = input("Auswahl: ")
    
    if auswahl == "1":
     vokabeln_erfassen(vokabeln)
        print(f"{len(vokabeln)} Vokabeln wurden erfasst.")
    
    elif auswahl == "2":
     vokabel_quiz(vokabeln)
    
    elif auswahl == "3":
        break
    
    else:
        print("Ungültige Auswahl. Bitte wählen Sie erneut.")
        
        input("Drücke Enter, um das Programm zu beenden...")

