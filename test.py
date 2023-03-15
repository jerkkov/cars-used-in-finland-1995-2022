from bokeh.plotting import figure, show, ColumnDataSource
x = [[1, 3, 2], [3, 4, 6, 6]]
y = [[2, 1, 4], [4, 7, 8, 5]]
p = figure(width=400, height=400)
source = ColumnDataSource(data=dict(x=x, y=y,))


p.multi_line(x='x', y='y', source=source, color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=4)

show(p)