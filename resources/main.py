from browser import document, bind, html

@bind("#add-form", "submit")
def match(event):
    # Verhindert das Neuladen der Seite
    event.preventDefault()

    sportarten = ["laufen","gewichtheben","schwimmen","fahrradfahren","wandern"]
    global user
    user = []
    userbase = []

    # Auslesen und verarbeiten der Beispieldaten
    
    input = open("resources/matches.txt", "r")
    for line in input:
        userbase.append(line.split())


    # Werte aus den Eingabefeldern abrufen
    name = document["name"].value
    user.append(name)
    for sport in sportarten:
        if document[sport].checked == True:
            user.append('1')
        else:
            user.append('0')
    

    # Matching durchführen
    global matches
    matches = []
    for list in userbase:
        score = 0
        count = 0
        match = []
        common_sport = []
        for i in range(1,len(list)):
            if list[i] == '1' and list[i] == user[i]:
                score += 1
                common_sport.append(sportarten[i-1])
            if list[i] == '1':
                count += 1
            elif user[i] == '1':
                count += 1
        ergebnis = int(score*100/count)
        if ergebnis > 0:
            match.append(ergebnis)
            match.append(list[0])
            match.append(common_sport)    
            matches.append(match)
    matches.sort(reverse=True)

    if len(matches) == 0:
        document['anleitung'].text = "Bitte wähle mindestens eine Sportart aus."
    else:
        update_display()

current_index = 0

# Funktion zum Aktualisieren des angezeigten Eintrags
def update_display():
    display_element = document['match']
    common = ""
    if matches and len(matches) > 0:  # Überprüfen, ob die Liste nicht leer ist
        document['anleitung'].text = f"Hi {user[0]}! Deine Matches:"
        display_element.text = f"{matches[current_index][1]} {matches[current_index][0]} %"
        document['image'].attrs['src'] = f"./resources/images/{matches[current_index][1].lower()}.png"
        for sport in matches[current_index][2]:
            if sport != matches[current_index][2][-1]:
                common += f"{sport.capitalize()} | "
            else:
                common += f"{sport.capitalize()}"
        document['common_sport'].text = common

# Funktion, um zum nächsten Eintrag zu navigieren
def next_entry(event):
    global current_index
    if current_index < len(matches) - 1:
        current_index += 1
    else:
        current_index = 0  # Zurück zum Anfang
    update_display()

# Funktion, um zum vorherigen Eintrag zu navigieren
def prev_entry(event):
    global current_index
    if current_index > 0:
        current_index -= 1
    else:
        current_index = len(matches) - 1  # Zum letzten Eintrag
    update_display()

def dark_mode(event):
    if document['dark_mode'].text == f'dark mode':
        document['dark_mode'].text = f'light mode'
        document['sun_moon'].text = f'☼'
    else:
        document['dark_mode'].text = f'dark mode'
        document['sun_moon'].text = f'☾'

# Event-Listener für die Buttons
document['next-button'].bind('click', next_entry)
document['prev-button'].bind('click', prev_entry)
document['dark_mode'].bind('click', dark_mode)
document['sun_moon'].bind('click', dark_mode)
# Initiales Setup
update_display()