from pathlib import Path
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import functions
from functions import *
import pandas as pd

class Visualize:
    def __init__(self,nodesPath,edgesPath,isDirected,isWeighted):

        self.nodesPath = nodesPath
        self.edgesPath = edgesPath
        self.isDirected = isDirected
        self.isWeighted = isWeighted
        self.edges = None
        self.nodes=None
        self.node_attributes =[]
        self.communities=None
        
        self.G = None
        self.createGraph()

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\Alrahma\Documents\my work\AI project\socialNetwork analysis\Social Media tool\frame3")
        #read data
        self.window = Tk(baseName="GraphBase",screenName="GraphScreen")
       
        self.canvas1 = Canvas(self.window,bg = "#D4D4D4",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")

        self.Visualize_image_1 = PhotoImage(file=self.relative_to_assets("Run_1.png"))
        self.Visualize_1 = Button(self.window,borderwidth=5,text='Visualize',font=20,bg="teal",command=lambda: functions.drawGraph(self.G,window=self.window),relief="flat")

        self.linkpred_image_2 = PhotoImage(file=self.relative_to_assets("Run_1.png"))
        self.linkpred_2 = Button(self.window,borderwidth=5,text='Show',font=20,bg="teal",command=lambda:functions.linkprediction(self.G,self.window),relief="flat")

        self.louvian_image_3 = PhotoImage(file=self.relative_to_assets("Run_1.png"))
        self.louvian_3 = Button(self.window,borderwidth=5,text='Run',font=20,bg="teal",command=lambda:self.get_community(),relief="flat")


        self.filter_options=['Defult','Node Degree']
        self.filter_options.append(list(self.edges.columns[2:len(self.edges.columns)]))
        self.selected_filter = StringVar(self.window)
        self.adjust_dropdown = OptionMenu(self.canvas1, self.selected_filter, *self.filter_options,command=self.adjust_graph)
        self.centrality_dropdown_window = self.canvas1.create_window( 1090,70.0, anchor=NW, window=self.adjust_dropdown)

        self.centrality_options = ["None","Closeness Centrality", "Betweenness centrality", "Harmonic centrality"]
        self.selected_centrality = StringVar(self.window)
        self.centrality_dropdown = OptionMenu(self.canvas1, self.selected_centrality, *self.centrality_options,command=self.filtergraph)
        self.centrality_dropdown_window = self.canvas1.create_window(1090,220.0, anchor=NW, window=self.centrality_dropdown)

        self.Evaluation_options = ["None","Average NodeDgree", "Conductance", "NMI"]
        self.selected_Evaluation = StringVar(self.window)
        self.Evaluation_dropdown = OptionMenu(self.canvas1, self.selected_Evaluation, *self.Evaluation_options,command=self.communityevaluation)
        self.Evaluation_dropdown_window = self.canvas1.create_window(1090,370.0, anchor=NW, window=self.Evaluation_dropdown)



        self.startScreen()

        self.window.resizable(False, False)
        self.window.mainloop()


    def startScreen(self):

        self.window.geometry("1280x720")
        self.window.configure(bg = "#D4D4D4")

      

        self.canvas1.place(x = 0, y = 0)
        self.canvas1.create_text(30.0,32.0,anchor="nw",text="Network Analysis",fill="#000000",font=("IstokWeb Regular", 40 * -1))



        self.canvas1.create_text(874.0,70.0,anchor="nw",text="Adjustment Graph ",fill="#000000",font=("Inter", 25 * -1))
        self.canvas1.create_text(874.0,370.0,anchor="nw",text="Evaluation Graph ",fill="#000000",font=("Inter", 25 * -1))
        self.canvas1.create_text(874.0,220.0,anchor="nw",text="Filter Graph ",fill="#000000",font=("Inter", 25 * -1))
        self.canvas1.create_text(874.0,520.0,anchor="nw",text="Link Prediction",fill="#000000",font=("Inter", 25 * -1))
        self.canvas1.create_text(874.0,660.0,anchor="nw",text="Louvain Algorithm ",fill="#000000",font=("Inter", 25 * -1))
        self.canvas1.create_text(328.0,572.0,anchor="nw",text="Visualize Network",fill="#000000",font=("Inter", 25 * -1))

        self.Visualize_1.place(x=390.0,y=626.0,width=88.02920532226562,height=36.22291564941406,)
        self.linkpred_2.place(x=1147.518310546875,y=509.94122314453125,width=88.0291748046875,height=36.22291564941406,)
        self.louvian_3.place(x=1147.518310546875,y=660.0,width=88.0291748046875,height=36.22291564941406)

        self.canvas1.create_text(30.0,682.0,anchor="nw",text="Powered by NetworkX Tkinter ",fill="teal",font=("Inter", 20 * -1))
        
        self.selected_filter.set(self.filter_options[0])
        self.adjust_dropdown.config(width=20,bg="teal")
        self.selected_centrality.set(self.centrality_options[0])
        self.centrality_dropdown.config(width=20,bg="teal")
        self.selected_Evaluation.set(self.Evaluation_options[0])
        self.Evaluation_dropdown.config(width=20,bg="teal")
      

    def createGraph(self):
        self.edges =pd.read_csv(self.edgesPath)
        self.nodes=pd.read_csv(self.nodesPath)
        if self.isDirected ==1:
            self.G=nx.DiGraph()
        else :
            self.G=nx.Graph()

         # Add nodes from the node list DataFrame
        for i, node in self.nodes.iterrows():
            self.G.add_node(node[0])

        lenght=len(self.nodes.columns)
        for i in range(1,lenght):
            dic=dict(zip(self.nodes[self.nodes.columns[0]], self.nodes[self.nodes.columns[i]]))
            nx.set_node_attributes(self.G, dic,self.nodes.columns[i])
            self.node_attributes.append(self.nodes.columns[i])    

        # Add edges from the edge list DataFrame
        wieght=[]
        for i, edge in self.edges.iterrows():
            self.G.add_edge(edge[0], edge[1])
            wieght.append((edge[0], edge[1]))
            
        print(wieght)
        lenght=len(self.edges.columns)
        for i in range(2,lenght):
            #d = self.G.set_index([self.edges[self.edges.columns[i]], self.edges[self.edges.columns[i]]])['cost'].reindex(index=link).to_dict()
            dic=dict(zip(wieght, self.edges[self.edges.columns[i]]))
            
            nx.set_edge_attributes(self.G, dic,self.edges.columns[i])    

        
        # remove rows with null values
        self.edges = self.edges.dropna(axis=0)
        self.edges = self.edges.dropna(axis=0)
        #xmin = min(edge['Source'].tolist())
        #xmax = max(edge['Source'].tolist())
        #ymin = min(edge['Target'].tolist())
        #ymax = max(edge['Target'].tolist())
        #x_mid = (xmin + xmax) / 2
        #y_mid = (ymin + ymax) / 2
        #plt.xlim(x_mid - 1280/2, x_mid + 1280/2)
        #plt.ylim(y_mid - 720/2, y_mid + 720/2)



    def get_community(self):
        self.communities= luovian_communityDetection(self.G,self.window)
  
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def adjust_graph(self, value):
    
        if value == self.filter_options[1]:
            draw_nodeDegree(self.G,self.window)
        else :
            draw_edge_weight(self.G,self.window,value[0])


    def filtergraph(self, value):
        if value == self.centrality_options[1]:
            draw_closeness_centrality(self.G,self.window)
        elif value== self.centrality_options[2]:
            draw_betweenness_centrality(self.G,self.window)
        elif value == self.centrality_options[3]:
            draw_harmonic_centrality(self.G,self.window)


    def communityevaluation(self, value):
        if value == self.Evaluation_options[1]:
            Average_Nodedgree(self.G,self.communities[1])
        elif value== self.Evaluation_options[2]:
            Conductance(self.G,self.communities[1])
        elif value == self.Evaluation_options[3]:
            normalized_mutual_info(self.G,self.communities,self.node_attributes[0])



    def __del__(self):
        print("Destroying instance of MyClass")

   