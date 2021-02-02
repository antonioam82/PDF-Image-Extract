from tkinter import *
from tkinter import filedialog
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
        self.root.geometry('782x450')
        self.root.configure(bg='light slate gray')
        self.current_dir = StringVar()
        self.canvas = Canvas(self.root,width=157,height=290)
        self.canvas.place(x=603,y=100)
        self.scrollbar = Scrollbar(self.canvas,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        
        self.pages_box = Listbox(self.canvas,width=23,height=19)
        self.pages_box.pack()
        self.pages_box.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.pages_box.yview)
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
        self.listlabel = Label(self.root,text="PAGE\S TO EXTRACT FROM:",bg='light slate gray',fg='white')
        self.listlabel.place(x=601,y=77)
        self.pdfName = Entry(self.root,width=45,bg='black',fg='light green',font=('arial',14),textvariable=self.pdf_name)
        self.pdfName.place(x=90,y=328)
        self.btnSearch = Button(self.root,text="SEARCH PDF",bg="gold3",command=self.load_pdf)
        self.btnSearch.place(x=10,y=328)
        self.btnExtract = Button(self.root, text="EXPORT TO CURRENT DIR",bg="PaleGreen1",width=81)
        self.btnExtract.place(x=10,y=370)
        self.btnExtractZip = Button(self.root,text="EXPORT TO ZIP",bg="PaleGreen1",width=81)
        self.btnExtractZip.place(x=10,y=409)
        self.btnSelect = Button(self.root,text="SELECT",width=21,bg="gold3")
        self.btnSelect.place(x=604,y=409)
        self.get_dir()
        
        self.root.mainloop()

    def get_dir(self):
        self.current_dir.set(os.getcwd())

    def load_pdf(self):
        pdf_root = filedialog.askopenfilename(initialdir="/",title="SELECT PDF", filetypes=(("PDF files","*.pdf"),("all files","*.*")))
        if pdf_root != "":
            self.display.insert(END,pdf_root+"\n")
            self.name = (pdf_root.split("/")[-1])
            pdf_file = fitz.open(pdf_root)
            self.pdf_name.set(self.name)
            self.num_pages.set(len(pdf_file))
            self.view_pages()

    def view_pages(self):
        #print(self.num_pages.get())
        for i in range(self.num_pages.get()):
            self.pages_box.insert(END,"PAGE: {}\n".format(i))
        self.pages_box.insert(END,"ALL PAGES")
            
if __name__=="__main__":
    app()





