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
    images = []

    pdf_file = fitz.open(file)
    print('{} Páginas'.format(len(pdf_file)))
    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.getImageList()
        if image_list:
            print('{} imágenes encontradas en la página {}'.format(len(image_list),page_index))
        else:
            print('0 imágenes encontradas en la página {}'.format(page_index))
        for image_index, img in enumerate(page.getImageList(), start=1):
            xref = img[0]
            base_image = pdf_file.extractImage(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image_name = (f"image{page_index+1}_{image_index}.{image_ext}")
            image.save(open(image_name,"wb"))
            images.append(image_name)
            print(images)

    with zipfile.ZipFile("images.zip","w") as zfile:
        for i in images:
            zfile.write(i)
            os.remove(i)
    zfile.close()

    conti = ns(input("¿Continuar(n/s)?: "))
    if conti == "n":
        break
