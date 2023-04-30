
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from networkx.algorithms import community, centrality
import numpy as np
import tkinter as tk
import copy
from sklearn.metrics.cluster import normalized_mutual_info_score


# ----------------------Centrality---------------------
def draw_harmonic_centrality(G,window):
    graph=copy.deepcopy(G)
    centrality_map = centrality.harmonic_centrality(G)
    sortedDict = sorted(centrality_map)
    for i in range(0, len(sortedDict) - 10):
        graph.remove_node(sortedDict[i])

    drawGraph(graph,window=window)


def draw_betweenness_centrality(G,window):
    graph=copy.deepcopy(G)
    centrality_map = centrality.betweenness_centrality(G)
    sortedDict = sorted(centrality_map)
    for i in range(0, len(sortedDict) - 10):
        graph.remove_node(sortedDict[i])

    drawGraph(graph,window=window)


def draw_closeness_centrality(G,window):
    graph=copy.deepcopy(G)
    centrality_map = centrality.closeness_centrality(G)
    sortedDict = sorted(centrality_map)
    for i in range(0, len(sortedDict) - 10):
        graph.remove_node(sortedDict[i])
    drawGraph(graph,window=window)




#  ----------------------Adjustment---------------------
def draw_nodeDegree(G,window):
    graph=copy.deepcopy(G)
    mx = max(graph.degree)[1]
    sizes = [(degree[1] * degree[1]) for degree in G.degree]
    drawGraph(graph, node_size=sizes,window=window)


def draw_edge_weight(G,window,value):
    #Take a copy (Don't alter the orginal graph)
    graph=copy.deepcopy(G)
    edge = [w for u, v, w in G.edges(data=True)]
    if value.lower() =='weight':
        edge = [w['weight'] / 20 for w in edge]
        drawGraph(graph, edge_width=edge,window=window)
    else:
        color_list = ['red', 'blue', 'green', 'yellow', 'purple','pink', 'brown', 'orange', 'gray', 'gold']
        attribute = nx.get_edge_attributes(G,value)
        uni_list = np.unique(list(attribute.values()))
        list_col = []
        dic = {}
        i = 1
        for val in uni_list:
            #Male:0
            #Female:1
            #NAn:2
            dic[val] = i
            i = i+1
        for u,v,d in G.edges(data=True):
            attribute=d[value]
            index=dic[attribute]
            list_col.append(color_list[index])
            
        drawGraph(graph, edge_color=list_col,window=window)

#  ----------------------Community Detection---------------------
def luovian_communityDetection(G,window):
    #Louvian comm detection and Visualization
    communities = community.louvain_communities(G)
    list_col = []
    color_list = ['red', 'blue', 'green', 'yellow', 'purple','pink', 'brown', 'orange', 'gray', 'gold']
    for node in G.nodes():
        for i in range(len(communities)):
            if node in communities[i]:
                list_col.append(color_list[i])
                break
    drawGraph(G,node_color=list_col,window=window)
    return communities


#  ----------------------Link Prediction---------------------
def linkprediction(G,window):
    list_of_pred=[]
    preds = nx.pagerank(G)
   
    for k,v in preds.items():
      list_of_pred.append(v*1000)
    #Link predction Algorithm
    #list_of_pred=sorted(list_of_pred,reverse=True)
    #tk.messagebox.showinfo(title='Link Prediction Using Jaccard coefficient', message=["".join("   "+str(item)+"   "+'\n\n') for item in list_of_pred[-10:len(list_of_pred)]])
    drawGraph(G,node_size=list_of_pred,window=window)
#-------------------------Community Evaluation---------------
def Average_Nodedgree(G,community):
    sum = 0
    for node in community:
        sum = sum + G.degree(node)
    tk.messagebox.showinfo(title='Community Evaluation Using Average Node degree', message=str(sum/len(G)))
     
def  Conductance(G,community):
     tk.messagebox.showinfo(title='Community Evaluation Using conductance', message=str(nx.conductance(G, community)))
     

def get_cluster_classes(G,communities,node_attribute):
        attribute = nx.get_node_attributes(G, node_attribute)
        uni_list = np.unique(list(attribute.values()))
        dic = {}
        i = 1
        for val in uni_list:
            #Male:0
            #Female:1
            #NAn:2
            dic[val] = i
            i = i+1

        clusters = []
        classes = []

        for i in range(len(communities)):
            for node in communities[i]:
                classes.append(dic[attribute[node]])
                clusters.append(i)
        return  clusters,classes

def normalized_mutual_info(G,communities,node_attribute):
    clusters,classes=get_cluster_classes(G,communities,node_attribute)
    nmi = normalized_mutual_info_score(classes, clusters)
    tk.messagebox.showinfo(title='Community Evaluation Using NMI', message=str(nmi))


#  ----------------------Draw---------------------
def drawGraph(G, node_size=None, edge_width=None,node_color=None,window=None,edge_color=None):
    plt.clf()
    # Draw the graph using matplotlib
    if node_size is None:
        node_size = ['50'] * G.number_of_nodes()
        node_size = [int(i) for i in node_size]
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=True, node_size=node_size,node_color=node_color)
    nx.draw_networkx_edges(G, pos=pos, edge_color=edge_color, alpha=1, width=edge_width)
    plt.axis('off')
    #plt.xlim(0, 0.19)
    #plt.ylim(0, 0.19)
    # Convert the matplotlib figure to a Tkinter-compatible format
    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().place(x=100, y=90)
    canvas.draw()




