from tkinter import *
from tkinter import filedialog, messagebox
#import tkinter.scrolledtext as slt
import zipfile
import Pmw
import io
import os
import threading
from PIL import Image
import fitz

class app():
    def __init__(self):

        self.root = Tk()
        self.root.title('PDF Image Extractor')
        self.root.geometry('774x420')
        self.root.configure(bg='light slate gray')
        self.current_dir = StringVar()
        self.canvas = Canvas(self.root,width=157,height=290)
        self.canvas.place(x=603,y=100)
        self.scrollbar = Scrollbar(self.canvas,orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.selected_pages = []
        self.name = ""
        self.to_zip = []
        self.pdf_file = ""
        self.pages_box = Listbox(self.canvas,width=23,height=17)
        self.pages_box.pack()
        self.pages_box.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command = self.pages_box.yview)
        self.currentDir = Entry(self.root,width=132,textvariable=self.current_dir)
        self.currentDir.place(x=0,y=0)
        #self.display = slt.ScrolledText(self.root,width=70,height=18,bg='dark green',fg='lawn green')
        #self.display.place(x=10,y=30)
        self.display = Pmw.ScrolledText(self.root,text_width=70,text_height=16,hscrollmode='none',vscrollmode='dynamic',
                                        text_background='dark green',text_foreground='lawn green')
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
        self.pdfName.place(x=90,y=333)
        self.btnSearch = Button(self.root,text="SEARCH PDF",bg="gold3",command=self.load_pdf)
        self.btnSearch.place(x=10,y=333)
        self.btnExtract = Button(self.root, text="EXPORT TO CURRENT DIR",bg="PaleGreen1",width=39,command=lambda:self.init_extract(False))
        self.btnExtract.place(x=10,y=377)
        self.btnExtractZip = Button(self.root,text="EXPORT TO ZIP",bg="PaleGreen1",width=38,command=lambda:self.init_extract(True))
        self.btnExtractZip.place(x=318,y=377)
        self.btnSelect = Button(self.root,text="SELECT",width=21,bg="gold3",command=self.select_page)
        self.btnSelect.place(x=604,y=377)
        self.btnClear = Button(self.root,text="CLEAR ALL",width=82,bg="light gray",command=self.clear_all)
        self.btnClear.place(x=10,y=291)
        self.get_dir()
        
        self.root.mainloop()

    def get_dir(self):
        self.current_dir.set(os.getcwd())

    def clear_all(self):
        self.selected_pages = []
        self.display.delete('1.0',END) 

    def load_pdf(self):
        pdf_root = filedialog.askopenfilename(initialdir="/",title="SELECT PDF", filetypes=(("PDF files","*.pdf"),("all files","*.*")))
        self.pages_box.delete(0, END)
        if pdf_root != "":
            try:
                self.name = (pdf_root.split("/")[-1])
                self.display.appendtext('PDF TITTLE: {}.\n'.format(self.name)) 
                os.chdir("/".join(pdf_root.split("/")[:-1]))#################
                self.pdf_file = fitz.open(pdf_root)
                self.pdf_name.set(self.name)
                self.num_pages.set(len(self.pdf_file))
                self.view_pages()
                self.get_dir()###############################################
            except Exception as e:
                print(str(e))
                messagebox.showwarning("ERROR","Can't open the file")

    def view_pages(self):
        for i in range(self.num_pages.get()):
            self.pages_box.insert(END,"PAGE: {}\n".format(i+1))
        self.pages_box.insert(END,"ALL PAGES")

    def select_page(self):
        try:
            pdf_index = self.pages_box.curselection()[0]
            if pdf_index not in self.selected_pages:
                #self.selected_pages = []######################
                if pdf_index == self.num_pages.get():
                    for i in range(self.num_pages.get()):
                        self.selected_pages.append(i)
                    dis_text = "ALL PAGES SELECTED\n"
                else:
                    dis_text = "SELECTED PAGE {}\n".format(pdf_index+1)
                    self.selected_pages.append(pdf_index)
                self.selected_pages.sort()
                self.display.appendtext(dis_text)
        except Exception as e:
            print(str(e))
            if self.pdf_file == "":
                messagebox.showwarning("ERROR","Search a PDF file.")
            else:
                messagebox.showwarning("ERROR","Select page\s to extract from.")

    def make_zip(self):
        if self.name != "":
            final_name,ex = os.path.splitext(self.name)
            with zipfile.ZipFile(final_name+".zip",'w') as zip_file:
                for i in self.to_zip:
                    zip_file.write(i)
                    os.remove(i)
            zip_file.close()
            #self.display.insert(END,"CREATED ZIP FILE.")
            self.display.appendtext("\nCREATED ZIP FILE {}".format(final_name+".zip\n"))
            self.display.appendtext("\nTASK COMPLETED.\n")
            self.to_zip = []
            
    def extract(self,z):
        if len(self.selected_pages) > 0:
            for p in self.selected_pages:
                page = self.pdf_file[p]
                image_list = page.getImageList()
                if len(image_list)>0:
                    count = 0
                    for image_index, img in enumerate(image_list, start=1):
                        xref = img[0]
                        base_image = self.pdf_file.extractImage(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]
                        image = Image.open(io.BytesIO(image_bytes))
                        image_name = ("image{}_{}.{}".format(p+1,count,image_ext))
                        self.to_zip.append(image_name)
                        image.save(open(image_name,"wb"))
                        self.display.appendtext("Extracted image {} from page {}.\n".format(count,p+1))
                        count+=1
                else:
                    self.display.appendtext("No images on page {}.\n".format(p+1))
        
            if z==True:
                self.make_zip()
            else:
                self.display.appendtext("\nTASK COMPLETED.\n")
            
            self.selected_pages = []

    def init_extract(self,tz):
        t = threading.Thread(target=self.extract(tz))
        t.start()
        
if __name__=="__main__":
    app()






