import getpass
import os
import json
from colorama import init, Fore, Style

# Initialisiere colorama
init()

def prompt_user_for_info():
    """Fragt den Benutzer nach seinen Registrierungsdaten und gibt ein Dictionary zurück."""
    print(Fore.CYAN + "Willkommen zur Benutzerregistrierung!" + Style.RESET_ALL)
    
    username = input(Fore.GREEN + "Benutzername: " + Style.RESET_ALL)
    
    # Passwort eingeben
    password = getpass.getpass(Fore.GREEN + "Passwort: " + Style.RESET_ALL)
    confirm_password = getpass.getpass(Fore.GREEN + "Passwort bestätigen: " + Style.RESET_ALL)
    
    if password != confirm_password:
        print(Fore.RED + "Die Passwörter stimmen nicht überein. Versuche es erneut." + Style.RESET_ALL)
        return None
    
    email = input(Fore.GREEN + "E-Mail-Adresse: " + Style.RESET_ALL)
    
    return {
        'username': username,
        'password': password,
        'email': email
    }

def save_to_conf_file(data, filename='user_info.conf'):
    """Speichert die Benutzerdaten in einer .conf-Datei im JSON-Format."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(Fore.BLUE + f"Die Daten wurden in '{filename}' gespeichert." + Style.RESET_ALL)

def main():
    user_data = prompt_user_for_info()
    if user_data:
        save_to_conf_file(user_data)

if __name__ == "__main__":
    main()
