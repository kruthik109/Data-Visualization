import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QComboBox, QStyleFactory, \
    QGridLayout, QSlider, QHBoxLayout
import pandas as pd
import re
import pyqtgraph as pg
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtCore    import Qt
from PyQt5.uic.properties import QtWidgets, QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

from matplotlib.figure import Figure
import math

x_0 ="h"
class Window(QDialog):


    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        title = 'plot'
        width = 900
        height = 400
        left = 900
        top = 400
        self.x = ""
        self.y = 0
        c = 0
        s= 0
        #self.setGeometry(400, 400, 900, 900)

        self.xComboBox = QComboBox(self)
        #self.xComboBox.resize(self.xComboBox.sizeHint())
        self.xComboBox.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.xLabel = QLabel("&X:")
        self.xLabel.setBuddy(self.xComboBox)

        self.yComboBox = QComboBox()
        self.yComboBox.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.yLabel = QLabel("Y:")
        self.yLabel.setBuddy(self.yComboBox)

        self.sComboBox = QComboBox()
        self.sComboBox.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.sLabel = QLabel("Size:")
        self.sLabel.setBuddy(self.sComboBox)

        self.cComboBox = QComboBox()
        self.cComboBox.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.cLabel = QLabel("Color:")
        self.cLabel.setBuddy(self.cComboBox)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.mySlider = QSlider(Qt.Horizontal, self)
        #self.mySlider.setGeometry(30, 40, 200, 30)
        self.mySlider.valueChanged[int].connect(self.changeValue)

        button = QPushButton("Plot Attributes 1", self)
        button.pressed.connect((self.find))

        #-------

        self.xComboBox1 = QComboBox(self)
        self.xComboBox1.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.xLabel1 = QLabel("&X:")
        self.xLabel1.setBuddy(self.xComboBox1)

        self.yComboBox1 = QComboBox()
        self.yComboBox1.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways", "Total fertility rate", "Life expectancy at birth"])
        self.yLabel1 = QLabel("Y:")
        self.yLabel1.setBuddy(self.yComboBox1)

        self.sComboBox1 = QComboBox()
        self.sComboBox1.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.sLabel1 = QLabel("Size:")
        self.sLabel1.setBuddy(self.sComboBox1)

        self.cComboBox1 = QComboBox()
        self.cComboBox1.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.cLabel1 = QLabel("Color:")
        self.cLabel1.setBuddy(self.cComboBox1)

        self.figure1 = plt.figure()
        self.canvas1 = FigureCanvas(self.figure1)

        self.mySlider1 = QSlider(Qt.Horizontal, self)
        #self.mySlider1.setGeometry(30, 40, 200, 30)
        self.mySlider1.valueChanged[int].connect(self.changeValue1)

        button1 = QPushButton("Plot Current Attributes 2", self)
        button1.pressed.connect((self.find1))

        # #---2------
        self.xComboBox2 = QComboBox(self)
        self.xComboBox2.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.xLabel2 = QLabel("&X:")
        self.xLabel2.setBuddy(self.xComboBox2)

        self.yComboBox2 = QComboBox()
        self.yComboBox2.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.yLabel2 = QLabel("Y:")
        self.yLabel2.setBuddy(self.yComboBox2)

        self.sComboBox2 = QComboBox()
        self.sComboBox2.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.sLabel2 = QLabel("Size:")
        self.sLabel2.setBuddy(self.sComboBox2)

        self.cComboBox2 = QComboBox()
        self.cComboBox2.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.cLabel2 = QLabel("Color:")
        self.cLabel2.setBuddy(self.cComboBox2)

        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)

        self.mySlider2 = QSlider(Qt.Horizontal, self)
        #self.mySlider2.setGeometry(30, 40, 200, 30)
        self.mySlider2.valueChanged[int].connect(self.changeValue2)

        button2 = QPushButton("Plot Current Attributes 3", self)
        button2.pressed.connect((self.find2))


        #---3-----
        self.xComboBox3 = QComboBox(self)
        self.xComboBox3.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.xLabel3 = QLabel("&X:")
        self.xLabel3.setBuddy(self.xComboBox3)

        self.yComboBox3 = QComboBox()
        self.yComboBox3.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.yLabel3 = QLabel("Y:")
        self.yLabel3.setBuddy(self.yComboBox3)

        self.sComboBox3 = QComboBox()
        self.sComboBox3.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.sLabel3 = QLabel("Size:")
        self.sLabel3.setBuddy(self.sComboBox3)

        self.cComboBox3 = QComboBox()
        self.cComboBox3.addItems(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption", "Highways",
             "Total fertility rate", "Life expectancy at birth"])
        self.cLabel3 = QLabel("Color:")
        self.cLabel3.setBuddy(self.cComboBox3)

        self.figure3 = plt.figure()
        self.canvas3 = FigureCanvas(self.figure3)

        self.mySlider3 = QSlider(Qt.Horizontal, self)
        self.mySlider3.setGeometry(30, 40, 200, 30)
        self.mySlider3.valueChanged[int].connect(self.changeValue3)

        button3 = QPushButton("Plot Attributes 4", self)
        button3.pressed.connect((self.find3))
        #---------------

        grid = QGridLayout()
        #
        # layout = QHBoxLayout()
        # layout.addWidget(self.xLabel)
        # layout.addWidget(self.xComboBox)
        #
        # layout1 = QHBoxLayout()
        # layout1.addWidget(self.yLabel)
        # layout1.addWidget(self.yComboBox)
        #
        # layout2 = QHBoxLayout()
        # layout2.addWidget(self.sLabel)
        # layout2.addWidget(self.sComboBox)
        #
        # layout3 = QHBoxLayout()
        # layout3.addWidget(self.cLabel)
        # layout3.addWidget(self.cComboBox)
        #
        # vert = QVBoxLayout()
        # vert.addLayout(layout)
        # vert.addLayout(layout1)
        # vert.addLayout(layout2)
        # vert.addLayout(layout3)
        vert = QVBoxLayout()
        vert.addWidget(self.xLabel)
        vert.addWidget(self.xComboBox)
        vert.addWidget(self.yLabel)
        vert.addWidget(self.yComboBox)
        vert.addWidget(self.sLabel)
        vert.addWidget(self.sComboBox)
        vert.addWidget(self.cLabel)
        vert.addWidget(self.cComboBox)




        grid.addWidget(self.canvas,0,1)
        grid.addWidget(self.mySlider,1,1)
        grid.addWidget(button,2,1)
        #---1--

        # layouta = QHBoxLayout()
        # layouta.addWidget(self.xLabel1)
        # layouta.addWidget(self.xComboBox1)
        #
        # layout1a = QHBoxLayout()
        # layout1a.addWidget(self.yLabel1)
        # layout1a.addWidget(self.yComboBox1)
        #
        # layout2a = QHBoxLayout()
        # layout2a.addWidget(self.sLabel1)
        # layout2a.addWidget(self.sComboBox1)
        #
        # layout3a = QHBoxLayout()
        # layout3a.addWidget(self.cLabel1)
        # layout3a.addWidget(self.cComboBox1)
        #
        # verta = QVBoxLayout()
        # verta.addLayout(layouta)
        # verta.addLayout(layout1a)
        # verta.addLayout(layout2a)
        # verta.addLayout(layout3a)
        verta = QVBoxLayout()
        verta.addWidget(self.xLabel1)
        verta.addWidget(self.xComboBox1)
        verta.addWidget(self.yLabel1)
        verta.addWidget(self.yComboBox1)
        verta.addWidget(self.sLabel1)
        verta.addWidget(self.sComboBox1)
        verta.addWidget(self.cLabel1)
        verta.addWidget(self.cComboBox1)

        grid.addWidget(self.canvas1, 0, 3)
        grid.addWidget(self.mySlider1, 1, 3)
        grid.addWidget(button1, 2, 3)


        #--2---

        # layoutb = QHBoxLayout()
        # layoutb.addWidget(self.xLabel2)
        # layoutb.addWidget(self.xComboBox2)
        #
        # layout1b = QHBoxLayout()
        # layout1b.addWidget(self.yLabel2)
        # layout1b.addWidget(self.yComboBox2)
        #
        # layout2b = QHBoxLayout()
        # layout2b.addWidget(self.sLabel2)
        # layout2b.addWidget(self.sComboBox2)
        #
        # layout3b = QHBoxLayout()
        # layout3b.addWidget(self.cLabel2)
        # layout3b.addWidget(self.cComboBox2)
        #
        # vertb = QVBoxLayout()
        # vertb.addLayout(layoutb)
        # vertb.addLayout(layout1b)
        # vertb.addLayout(layout2b)
        # vertb.addLayout(layout3b)
        vertb = QVBoxLayout()
        vertb.addWidget(self.xLabel2)
        vertb.addWidget(self.xComboBox2)
        vertb.addWidget(self.yLabel2)
        vertb.addWidget(self.yComboBox2)
        vertb.addWidget(self.sLabel2)
        vertb.addWidget(self.sComboBox2)
        vertb.addWidget(self.cLabel2)
        vertb.addWidget(self.cComboBox2)

        grid.addWidget(self.canvas2, 3, 1)
        grid.addWidget(self.mySlider2, 4, 1)
        grid.addWidget(button2, 5, 1)



        # #----3----
        # layoutc = QHBoxLayout()
        # layoutc.addWidget(self.xLabel3)
        # layoutc.addWidget(self.xComboBox3)
        #
        # layout1c = QHBoxLayout()
        # layout1c.addWidget(self.yLabel3)
        # layout1c.addWidget(self.yComboBox3)
        #
        # layout2c = QHBoxLayout()
        # layout2c.addWidget(self.sLabel3)
        # layout2c.addWidget(self.sComboBox3)
        #
        # layout3c = QHBoxLayout()
        # layout3c.addWidget(self.cLabel3)
        # layout3c.addWidget(self.cComboBox3)
        #
        # vertc = QVBoxLayout()
        # vertc.addLayout(layoutc)
        # vertc.addLayout(layout1c)
        # vertc.addLayout(layout2c)
        # vertc.addLayout(layout3c)
        vertc = QVBoxLayout()
        vertc.addWidget(self.xLabel3)
        vertc.addWidget(self.xComboBox3)
        vertc.addWidget(self.yLabel3)
        vertc.addWidget(self.yComboBox3)
        vertc.addWidget(self.sLabel3)
        vertc.addWidget(self.sComboBox3)
        vertc.addWidget(self.cLabel3)
        vertc.addWidget(self.cComboBox3)

        grid.addWidget(self.canvas3, 3, 3)
        grid.addWidget(self.mySlider3, 4, 3)
        grid.addWidget(button3, 5, 3)
        #-------


        self.setLayout(grid)
        grid.addLayout(vert,0,0)
        grid.addLayout(verta, 0, 2)
        grid.addLayout(vertb, 3, 0)
        grid.addLayout(vertc, 3, 2)



