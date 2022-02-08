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

plt.figure(figsize=(50, 50))
m = Basemap(
    projection='merc',
    llcrnrlon=-180,
    llcrnrlat=10,
    urcrnrlon=-50,
    urcrnrlat=70,
    lat_ts=0,
    resolution='l',
    suppress_ticks=True)

node_lis = []
position = {}
att = {}
tz = []
width = []
for i in js_data['nodes']:
    att['state'] = i['state']
    att['name'] = i['name']
    v = (i['id'], att)
    node_lis.append(v)

    position[i['id']] = (m(i['longitude'], i['latitude']))
    if (us.states.lookup(i['state'])) == None:
        t = 'n'
    else:
        t = ((us.states.lookup(i['state'])).time_zones)[0]

    tz.append(t)
# print(js_data['links'])
G = nx.Graph()
edge_lis = []
for j in js_data['links']:
    e = (j['source'], j['target'])
    edge_lis.append(e)
    width.append(j['value'])
G.add_nodes_from(node_lis, )
G.add_edges_from(edge_lis)

df = pd.DataFrame(tz, dtype='category')

line1 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#ff7f0e", markersize=20)
line2 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#8c564b", markersize=20)
line3 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=20)
line4 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#d62728", markersize=20)
line5 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#9467bd", markersize=20)
line6 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#bcbd22", markersize=20)
line7 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#2ca02c", markersize=20)
line8 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#1f77b4", markersize=20)
line9 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#17becf", markersize=20)
line11 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#e377c2", markersize=20)

plt.legend((line1, line2, line3, line4, line5, line6, line7, line8, line9, line11),
           ('America/Chicago', 'America/Phoenix', 'Pacific/Guam', 'America/Los_Angeles',
            'America/New_York', 'Pacific/Honolulu', 'America/Denver', 'America/Anchorage',
            'Pacific/Samoa', 'America/Puerto_Rico'), title="Time Zone",
           fontsize=12, loc='upper right', prop={'size': 50})
# ax.add_artist(legend1)
nx.draw_networkx_nodes(G=G, pos=position, nodelist=G.nodes(), node_size=400, edgecolors='white',
                       node_color=df[0].cat.codes, alpha=1, cmap=plt.cm.tab10)
nx.draw_networkx_edges(G=G, pos=position, alpha=.2)

m.drawcountries(linewidth=3)
m.drawstates(linewidth=0.2)
m.drawcoastlines(linewidth=3)

plt.tight_layout()

plt.show()
