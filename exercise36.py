##### practicepython.org: Exercise 36

from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook

output_file("plot.html")

output_notebook()

x_categories = c.keys()
x = x_categories
print x

y = c.values()
print y

p = figure(x_range=x_categories)

p.vbar(x=x, top=y, width=0.25)

show(p)