#----

    def changeValue(self, value):
            x = self.xComboBox.currentText()
            y = self.yComboBox.currentText()
            s = self.sComboBox.currentText()
            c = self.cComboBox.currentText()

            self.figure.clear()

            # create an axis
            ax = self.figure.add_subplot(111)

            df = pd.read_csv("factbook.csv")
            col = []
            for i in range(0, 60, 10):
                col.append(i)

            non_decimal = re.compile(r'[^\d.]+')
            if (type(df[x][0])) == str:
                df[x] = df[x].apply(lambda x1: non_decimal.sub('', x1)).astype(float).astype(int)

            if (type(df[y][0])) == str:
                df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

            if (type(df[s][0])) == str:
                print(df[s][0])
                df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            if (type(df[c][0])) == str:
                df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            df['new_c'] = (pd.cut(df[c], bins=5))

            curr = max(df[s])

            if curr > 150:
                div = "5"
                div += "0" * (len(str(math.trunc(curr))) - 4)

                df["s_new"] = df[s] * value / (int(div) * 50)
            else:
                df["s_new"] = df[s] * value / 50

            b = ax.scatter(x=df[x], y=df[y], s=df["s_new"], c=df["new_c"].cat.codes)
            t = y + " vs " + x
            ax.set(xlabel=x, ylabel=y, title=t)

            # scatter = a.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes, label= df["new_c"])
            #
            handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

            l = df["new_c"].unique()
            legend1 = ax.legend(*b.legend_elements(),
                                title=c, loc="lower left")
            ax.add_artist(legend1)
            legend2 = ax.legend(handles, labels, title=s, loc = "upper right")
            ax.set(xlabel=x, ylabel=y, title=t)
            # plt.show()

            annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"),
                                arrowprops=dict(arrowstyle="->"))
            annot.set_visible(False)
            names = np.array(
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"])
            norm = plt.Normalize(1, 4)
            c = np.random.randint(1, 5, size=149)
            cmap = plt.cm.RdYlGn

            def update_annot(ind):

                pos = b.get_offsets()[ind["ind"][0]]
                # print('p',pos)
                annot.xy = pos

                df_sub = df[
                    ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                     "Highways", "Total fertility rate", "Life expectancy at birth"]]

                # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
                #                        " ".join([names[n] for n in ind["ind"]]))
                text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                              " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                              " ".join('\nArea: '),
                                                              " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                              " ".join('\nBirth rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                              " ".join('\nDeath rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                              " ".join('\nGDP per capita: '),
                                                              " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                        ind["ind"]]))

                annot.set_text(text)
                # print('i2', c[ind["ind"][0]])
                annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
                annot.get_bbox_patch().set_alpha(0.4)

            def hover(event):
                vis = annot.get_visible()
                if event.inaxes == ax:
                    cont, ind = b.contains(event)
                    if cont:
                        update_annot(ind)
                        annot.set_visible(True)
                        self.canvas.draw_idle()
                    else:
                        if vis:
                            annot.set_visible(False)
                            self.canvas.draw_idle()

            self.canvas.mpl_connect("motion_notify_event", hover)



            self.canvas.draw()

        #-----1-----
    def changeValue1(self, value):
        x = self.xComboBox1.currentText()
        y = self.yComboBox1.currentText()
        s = self.sComboBox1.currentText()
        c = self.cComboBox1.currentText()

        self.figure1.clear()

        # create an axis
        ax = self.figure1.add_subplot(111)


        df = pd.read_csv("factbook.csv")
        col = []
        for i in range(0, 60, 10):
            col.append(i)

        non_decimal = re.compile(r'[^\d.]+')
        if (type(df[x][0])) == str:
            df[x] = df[x].apply(lambda x1: non_decimal.sub('',x1)).astype(float).astype(int)


        if (type(df[y][0])) == str:
            df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

        if (type(df[s][0])) == str:

            df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)


        if (type(df[c][0])) == str:
            df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

        df['new_c'] = (pd.cut(df[c], bins=5))

        curr = max(df[s])

        if curr > 150:
            div = "5"
            div += "0" * (len(str(math.trunc(curr)))-4)

            df["s_new"]= df[s]*value/(int(div)*50)
        else:
            df["s_new"] = df[s]*value/50



        b = ax.scatter(x=df[x], y=df[y], s = df["s_new"], c = df["new_c"].cat.codes)
        t = y + " vs " + x
        ax.set(xlabel=x, ylabel =y, title=t )


        handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

        l = df["new_c"].unique()
        legend1 = ax.legend(*b.legend_elements(),
                            loc="lower left", title=c)
        ax.add_artist(legend1)
        legend2 = ax.legend(handles, labels, title=s, loc='upper right')
        ax.set(xlabel=x, ylabel =y, title=t )
        # plt.show()
        annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        names = np.array(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
             "Highways", "Total fertility rate", "Life expectancy at birth"])
        norm = plt.Normalize(1, 4)
        c = np.random.randint(1, 5, size=149)
        cmap = plt.cm.RdYlGn

        def update_annot(ind):

            pos = b.get_offsets()[ind["ind"][0]]
            # print('p',pos)
            annot.xy = pos

            df_sub = df[
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"]]

            # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
            #                        " ".join([names[n] for n in ind["ind"]]))
            text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                          " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                          " ".join('\nArea: '),
                                                          " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                          " ".join('\nBirth rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                          " ".join('\nDeath rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                          " ".join('\nGDP per capita: '),
                                                          " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                    ind["ind"]]))

            #t('txt', text)
            annot.set_text(text)
            # print('i2', c[ind["ind"][0]])
            annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
            annot.get_bbox_patch().set_alpha(0.4)

        def hover(event):
            vis = annot.get_visible()

            #print('e', event.inaxes)
            if event.inaxes == ax:
                #print('ax', ax)
                cont, ind = b.contains(event)
                #print("IND", ind, cont)
                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    self.canvas1.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        self.canvas1.draw_idle()

        self.canvas1.mpl_connect("motion_notify_event", hover)


        self.canvas1.draw()

    #----2--------
    def changeValue2(self, value):
            x = self.xComboBox2.currentText()
            y = self.yComboBox2.currentText()
            s = self.sComboBox2.currentText()
            c = self.cComboBox2.currentText()

            self.figure2.clear()

            # create an axis
            ax = self.figure2.add_subplot(111)

            df = pd.read_csv("factbook.csv")
            col = []
            for i in range(0, 60, 10):
                col.append(i)

            non_decimal = re.compile(r'[^\d.]+')
            if (type(df[x][0])) == str:
                df[x] = df[x].apply(lambda x1: non_decimal.sub('', x1)).astype(float).astype(int)

            if (type(df[y][0])) == str:
                df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

            if (type(df[s][0])) == str:
                #t(df[s][0])
                df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            if (type(df[c][0])) == str:
                df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            df['new_c'] = (pd.cut(df[c], bins=5))

            curr = max(df[s])

            if curr > 150:
                div = "5"
                div += "0" * (len(str(math.trunc(curr))) - 4)

                df["s_new"] = df[s] * value / (int(div) * 50)
            else:
                df["s_new"] = df[s] * value / 50

            b = ax.scatter(x=df[x], y=df[y], s=df["s_new"], c=df["new_c"].cat.codes)
            t = y + " vs " + x
            ax.set(xlabel=x, ylabel=y, title=t)

            handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

            l = df["new_c"].unique()
            legend1 = ax.legend(*b.legend_elements(),
                                loc="lower left", title=c)
            ax.add_artist(legend1)
            legend2 = ax.legend(handles, labels,  loc = "upper right", title=s)
            ax.set(xlabel=x, ylabel=y, title=t)
            # plt.show()

            annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"),
                                arrowprops=dict(arrowstyle="->"))
            annot.set_visible(False)
            names = np.array(
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"])
            norm = plt.Normalize(1, 4)
            c = np.random.randint(1, 5, size=149)
            cmap = plt.cm.RdYlGn

            def update_annot(ind):

                pos = b.get_offsets()[ind["ind"][0]]
                # print('p',pos)
                annot.xy = pos

                df_sub = df[
                    ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                     "Highways", "Total fertility rate", "Life expectancy at birth"]]

                # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
                #                        " ".join([names[n] for n in ind["ind"]]))
                text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                              " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                              " ".join('\nArea: '),
                                                              " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                              " ".join('\nBirth rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                              " ".join('\nDeath rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                              " ".join('\nGDP per capita: '),
                                                              " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                        ind["ind"]]))

                #print('txt', text)
                annot.set_text(text)
                # print('i2', c[ind["ind"][0]])
                annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
                annot.get_bbox_patch().set_alpha(0.4)

            def hover(event):
                vis = annot.get_visible()

                #print('e', event.inaxes)
                if event.inaxes == ax:
                    #print('ax', ax)
                    cont, ind = b.contains(event)
                    #print("IND", ind, cont)
                    if cont:
                        update_annot(ind)
                        annot.set_visible(True)
                        self.canvas2.draw_idle()
                    else:
                        if vis:
                            annot.set_visible(False)
                            self.canvas2.draw_idle()

            self.canvas2.mpl_connect("motion_notify_event", hover)

            self.canvas2.draw()
    #--------3------
    def changeValue3(self, value):
        x = self.xComboBox3.currentText()
        y = self.yComboBox3.currentText()
        s = self.sComboBox3.currentText()
        c = self.cComboBox3.currentText()

        self.figure3.clear()

        # create an axis
        ax = self.figure3.add_subplot(111)


        df = pd.read_csv("factbook.csv")
        col = []
        for i in range(0, 60, 10):
            col.append(i)

        non_decimal = re.compile(r'[^\d.]+')
        if (type(df[x][0])) == str:
            df[x] = df[x].apply(lambda x1: non_decimal.sub('',x1)).astype(float).astype(int)


        if (type(df[y][0])) == str:
            df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

        if (type(df[s][0])) == str:
            print(df[s][0])
            df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)


        if (type(df[c][0])) == str:
            df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

        df['new_c'] = (pd.cut(df[c], bins=5))

        curr = max(df[s])

        if curr > 150:
            div = "5"
            div += "0" * (len(str(math.trunc(curr)))-4)

            df["s_new"]= df[s]*value/(int(div)*50)
        else:
            df["s_new"] = df[s]*value/50



        b = ax.scatter(x=df[x], y=df[y], s = df["s_new"], c = df["new_c"].cat.codes)
        t = y + " vs " + x
        ax.set(xlabel=x, ylabel =y, title=t )


        handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

        l = df["new_c"].unique()
        legend1 = ax.legend(*b.legend_elements(),
                            loc="lower left", title=c)
        ax.add_artist(legend1)
        legend2 = ax.legend(handles, labels,  loc = "upper right", title=s)
        ax.set(xlabel=x, ylabel =y, title=t )
        # plt.show()

        annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        names = np.array(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
             "Highways", "Total fertility rate", "Life expectancy at birth"])
        norm = plt.Normalize(1, 4)
        c = np.random.randint(1, 5, size=149)
        cmap = plt.cm.RdYlGn

        def update_annot(ind):

            pos = b.get_offsets()[ind["ind"][0]]
            # print('p',pos)
            annot.xy = pos

            df_sub = df[
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"]]

            # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
            #                        " ".join([names[n] for n in ind["ind"]]))
            text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                          " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                          " ".join('\nArea: '),
                                                          " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                          " ".join('\nBirth rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                          " ".join('\nDeath rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                          " ".join('\nGDP per capita: '),
                                                          " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                    ind["ind"]]))

            #print('txt', text)
            annot.set_text(text)
            # print('i2', c[ind["ind"][0]])
            annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
            annot.get_bbox_patch().set_alpha(0.4)

        def hover(event):
            vis = annot.get_visible()

            #print('e', event.inaxes)
            if event.inaxes == ax:
                #print('ax', ax)
                cont, ind = b.contains(event)
                #print("IND", ind, cont)
                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    self.canvas3.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        self.canvas3.draw_idle()

        self.canvas3.mpl_connect("motion_notify_event", hover)


        self.canvas3.draw()


    #----find----


    def find(self):
        # finding the content of current item in combo box
        x = self.xComboBox.currentText()
        y = self.yComboBox.currentText()
        s = self.sComboBox.currentText()
        c = self.cComboBox.currentText()

        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)


        df = pd.read_csv("factbook.csv")
        col = []
        for i in range(0, 60, 10):
            col.append(i)

        non_decimal = re.compile(r'[^\d.]+')
        if (type(df[x][0])) == str:
            df[x] = df[x].apply(lambda x1: non_decimal.sub('',x1)).astype(float).astype(int)


        if (type(df[y][0])) == str:
            df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

        if (type(df[s][0])) == str:
            #print(df[s][0])
            df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)


        if (type(df[c][0])) == str:
            df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

        df['new_c'] = (pd.cut(df[c], bins=5))

        curr = max(df[s])

        if curr > 150:
            div = "5"
            div += "0" * (len(str(math.trunc(curr)))-4)

            df[s]= df[s]/int(div)



        b = ax.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes)
        t = y + " vs " + x
        ax.set(xlabel=x, ylabel =y, title=t )

        # scatter = a.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes, label= df["new_c"])
        #
        handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

        l = df["new_c"].unique()
        legend1 = ax.legend(*b.legend_elements(),
                            loc="lower left", title=c)
        ax.add_artist(legend1)
        legend2 = ax.legend(handles, labels,  loc = "upper right", title=s)
        ax.set(xlabel=x, ylabel =y, title=t )
        # plt.show()

        annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        names = np.array(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
             "Highways", "Total fertility rate", "Life expectancy at birth"])
        norm = plt.Normalize(1, 4)
        c = np.random.randint(1, 5, size=149)
        cmap = plt.cm.RdYlGn

        def update_annot(ind):

            pos = b.get_offsets()[ind["ind"][0]]
            # print('p',pos)
            annot.xy = pos

            df_sub = df[
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"]]

            # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
            #                        " ".join([names[n] for n in ind["ind"]]))
            text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                          " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                          " ".join('\nArea: '),
                                                          " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                          " ".join('\nBirth rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                          " ".join('\nDeath rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                          " ".join('\nGDP per capita: '),
                                                          " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                    ind["ind"]]))

            #print('txt', text)
            annot.set_text(text)
            # print('i2', c[ind["ind"][0]])
            annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
            annot.get_bbox_patch().set_alpha(0.4)

        def hover(event):
            vis = annot.get_visible()

            #print('e', event.inaxes)
            if event.inaxes == ax:
                print('ax', ax)
                cont, ind = b.contains(event)
                print("IND", ind, cont)
                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    self.canvas.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        self.canvas.draw_idle()

        self.canvas.mpl_connect("motion_notify_event", hover)



        self.canvas.draw()

    #-----1-------
    def find1(self):
            # finding the content of current item in combo box
            x = self.xComboBox1.currentText()
            y = self.yComboBox1.currentText()
            s = self.sComboBox1.currentText()
            c = self.cComboBox1.currentText()

            self.figure1.clear()

            # create an axis
            ax = self.figure1.add_subplot(111)

            df = pd.read_csv("factbook.csv")
            col = []
            for i in range(0, 60, 10):
                col.append(i)

            non_decimal = re.compile(r'[^\d.]+')
            if (type(df[x][0])) == str:
                df[x] = df[x].apply(lambda x1: non_decimal.sub('', x1)).astype(float).astype(int)

            if (type(df[y][0])) == str:
                df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

            if (type(df[s][0])) == str:
                print(df[s][0])
                df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            if (type(df[c][0])) == str:
                df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            df['new_c'] = (pd.cut(df[c], bins=5))

            curr = max(df[s])

            if curr > 150:
                div = "5"
                div += "0" * (len(str(math.trunc(curr))) - 4)

                df[s] = df[s] / int(div)

            b = ax.scatter(x=df[x], y=df[y], s=df[s], c=df["new_c"].cat.codes)
            t = y + " vs " + x
            ax.set(xlabel=x, ylabel=y, title=t)

            # scatter = a.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes, label= df["new_c"])
            #
            handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

            l = df["new_c"].unique()
            legend1 = ax.legend(*b.legend_elements(),
                                loc="lower left", title=c)
            ax.add_artist(legend1)
            legend2 = ax.legend(handles, labels,  loc = "upper right", title=s)
            ax.set(xlabel=x, ylabel=y, title=t)
            # plt.show()

            annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"),
                                arrowprops=dict(arrowstyle="->"))
            annot.set_visible(False)
            names = np.array(
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"])
            norm = plt.Normalize(1, 4)
            c = np.random.randint(1, 5, size=149)
            cmap = plt.cm.RdYlGn

            def update_annot(ind):

                pos = b.get_offsets()[ind["ind"][0]]
                # print('p',pos)
                annot.xy = pos

                df_sub = df[
                    ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                     "Highways", "Total fertility rate", "Life expectancy at birth"]]

                # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
                #                        " ".join([names[n] for n in ind["ind"]]))
                text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                              " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                              " ".join('\nArea: '),
                                                              " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                              " ".join('\nBirth rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                              " ".join('\nDeath rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                              " ".join('\nGDP per capita: '),
                                                              " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                        ind["ind"]]))

                print('txt', text)
                annot.set_text(text)
                # print('i2', c[ind["ind"][0]])
                annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
                annot.get_bbox_patch().set_alpha(0.4)

            def hover(event):
                vis = annot.get_visible()

                print('e', event.inaxes)
                if event.inaxes == ax:
                    print('ax', ax)
                    cont, ind = b.contains(event)
                    print("IND", ind, cont)
                    if cont:
                        update_annot(ind)
                        annot.set_visible(True)
                        self.canvas1.draw_idle()
                    else:
                        if vis:
                            annot.set_visible(False)
                            self.canvas1.draw_idle()

            self.canvas1.mpl_connect("motion_notify_event", hover)


            self.canvas1.draw()
