# Si vuole simulare l'andamento di un'asta on line che vuole
# sperimentare una conduzione innovativa: ogni partecipante
# farà una sola offerta ed il pezzo messo all'asta sarà aggiudicato
# al partecipante la cui offerta più si avvicina alla media
# calcolata su tutte le offerte; ogni offerta sarà registrata
# come una coppia [email, offerta_in_bitcoin].
#
# Dovrà essere memorizzata una lista di tutte le offerte pervenute.

# Al termine:
# - dalla lista dovrà essere eliminata l'offerta minima e massima
# - dovrà essere costruita una seconda lista contenente
#   solo le offerte che non discostano più del 10% rispetto alla media
#   calcolata su tutte le offerte rimaste.
import re


def stampa_lista(lista_offerte):
    for offerta in lista_offerte:
        print(f"Email offerente: {offerta[0]} - offerta: {offerta[1]}")


def trova_email(email, lista_offerte):
    for offerta in lista_offerte:
        if offerta[0] == email:
            return True

    return False


def inserisci_offerte():
    lista = []
    altre_offerte = True

    while altre_offerte:
        offerta = input("Inserisci l'offerta pervenuta (0 per terminare): ")

        try:
            offerta = float(offerta)
        except ValueError:
            print("Formato non valido, riprova...")
            continue

        if offerta == 0:
            altre_offerte = False
            continue

        if offerta < 0:
            print("Non possono essere fatte offerte negative!")
            continue

        email = input("Inserire l'email dell'offerente: ")

        if (not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)):
            print("Email non valida, riprova...")
            continue

        nuova_offerta = [email, offerta]

        # da migliorare, verifica solo la stessa offerta con la stessa mail
        # if nuova_offerta in lista:
        #    print("Questo utente ha già fatto la sua unica offerta!")
        #    continue
        # else:
        #    lista.append(nuova_offerta)

        # 'finta' trova_mail, giusto per provare il resto del programma
        # restituisce sempre False
        if trova_email(email, lista):
            print("Questo utente ha già fatto la sua unica offerta")
            continue
        else:
            lista.append(nuova_offerta)

    return lista


# codice del "main":
offerte = inserisci_offerte()
stampa_lista(offerte)

