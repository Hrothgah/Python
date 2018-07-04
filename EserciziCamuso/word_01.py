import docx

divina = docx.Document("Doc/divina1.docx")

sezioni = divina.sections
print("Il documento contiene: ", end="")
print("{0} sezione/i".format(len(sezioni)), end="")

paragrafi = divina.paragraphs
print(" e {0} paragrafo/i\n".format(len(paragrafi)))

for p in paragrafi:
    print(p.text)
    print("-"*40)

# esempio di creazione di una lista
miaLista = []

# lista che contiene il primo e l'ultimo paragrafo del docx in esame
primoEultimo = [paragrafi[0], paragrafi[-1]]  # invece che fare n-1 per l'ultimo paragrafo
# in python si possono usare indici negativi, -1 è l'ultimo elemento, -2 il penultimo etc

# altro modo di istanziare una lista con lo slicing indico il primo indice e l'utimo (escluso)
secondoEterzo = paragrafi[1:3]

# esempio con primo indice mancante, quindi parte dall'inizio
primi3 = paragrafi[:3]

# esempio con secondo indice mancante, quindi arriva alla fine
ultimi2 = paragrafi[-2:]

# esempio con 3 indici, l'inizio, la fine e il passo (inizio e fine omessi, parte dall'inizio e
# finisce alla fine
pari = paragrafi[::2]

# esempio con nessun indice
tutti = paragrafi[:]
