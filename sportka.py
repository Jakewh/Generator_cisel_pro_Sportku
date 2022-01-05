import inquirer, random

print(""" 
                      _   _         
 ___ _ __   ___  _ __| |_| | ____ _ 
/ __| '_ \ / _ \| '__| __| |/ / _` |
\__ \ |_) | (_) | |  | |_|   < (_| |
|___/ .__/ \___/|_|   \__|_|\_\__,_|
    |_|                             
                                                               
""")
opakovat = True
while opakovat:
    cisla = list(range(1,50))
    sloupec = 1
    # začátek menu
    otazka = [
        inquirer.List("main_menu",
        message="Co chceš losovat?",
        choices=["Celý tiket", "Sloupec"],
        ),
    ]
    odpoved = inquirer.prompt(otazka)
    # konec menu
    if odpoved == {'main_menu': 'Celý tiket'}:  # vyplnění celého tiketu
        while sloupec <= 10:
            print("Vylosovaná čísla jsou:")
            print("Sloupec ", sloupec, random.sample(cisla, 6),"\n")
            sloupec += 1
            continue    
    elif odpoved == {'main_menu': 'Sloupec'}:   # vyplnění jednoho sloupce
        print("Vylosovaná čísla jsou:")
        print(random.sample(cisla, 6))
    znovu = input("Losovat znovu? ano/ne: ")
    if znovu == "ano" or znovu == "":
        continue
    else:
        break
print("\n***Hacker Ninjas North 2022***")
input()
