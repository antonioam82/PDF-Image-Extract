from tkinter import *
import zipfile
import io
from PIL import Image
import fitz

class app():
    def __init__(self):

        self.root = Tk()
        self.root.title('PDF Image Extractor')
        self.root.geometry('800x470')

        self.root.mainloop()

if __name__=="__main__":
    app()
