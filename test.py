import random

Numero = random.randint(1, 100)

input_utente = input("Indovina il numero:")
tentativo = int(input_utente)
numero_di_tentativi = 10

for i in range(numero_di_tentativi):

    if tentativo > Numero:
        print("Minore")
    else:
        print("Maggiore")

    input_utente = input("Riprova:")
    tentativo = int(input_utente)

    if tentativo == Numero:
        print("Hai Vinto!")
        break
    if i == (numero_di_tentativi - 1):
        print("Hai Perso!")

input("Premere qualsiasi tasto per chiudere.")
    

