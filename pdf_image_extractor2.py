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
        self.display = slt.ScrolledText(self.root,width=70,height=18,bg='dark green',fg='lawn green')
        self.display.place(x=10,y=30)
        self.pgeslabel = Label(self.root,text="PAGES:",bg='light slate gray',fg='white')
        self.pgeslabel.place(x=600,y=38)
        self.num_pages = IntVar()
        self.pges = Entry(self.root,width=18,bg='black',fg='light green',textvariable=self.num_pages)
        self.pges.place(x=649,y=38)
        self.num_pages.set(0)
        self.pdf_name = StringVar()
        self.pdfName = Entry(self.root,width=97,bg='black',fg='light green',textvariable=self.pdf_name)
        self.pdfName.place(x=10,y=330)
        self.get_dir()
        
        self.root.mainloop()

    def get_dir(self):
        self.current_dir.set(os.getcwd())

if __name__=="__main__":
    app()



