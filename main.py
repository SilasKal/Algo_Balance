def balance(data_string):
    stapel = []  # Stapel erstellen
    balanced = 1
    for klammer in data_string:  # Gehe durch den Stapel durch
        if klammer == '(' or klammer == '[':
            stapel.append(klammer)
            # Wenn Klammer auf geht, füge sie an den Stapel an.
        elif (klammer == ')' or klammer == ']') and not stapel:
            balanced = 0
        else:
            # Klammer geht zu
            if stapel:
                # Wenn der Stapel nicht leer ist:
                top = stapel[-1]
                if klammer == ')' and top == '(' or klammer == ']' \
                        and top == '[':
                    stapel.pop()
                    # schaue ob bereits geöffnete Klammer geschlossen wird und
                    # entferne ggf. Paar. sonst wähle nächste Klammer aus Input
                else:
                    balanced = 0
    if not stapel and balanced:
        print("1")
        # Stapel ist leer und es wurden alle Klammern gematcht: 1
    else:
        print("0")
        # Es bleiben Klammern übrig die nicht gematcht wurden: 0

with open(r'balance2.txt') as data:
    for line in data:
        line = line.strip()
        balance(line)
    # Entfernen der Leerzeichen und Aufruf der Funktion balance zeilenweise
