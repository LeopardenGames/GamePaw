def ask_questions():
    answers = {}
    
    # Fragen an den Benutzer stellen
    answers['Username'] = input("Set Username")
    answers['Passwort'] = input("Set Passwort")
    
    return answers

def write_conf_file(filename, answers):
    with open(filename, 'w') as f:
        for key, value in answers.items():
            f.write(f"{key} = {value}\n")

if __name__ == "__main__":
    user_answers = ask_questions()
    write_conf_file('config/user_info.conf', user_answers)
    print("Die Antworten wurden in 'user_info.conf' gespeichert.")
