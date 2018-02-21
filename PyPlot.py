"""
2018-02-21T22:30:22.014Z
@author: Alejandro Guevara
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create some data so we can work with
x = np.arange(12)
y = x**2

plt.plot(x, y) # Plots the data using a blue line
plt.show()

plt.plot(x, y, '*') # Scatter plot using '*' for each point
plt.show()

plt.plot(x, y, 'r--') # Line plot, red colored and dotted line
plt.show()

# More options for format can be review at the end of this document

# Plots with red dotted line, the scales are specified with xlim and y xlim
# The plot gets a tittle and labels are asigned for the axis
plt.plot(x,y,'r--')
plt.xlim(2,4)
plt.ylim(10,20)
plt.title("Zoomed")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# New data is generated, this time a matrix with incremental values
mat = np.arange(0, 100).reshape(10,10)

# imshow is used to print images, which are nothing more than matrices with values
plt.imshow(mat)
plt.show()

# New data is generated this time randint matrix
mat = np.random.randint(0,100,(10,10))

# imshow lets us change the coloring it is using for the Plot
# adding a colobar will help to understand the plot
plt.imshow(mat, cmap="coolwarm")
plt.colorbar()
plt.show()

## Plotting with Pandas Data

# We can create a DataFrame reading from a CSV file, or Numpy array, etc.
df = pd.read_csv('salaries.csv')
print(df)

# df.plot is derived from pyplot, so the results are quite similar
df.plot(x='Salary',y='Age',kind='scatter')
plt.show()

df.plot(x='Salary',kind='hist')
plt.show()

# It is possible to print an histogram direcly from the DataFrame column
df['Age'].hist()
plt.show()

# A full list of kinds is available at the end of this file

"""
## plt.plot format options

The following format string characters are accepted to control
the line style or marker:

================    ===============================
character           description
================    ===============================
``'-'``             solid line style
``'--'``            dashed line style
``'-.'``            dash-dot line style
``':'``             dotted line style
``'.'``             point marker
``','``             pixel marker
``'o'``             circle marker
``'v'``             triangle_down marker
``'^'``             triangle_up marker
``'<'``             triangle_left marker
``'>'``             triangle_right marker
``'1'``             tri_down marker
``'2'``             tri_up marker
``'3'``             tri_left marker
``'4'``             tri_right marker
``'s'``             square marker
``'p'``             pentagon marker
``'*'``             star marker
``'h'``             hexagon1 marker
``'H'``             hexagon2 marker
``'+'``             plus marker
``'x'``             x marker
``'D'``             diamond marker
``'d'``             thin_diamond marker
``'|'``             vline marker
``'_'``             hline marker
================    ===============================

The following color abbreviations are supported:

==========  ========
character   color
==========  ========
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
==========  ========
"""

"""
Pandas plotting kinds available

    ‘line’ : line plot (default)
    ‘bar’ : vertical bar plot
    ‘barh’ : horizontal bar plot
    ‘hist’ : histogram
    ‘box’ : boxplot
    ‘kde’ : Kernel Density Estimation plot
    ‘density’ : same as ‘kde’
    ‘area’ : area plot
    ‘pie’ : pie plot
    ‘scatter’ : scatter plot
    ‘hexbin’ : hexbin plot

"""
