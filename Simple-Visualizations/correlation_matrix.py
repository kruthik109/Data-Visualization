# -*- coding: utf-8 -*-
"""p1_matrix

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jPqlSc6oxmSKVxCWGHtUewjPOGK4xkiF
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("old_cars.csv")

#Q4
#Visualize gas mileage, weight, horsepower, and engine volume(disp) in a scatter plot matrix. 
#Color code the individual data points by country of origin.
df1 = df[['MPG','Displacement',	'Horsepower',	'Weight',	'Origin' ]]

#shows either a density ot hist as daigonal
sns.pairplot(df1, hue='Origin', diag_kind='kde')
