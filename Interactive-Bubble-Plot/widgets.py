import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QComboBox, QStyleFactory, \
    QGridLayout, QSlider
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
        self.setGeometry(400, 400, 900, 900)






        self.xComboBox = QComboBox(self)
        self.xComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.xLabel = QLabel("&X:")
        self.xLabel.setBuddy(self.xComboBox)

        self.yComboBox = QComboBox()
        self.yComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways", "Total fertility rate", "Life expectancy at birth"])
        self.yLabel = QLabel("Y:")
        self.yLabel.setBuddy(self.yComboBox)

        self.sComboBox = QComboBox()
        self.sComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.sLabel = QLabel("Size:")
        self.sLabel.setBuddy(self.sComboBox)

        self.cComboBox = QComboBox()
        self.cComboBox.addItems(["Area","Death rate", " Birth rate","GDP per capita","Population","Electricity consumption", "Highways",  "Total fertility rate", "Life expectancy at birth"])
        self.cLabel = QLabel("Color:")
        self.cLabel.setBuddy(self.cComboBox)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.mySlider = QSlider(Qt.Horizontal, self)
        self.mySlider.setGeometry(30, 40, 200, 30)
        self.mySlider.valueChanged[int].connect(self.changeValue)




        button = QPushButton("Plot Current Attributes", self)
        button.pressed.connect((self.find))
        #x, y, c, s = self.find()


        df = pd.read_csv("factbook.csv")
        col = []
        for i in range(0, 60, 10):
            col.append(i)




        grid = QVBoxLayout()
        grid.addWidget(self.xLabel)
        grid.addWidget(self.xComboBox)
        grid.addWidget(self.yLabel)
        grid.addWidget(self.yComboBox)
        grid.addWidget(self.sLabel)
        grid.addWidget(self.sComboBox)
        grid.addWidget(self.cLabel)
        grid.addWidget(self.cComboBox)
        grid.addWidget(self.canvas)
        grid.addWidget(self.mySlider)
        grid.addWidget(button)
        self.setLayout(grid)

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

            df["s_new"]= df[s]*value/(int(div)*50)
        else:
            df["s_new"] = df[s]*value/50



        b = ax.scatter(x=df[x], y=df[y], s = df["s_new"], c = df["new_c"].cat.codes)
        t = y + " vs " + x
        ax.set(xlabel=x, ylabel =y, title=t )

        # scatter = a.scatter(x=df[x], y=df[y], s = df[s], c = df["new_c"].cat.codes, label= df["new_c"])
        #
        handles, labels = b.legend_elements(prop="sizes", alpha=0.6)

        l = df["new_c"].unique()
        legend1 = ax.legend(*b.legend_elements(),
                            loc="best", title=c)
        ax.add_artist(legend1)
        legend2 = ax.legend(handles, labels, bbox_to_anchor=(1, 1),loc=2, title=s)
        ax.set(xlabel=x, ylabel =y, title=t )
        # plt.show()

        self.canvas.draw()



        #print(value)
    def slide(self):
        s = self.sComboBox.currentText()


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
                            loc="best", title=c)
        ax.add_artist(legend1)
        legend2 = ax.legend(handles, labels, bbox_to_anchor=(1, 1),loc=2, title="Sizes")
        ax.set(xlabel=x, ylabel =y, title=t )
        # plt.show()

        self.canvas.draw()


if __name__ == '__main__':
        # creating apyqt5 application
        app = QApplication(sys.argv)

        # creating a window object
        main = Window()

        # showing the window
        main.show()

        # loop
        sys.exit(app.exec_())