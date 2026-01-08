#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def show_menu():
    """Zeigt das Hauptmenü an"""
    print("\n" + "=" * 50)
    print("         INTERAKTIVES PROGRAMM")
    print("=" * 50)
    print("1. Willkommen anzeigen")
    print("2. Text eingeben und ausgeben")
    print("3. Mathe-Rechner")
    print("4. Liste erstellen")
    print("5. Aktuelle Zeit anzeigen")
    print("0. Beenden")
    print("=" * 50)

def welcome():
    """Zeigt eine Willkommensmeldung"""
    print("\n👋 Willkommen zu diesem interaktiven Programm!")
    print("📋 Hier kannst du verschiedene Funktionen ausprobieren.")

def text_echo():
    """Benutzer gibt Text ein und dieser wird ausgegeben"""
    text = input("\n📝 Gib einen Text ein: ")
    print(f"✅ Du hast eingegeben: {text}")

def calculator():
    """Einfacher Taschenrechner"""
    print("\n🧮 TASCHENRECHNER")
    try:
        num1 = float(input("   Erste Zahl: "))
        operation = input("   Operation (+, -, *, /): ")
        num2 = float(input("   Zweite Zahl: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("   ❌ Fehler: Division durch Null nicht möglich!")
                return
            result = num1 / num2
        else:
            print("   ❌ Ungültige Operation!")
            return
        
        print(f"   📊 Ergebnis: {num1} {operation} {num2} = {result}")
    except ValueError:
        print("   ❌ Fehler: Bitte gültige Zahlen eingeben!")

def list_creator():
    """Erstellt eine Liste mit Benutzer-Eingaben"""
    print("\n📚 LISTENERSTELLUNG")
    items = []
    print("   Gib Einträge ein (leere Eingabe zum Beenden):")
    
    while True:
        item = input(f"   Eintrag {len(items) + 1}: ")
        if not item:
            break
        items.append(item)
    
    if items:
        print("\n   ✅ Deine Liste:")
        for i, item in enumerate(items, 1):
            print(f"      {i}. {item}")
    else:
        print("   ℹ️  Keine Einträge hinzugefügt.")

def show_time():
    """Zeigt aktuelle Zeit an"""
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d.%m.%Y")
    print(f"\n🕐 Aktuelle Zeit: {current_time}")
    print(f"📅 Heutiges Datum: {current_date}")

def main():
    """Hauptprogramm mit Menüschleife"""
    print("\n🚀 Programm gestartet...")
    
    while True:
        show_menu()
        choice = input("Wähle eine Option (0-5): ").strip()
        
        if choice == '1':
            welcome()
        elif choice == '2':
            text_echo()
        elif choice == '3':
            calculator()
        elif choice == '4':
            list_creator()
        elif choice == '5':
            show_time()
        elif choice == '0':
            print("\n👋 Auf Wiedersehen!")
            break
        else:
            print("\n❌ Ungültige Option! Bitte wähle 0-5.")

if __name__ == "__main__":
    main()