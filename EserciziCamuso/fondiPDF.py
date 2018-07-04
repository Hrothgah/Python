# fonde due o più file pdf in uno solo
import PyPDF2

pdfFile1 = open("Doc/doc1.pdf", "rb")  # r=read, b=binary
reader1 = PyPDF2.PdfFileReader(pdfFile1)
print(reader1.numPages)

# copiamo il pdf in un altro replicando 3 volte l'unica pagina
pdfFile2 = open("Doc/doc1Copia_x6.pdf", "wb")  # W=write, b=binary
writer1 = PyPDF2.PdfFileWriter()

# for numeroPagina in range(reader1.numPages):
#     writer1.addPage(reader1.getPage(numeroPagina))

writer1.addPage(reader1.getPage(0))
writer1.addPage(reader1.getPage(0))
writer1.addPage(reader1.getPage(0))
writer1.addPage(reader1.getPage(0))
writer1.addPage(reader1.getPage(0))
writer1.addPage(reader1.getPage(0))


writer1.write(pdfFile2)
pdfFile1.close()
pdfFile2.close()
