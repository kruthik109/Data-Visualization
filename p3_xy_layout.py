from mpl_toolkits.basemap import Basemap as Basemap
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import json
from mpl_toolkits.basemap import Basemap as Basemap
import us
from matplotlib.widgets import Slider, Button
import matplotlib
import matplotlib.lines as mlines
%matplotlib inline

with open('/Users/kruthikrishnappa/PycharmProjects/VIZProj3/USAir97v2.json') as f:
    js_data = json.loads(f.read())

node_lis = []
position = {}
for i in js_data['nodes']:
    v = (i['id'], i)
    node_lis.append(v)
    position[i['id']] = (i['posx'], i['posy'])
#print(js_data['links'])
G = nx.Graph()
edge_lis = []
for j in js_data['links']:
    e = (j['source'], j['target'])
    edge_lis.append(e)
G.add_nodes_from(node_lis)
G.add_edges_from(edge_lis)



fig = plt.figure(figsize=(50,50))
nx.draw(G, with_labels=True,  pos=position)