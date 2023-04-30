from pathlib import Path
from tkinter import filedialog #for Python 3
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import functions
from functions import *
import GraphScreen
from GraphScreen import Visualize


class DataReader:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\Alrahma\Documents\my work\AI project\socialNetwork analysis\Social Media tool\frame0")

        self.window = Tk(baseName="MainBase",screenName="MainScreen")
        self.canvas2 = Canvas(self.window,bg = "#E7DCDC",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")

        self.isdirected = tk.IntVar()
        self.chkdir = tk.Checkbutton(self.window,bg="teal", text='Directed Graph',font=10, variable=self.isdirected)

        self.isweighted = tk.IntVar()
        self.chkwe = tk.Checkbutton(self.window,bg="teal", text='Weighted Graph',font=10, variable=self.isweighted)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas2.create_image(640.5,259.5,image=self.entry_image_1)
        self.entry_1 = Entry(bd=0,bg="teal",fg="#000716",highlightthickness=0)

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas2.create_image(640.5,406.5,image=self.entry_image_2)
        self.entry_2 = Entry(bd=0,bg="teal",fg="#000716",highlightthickness=0)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.button_image_1,borderwidth=0,highlightthickness=0,command=lambda : self.submit() ,relief="flat")

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.button_image_2,borderwidth=0,highlightthickness=0,command=lambda: self.settext(1),relief="flat")

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(image=self.button_image_3,borderwidth=0,highlightthickness=0,command=lambda: self.settext(2),relief="flat")
    
        self.startScreen()

        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def startScreen(self):
        self.window.geometry("1280x720")
        self.window.configure(bg = "#E7DCDC")

        self.canvas2.place(x = 0, y = 0)
        self.canvas2.create_text(380.0,37.0,anchor="nw",text="Welcome To Network Analysis Tool",fill="#000000",font=("Inter Bold", 36 * -1))
        self.canvas2.create_text(470,150,anchor="nw",text="Enter the path of the data to continue",fill="teal",font=("Inter Regular", 20 * -1))
        self.canvas2.create_text(113.0,237.0,anchor="nw",text="Edge Data",fill="#000000",font=("Inter Regular", 40 * -1))
        self.canvas2.create_text(113.0,375.0,anchor="nw",text="Node Data",fill="#000000",font=("Inter Regular", 40 * -1))
        self.canvas2.create_text(113.0,497.0,anchor="nw",text="Graph Type:",fill="#000000",font=("Inter Regular", 40 * -1))

        self.chkdir.place(x=400,y=500) #Directed
        self.chkwe.place(x=800,y=500) #Weighted

        self.entry_1.place(x=454.0,y=243.0,width=373.0,height=31.0) #Nodes
        self.entry_2.place(x=454.0,y=390.0,width=373.0,height=31.0) #Edges

        self.button_1.place(x=508.0,y=610.0,width=288.0,height=68.0)
        self.button_2.place(x=929.0,y=243.0,width=164.0,height=33.0)
        self.button_3.place(x=928.0,y=394.0,width=164.0,height=33.0)

    # ------------------------- Function ------------------------------

# entry_1 --> Edges
# entry_2 --> Nodes

### File Path
    def getfilepath(self):
        path=filedialog.askopenfilename()
        return path 
    def settext(self,val):
        path=self.getfilepath()
        if val==1:
            self.entry_1.delete(0,tk.END)
            self.entry_1.insert(0,path)
        if val==2:
            self.entry_2.delete(0,tk.END)
            self.entry_2.insert(0,path)


    ## Submit 
    def submit(self):
        # entry_1 -> nodesPath   entry_2 -> edgesPath   isdirected  sweighted 
        obj = GraphScreen.Visualize(nodesPath = self.entry_2.get(), edgesPath= self.entry_1.get(),isDirected = self.isdirected.get(), isWeighted = self.isweighted.get())
        self.window.destroy()

    def __del__(self):
        self.window.destroy()


var = DataReader()