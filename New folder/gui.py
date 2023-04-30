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
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\youssef\4.2\social\task\Code\Social Media tool\frame3")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#D4D4D4")


# Generate a random graph
G = nx.Graph()

G.add_edge("a", "b", weight=300)
G.add_edge("a", "c", weight=25)
G.add_edge("c", "d", weight=10)
G.add_edge("c", "e", weight=5)
G.add_edge("c", "f", weight=50)
G.add_edge("a", "d", weight=30)



canvas = Canvas(
    window,
    bg = "#D4D4D4",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

canvas.create_text(
    30.0,
    32.0,
    anchor="nw",
    text="Network Analysis",
    fill="#000000",
    font=("IstokWeb Regular", 40 * -1)
)



canvas.create_text(
    874.0,
    69.0,
    anchor="nw",
    text="Adjustment Graph ",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    874.0,
    251.0,
    anchor="nw",
    text="Filter Graph ",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    873.649658203125,
    515.978271484375,
    anchor="nw",
    text="Link Prediction",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    873.649658203125,
    596.4736938476562,
    anchor="nw",
    text="Louvain Algorithm ",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    328.0,
    572.0,
    anchor="nw",
    text="Visualize Network",
    fill="#000000",
    font=("Inter", 25 * -1)
)

Visualize_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
Visualize_1 = Button(
    image=Visualize_image_1,
    borderwidth=10,
    highlightthickness=10,
    command=lambda: functions.drawGraph(G,window=window),
    relief="flat"
)
Visualize_1.place(
    x=390.0,
    y=626.0,
    width=88.02920532226562,
    height=36.22291564941406
)

linkpred_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
linkpred_2 = Button(
    image=linkpred_image_2,
    borderwidth=10,
    highlightthickness=10,
    command=lambda:functions.linkprediction(G),
    relief="flat"
)
linkpred_2.place(
    x=1147.518310546875,
    y=509.94122314453125,
    width=88.0291748046875,
    height=36.22291564941406,
)

louvian_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
louvian_3 = Button(
    image=louvian_image_3,
    borderwidth=10,
    highlightthickness=10,
    command=lambda: luovian_communityDetection(G),
    relief="flat"
)
louvian_3.place(
    x=1147.518310546875,
    y=590.4365234375,
    width=88.0291748046875,
    height=36.22291564941406
)

canvas.create_text(
    30.0,
    682.0,
    anchor="nw",
    text="Powered by NetworkX Tkinter ",
    fill="#3F3E3E",
    font=("Inter", 20 * -1)
)

# Define the options for the drop-down menu

filter_options=['Defult','Node Degree','Edge weight']

# Create a variable to store the selected centrality measure
selected_filter = StringVar(window)
selected_filter.set(filter_options[0])
# Create the drop-down menu and add options
def adjust_graph(value):
    if value == filter_options[1]:
        draw_nodeDegree(G)
    elif value == filter_options[2]:
        draw_edge_weight(G)


adjust_dropdown = OptionMenu(canvas, selected_filter, *filter_options,command=adjust_graph)

adjust_dropdown.config(width=20)
centrality_dropdown_window = canvas.create_window( 1090,
    69.0, anchor=NW, window=adjust_dropdown)


# Create a variable to store the selected centrality measure
centrality_options = ["None","Closeness Centrality", "Betweenness centrality", "Harmonic centrality"]
selected_centrality = StringVar(window)
selected_centrality.set(centrality_options[0])  # Set default option
# Create the drop-down menu and add options

def filtergraph(value):
    if value == centrality_options[1]:
        draw_closeness_centrality(G)
    elif value== centrality_options[2]:
        draw_betweenness_centrality(G)
    elif value == centrality_options[3]:
        draw_harmonic_centrality(G)

centrality_dropdown = OptionMenu(canvas, selected_centrality, *centrality_options,command=filtergraph)
centrality_dropdown.config(width=20)
centrality_dropdown_window = canvas.create_window(1090,
    251.0, anchor=NW, window=centrality_dropdown)


window.resizable(False, False)
window.mainloop()
