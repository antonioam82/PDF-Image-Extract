from tkinter import *
import tkinter.scrolledtext as slt
import zipfile
import io
import os
from PIL import Image
import fitz

class app():
    def __init__(self):

        self.root = Tk()
        self.root.title('PDF Image Extractor')
        self.root.geometry('790x470')
        self.root.configure(bg='light slate gray')
        self.current_dir = StringVar()
        self.currentDir = Entry(self.root,width=132,textvariable=self.current_dir)
        self.currentDir.place(x=0,y=0)
        self.display = slt.ScrolledText(self.root,width=70,height=18,bg='blue',fg='light green')
        self.display.place(x=10,y=30)

        self.get_dir()
        
        self.root.mainloop()

    def get_dir(self):
        self.current_dir.set(os.getcwd())

if __name__=="__main__":
    app()

