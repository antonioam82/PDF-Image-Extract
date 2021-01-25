import fitz
import io
import os
from PIL import Image
import zipfile
from VALID import ns

def check_dir():
    while True:
        direc = input("Introducir directorio: ")
        if os.path.isdir(direc):
            break
        else:
            print("DIRECTORIO NO VÁLIDO.")
    return direc

def check_file():
    while True:
        filen = input("Introduce archivo PDF: ")
        if filen in os.listdir() and filen.endswith(".pdf"):
            break
        else:
            print("ARCHIVO NO VÁLIDO.")
    return filen

while True:
    dire = check_dir()
    os.chdir(dire)
    file = check_file()
    images = []

    pdf_file = fitz.open(file)
    print('{} Páginas'.format(len(pdf_file)))
    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.getImageList()
        print('{} imágenes encontradas en la página {}'.format(len(image_list),page_index))
        
        for image_index, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image_name = (f"image{page_index+1}_{image_index}.{image_ext}")
            image.save(open(image_name,"wb"))
            images.append(image_name)

    with zipfile.ZipFile("images.zip","w") as zfile:
        for i in images:
            zfile.write(i)
            os.remove(i)
    zfile.close()

    conti = ns(input("¿Continuar(n/s)?: "))
    if conti == "n":
        break
