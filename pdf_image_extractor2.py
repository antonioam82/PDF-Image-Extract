from tkinter import *
import zipfile
import io
from PIL import Image
import fitz

class app():
    def __init__(self):

        self.root = Tk()
        self.root.title('PDF Image Extractor')
        self.root.geometry('797x470')
        self.current_dir = StringVar()
        self.currentDir = Entry(self.root,width=132,textvariable=self.current_dir)
        self.currentDir.place(x=0,y=0)

        self.root.mainloop()

if __name__=="__main__":
    app()
