# fonde in un solo file tutti i pdf trovati nella cartella di lavoro "Fusione"
import PyPDF2
import os

# elenco di files e cartelle dentro la cartella Fusione
listaFiles = os.listdir("Fusione")

# apriamo in scrittura il file pdf in cui fondere gli altri
print("Digita il nome per il file di destinazione:")
nomeFileDestinazione = input()
PDF_Destinazione = open(nomeFileDestinazione, "wb")
merger = PyPDF2.PdfFileMerger()

for nomeFile in listaFiles:
    # controllo se l'oggetto è un file e se (dopo aver impostato il nome in maiuscolo)
    # finisce con .PDF
    if os.path.isfile(nomeFile) and nomeFile.upper().endswith(".PDF"):
        pdfFile = open(nomeFile, "rb")
        readerPDF = PyPDF2.PdfFileReader(pdfFile)
        merger.append(readerPDF)
        pdfFile.close()

merger.write(PDF_Destinazione)
PDF_Destinazione.close()

#print(listaFiles)
