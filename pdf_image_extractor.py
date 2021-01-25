import fitz
import io
import os
from PIL import Image
import zipfile
from VALID import ns

while True:
    dire = input("Introducir directorio: ")
    os.chdir(dire)
    file = input("Introduce archivo PDF: ")

    pdf_file = fitz.open(file)
    print('{} Páginas'.format(len(pdf_file)))

    conti = ns(input("¿Continuar(n/s)?: "))
    if conti == "n":
        break
