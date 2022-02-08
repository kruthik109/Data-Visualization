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

% matplotlib inline
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
import us
import matplotlib.lines as mlines
import json

with open('/Users/kruthikrishnappa/PycharmProjects/VIZProj3/USAir97v2.json') as f:
    js_data = json.loads(f.read())
fig, ax = plt.subplots()
fig.set_size_inches(10, 10)

m = Basemap(
    projection='merc',
    llcrnrlon=-180,
    llcrnrlat=10,
    urcrnrlon=-50,
    urcrnrlat=70,
    lat_ts=0,
    resolution='l',
    suppress_ticks=True,
    ax=ax)

node_lis = []
position = {}
att = {}
tz = []
width = []
importance_factor = {}
edge_lis = []
degree = {}
for j in js_data['links']:
    if j['source'] in importance_factor:
        importance_factor[j['source']] += j['value']
    else:
        importance_factor[j['source']] = j['value']
    if j['target'] in importance_factor:
        importance_factor[j['target']] += j['value']
    else:
        importance_factor[j['target']] = j['value']

    if j['source'] in degree:
        degree[j['source']] += 1
    else:
        degree[j['source']] = 1
    if j['target'] in degree:
        degree[j['target']] += 1
    else:
        degree[j['target']] = 1

    e = (j['source'], j['target'])
    edge_lis.append(e)
    width.append(j['value'] * 15)

for i in js_data['nodes']:
    att['state'] = i['state']
    att['name'] = i['name']
    att['degree'] = degree.get(i['id'])
    v = (i['id'], att)
    node_lis.append(v)

    position[i['id']] = (m(i['longitude'], i['latitude']))
    if (us.states.lookup(i['state'])) == None:
        t = 'n'
    else:
        t = ((us.states.lookup(i['state'])).time_zones)[0]

    tz.append(t)

G = nx.Graph()

G.add_nodes_from(node_lis)
G.add_edges_from(edge_lis)

df = pd.DataFrame(tz, dtype='category')

node_size = [0] * 332
for i in importance_factor:
    node_size[i - 1] = importance_factor[i] * 75

nx.draw_networkx_nodes(G=G, ax=ax, pos=position, nodelist=G.nodes(), node_size=node_size, edgecolors='white',
                       node_color=df[0].cat.codes, alpha=1, cmap=plt.cm.tab10)
nx.draw_networkx_edges(G=G, ax=ax, pos=position, alpha=1, width=width, edge_cmap=plt.cm.Greys, edge_color=width)

line1 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=20)
line2 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=16)
line3 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=12)
line4 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=8)
line5 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=4)

line6 = mlines.Line2D(range(1), range(1), color="gray", marker='', markerfacecolor="gray", markersize=30, linewidth=5,
                      alpha=1)
line7 = mlines.Line2D(range(1), range(1), color="gray", marker='', markerfacecolor="gray", markersize=24, linewidth=4,
                      alpha=.8)
line8 = mlines.Line2D(range(1), range(1), color="gray", marker='', markerfacecolor="gray", markersize=18, linewidth=3,
                      alpha=.6)
line9 = mlines.Line2D(range(1), range(1), color="gray", marker='', markerfacecolor="gray", markersize=12, linewidth=2,
                      alpha=.4)
line10 = mlines.Line2D(range(1), range(1), color="gray", marker='', markerfacecolor="gray", markersize=6, linewidth=1,
                       alpha=.2)

line11 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#ff7f0e", markersize=7)
line12 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#8c564b", markersize=7)
line13 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="gray", markersize=7)
line14 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#d62728", markersize=7)
line15 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#9467bd", markersize=7)
line16 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#bcbd22", markersize=7)
line17 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#2ca02c", markersize=7)
line18 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#1f77b4", markersize=7)
line19 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#17becf", markersize=7)
line20 = mlines.Line2D(range(1), range(1), color="white", marker='o', markerfacecolor="#e377c2", markersize=7)

lengend0 = ax.legend((line11, line12, line13, line14, line15, line16, line17, line18, line19, line20),
                     ('America/Chicago', 'America/Phoenix', 'Pacific/Guam', 'America/Los_Angeles',
                      'America/New_York', 'Pacific/Honolulu', 'America/Denver', 'America/Anchorage',
                      'Pacific/Samoa', 'America/Puerto_Rico'), title="Time Zone",
                     fontsize=12, loc='upper left', prop={'size': 10})
ax.add_artist(lengend0)

m.drawcountries(linewidth=3)
m.drawstates(linewidth=0.2)
m.drawcoastlines(linewidth=3)
legend1 = ax.legend((line1, line2, line3, line4, line5), ('10', '8', '6', '4', '2'), title="Importance Factor",
                    fontsize=12, loc='upper right')
ax.add_artist(legend1)
legend2 = ax.legend((line6, line7, line8, line9, line10), ('0.500', '0.374', '0.249', '0.124', '0.001'),
                    title="Frequency",
                    fontsize=12, loc='lower left')
ax.add_artist(legend2)

plt.tight_layout()

#
plt.show()