#-----2------
    def find2(self):
        # finding the content of current item in combo box
        x = self.xComboBox2.currentText()
        y = self.yComboBox2.currentText()
        s = self.sComboBox2.currentText()
        c = self.cComboBox2.currentText()

        self.figure2.clear()

        # create an axis
        ax = self.figure2.add_subplot(111)


        df = pd.read_csv("factbook.csv")
        col = []
        for i in range(0, 60, 10):
            col.append(i)

        non_decimal = re.compile(r'[^\d.]+')
        if (type(df[x][0])) == str:
            df[x] = df[x].apply(lambda x1: non_decimal.sub('',x1)).astype(float).astype(int)


        if (type(df[y][0])) == str:
            df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

        if (type(df[s][0])) == str:
            print(df[s][0])
            df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)


        if (type(df[c][0])) == str:
            df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

        df['new_c'] = (pd.cut(df[c], bins=5))

        curr = max(df[s])

        if curr > 150:
            div = "5"
            div += "0" * (len(str(math.trunc(curr)))-4)

            df[s]= df[s]/int(div)



        b = ax.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes)
        t = y + " vs " + x
        ax.set(xlabel=x, ylabel =y, title=t )

        # scatter = a.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes, label= df["new_c"])
        #
        handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

        l = df["new_c"].unique()
        legend1 = ax.legend(*b.legend_elements(),
                            loc="lower left", title=c)
        ax.add_artist(legend1)
        legend2 = ax.legend(handles, labels,  loc = "upper right", title=s)
        ax.set(xlabel=x, ylabel =y, title=t )
        # plt.show()

        annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        names = np.array(
            ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
             "Highways", "Total fertility rate", "Life expectancy at birth"])
        norm = plt.Normalize(1, 4)
        c = np.random.randint(1, 5, size=149)
        cmap = plt.cm.RdYlGn

        def update_annot(ind):

            pos = b.get_offsets()[ind["ind"][0]]
            # print('p',pos)
            annot.xy = pos

            df_sub = df[
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"]]

            # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
            #                        " ".join([names[n] for n in ind["ind"]]))
            text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                          " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                          " ".join('\nArea: '),
                                                          " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                          " ".join('\nBirth rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                          " ".join('\nDeath rate: '),
                                                          " ".join(
                                                              [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                          " ".join('\nGDP per capita: '),
                                                          " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                    ind["ind"]]))

            print('txt', text)
            annot.set_text(text)
            # print('i2', c[ind["ind"][0]])
            annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
            annot.get_bbox_patch().set_alpha(0.4)

        def hover(event):
            vis = annot.get_visible()

            print('e', event.inaxes)
            if event.inaxes == ax:
                print('ax', ax)
                cont, ind = b.contains(event)

                if cont:
                    update_annot(ind)
                    annot.set_visible(True)
                    self.canvas2.draw_idle()
                else:
                    if vis:
                        annot.set_visible(False)
                        self.canvas2.draw_idle()

        self.canvas2.mpl_connect("motion_notify_event", hover)

        self.canvas2.draw()

    #-----3------
    def find3(self):
            # finding the content of current item in combo box
            x = self.xComboBox3.currentText()
            y = self.yComboBox3.currentText()
            s = self.sComboBox3.currentText()
            c = self.cComboBox3.currentText()

            self.figure3.clear()

            # create an axis
            ax = self.figure3.add_subplot(111)

            df = pd.read_csv("factbook.csv")
            col = []
            for i in range(0, 60, 10):
                col.append(i)

            non_decimal = re.compile(r'[^\d.]+')
            if (type(df[x][0])) == str:
                df[x] = df[x].apply(lambda x1: non_decimal.sub('', x1)).astype(float).astype(int)

            if (type(df[y][0])) == str:
                df[y] = df[y].apply(lambda y1: non_decimal.sub('', y1)).astype(float).astype(int)

            if (type(df[s][0])) == str:
                print(df[s][0])
                df[s] = df[s].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            if (type(df[c][0])) == str:
                df[c] = df[c].apply(lambda x: non_decimal.sub('', x)).astype(float).astype(int)

            df['new_c'] = (pd.cut(df[c], bins=5))

            curr = max(df[s])

            if curr > 150:
                div = "5"
                div += "0" * (len(str(math.trunc(curr))) - 4)

                df[s] = df[s] / int(div)

            b = ax.scatter(x=df[x], y=df[y], s=df[s], c=df["new_c"].cat.codes)
            t = y + " vs " + x
            ax.set(xlabel=x, ylabel=y, title=t)

            # scatter = a.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes, label= df["new_c"])
            #
            handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

            l = df["new_c"].unique()
            legend1 = ax.legend(*b.legend_elements(),
                                loc="lower left", title=s)
            ax.add_artist(legend1)
            legend2 = ax.legend(handles, labels,  loc = "upper right", title=s)
            ax.set(xlabel=x, ylabel=y, title=t)
            # plt.show()

            annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"),
                                arrowprops=dict(arrowstyle="->"))
            annot.set_visible(False)
            names = np.array(
                ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                 "Highways", "Total fertility rate", "Life expectancy at birth"])
            norm = plt.Normalize(1, 4)
            c = np.random.randint(1, 5, size=149)
            cmap = plt.cm.RdYlGn

            def update_annot(ind):

                pos = b.get_offsets()[ind["ind"][0]]
                # print('p',pos)
                annot.xy = pos

                df_sub = df[
                    ["Area", "Death rate", " Birth rate", "GDP per capita", "Population", "Electricity consumption",
                     "Highways", "Total fertility rate", "Life expectancy at birth"]]

                # text = "{}, {}".format(" ".join(list(map(str, ind["ind"]))),
                #                        " ".join([names[n] for n in ind["ind"]]))
                text = "{} {} {} {} {} {} {} {} {} {}".format(" ".join("Country: "),
                                                              " ".join([df.iloc[n]["Country"] for n in ind["ind"]]),
                                                              " ".join('\nArea: '),
                                                              " ".join([str(df.iloc[n]["Area"]) for n in ind["ind"]]),
                                                              " ".join('\nBirth rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n][" Birth rate"]) for n in ind["ind"]]),
                                                              " ".join('\nDeath rate: '),
                                                              " ".join(
                                                                  [str(df.iloc[n]["Death rate"]) for n in ind["ind"]]),
                                                              " ".join('\nGDP per capita: '),
                                                              " ".join([str(df.iloc[n]["GDP per capita"]) for n in
                                                                        ind["ind"]]))

                print('txt',text)
                annot.set_text(text)
                # print('i2', c[ind["ind"][0]])
                annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
                annot.get_bbox_patch().set_alpha(0.4)

            def hover(event):
                vis = annot.get_visible()

                print('e', event.inaxes)
                if event.inaxes == ax:
                    print('ax', ax)
                    cont, ind = b.contains(event)
                    print("IND", ind, cont)
                    if cont:
                        update_annot(ind)
                        annot.set_visible(True)
                        self.canvas3.draw_idle()
                    else:
                        if vis:
                            annot.set_visible(False)
                            self.canvas3.draw_idle()

            self.canvas3.mpl_connect("motion_notify_event", hover)



            self.canvas3.draw()


if __name__ == '__main__':
        # creating apyqt5 application
        app = QApplication(sys.argv)

        # creating a window object
        main = Window()

        # showing the window
        main.show()

        # loop
        sys.exit(app.exec_())