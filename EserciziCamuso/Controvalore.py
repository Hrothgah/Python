print("Digita l'anno di acquisto del titolo")
annoDeposito = int(input())
print("Digita l'importo del titolo")
importoDeposito = int(input())
print("Digita il tasso di interessi")
tassoInteressi = int(input())
annoCorrente = 2016
controValore = importoDeposito

anniTrascorsi = annoCorrente - annoDeposito

for i in range(0, anniTrascorsi):
    controValore = ((importoDeposito * tassoInteressi)/100) + controValore


print("Il controvalore al 2016 di questo titolo è")
print(str(controValore) + "0 €")
