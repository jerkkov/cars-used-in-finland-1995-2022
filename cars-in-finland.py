# -*- coding: utf-8 -*-
from bokeh.layouts import column
from bokeh.plotting import ColumnDataSource, figure, show
from bokeh.models import AutocompleteInput, Div, CustomJS, MultiChoice, CustomJSFilter, CDSView
from enum import Enum
import json

class PowerSource(str, Enum):
    GAS = "Gas"
    ELECTRIC = "Electric"
    GASOLINE = "Gasoline"
    HYDROGEN = "Hydrogen"
    DIESEL = "Diesel"
    OVERALL = "Overall"

DEFAULT_AREA = "MA1 MANNER0SUOMI"

f = open("cars-in-finland-1995-2022.json", encoding="utf-8")
data = json.load(f)

def get_areas(list: list):
    areas = []
    for i in list:
        areas.append(i)
    return areas

def get_years(list: list):
    years = []
    for i in list.keys():
        dict_key = str(i)
        year = dict_key.split(" ")[0]
        if years.count(year) == 0:
            years.append(year)
    return years
            
def get_power_source_values(list: list, power_source_name: PowerSource):
    power_source_values = []
    for x, y in list.items():
        dict_key = str(x)
        power_source = dict_key.split(" ")[1]
        if power_source == power_source_name:
            power_source_values.append(y)
    return power_source_values


# ALL -> MA1 MANNER0SUOMI
areas = get_areas(data)

# selected_area = auto_complete_input.value
years = get_years(data[DEFAULT_AREA])
gasoline = get_power_source_values(data[DEFAULT_AREA], PowerSource.GASOLINE)
gas = get_power_source_values(data[DEFAULT_AREA], PowerSource.GAS)
electric = get_power_source_values(data[DEFAULT_AREA], PowerSource.ELECTRIC)
hydrogen = get_power_source_values(data[DEFAULT_AREA], PowerSource.HYDROGEN)
diesel = get_power_source_values(data[DEFAULT_AREA], PowerSource.DIESEL)
overall = get_power_source_values(data[DEFAULT_AREA], PowerSource.OVERALL)

auto_complete_input = AutocompleteInput(title="Enter a city:", completions=areas, value="MA1 MANNER0SUOMI")
source = ColumnDataSource(data=dict(x=years, y=electric))
# view = CDSView(filter=IndexFilter([0, 2, 4]))

# Hover over graph
TOOLTIPS = [
    ("index", "$index"),
    ("(Year,Power Source)", "($x, $y)"),
]

TOOLS="hover,pan,wheel_zoom,zoom_in,zoom_out,box_zoom"

# create a new plot with a title and axis labels
p = figure(title="Electric cars in use from 1995 to 2022", x_axis_label="Years", y_axis_label="y", tools=TOOLS, tooltips=TOOLTIPS)

# add a line renderer with legend and line thickness to the plot

p.line('x', 'y', source=source, legend_label="Electric cars", line_width=2)

callback = CustomJS(args=dict(source=source, years=years, areas=areas, newData=data), code="""
  console.log('areas', areas)
  console.log('areas', areas)
  
  const oldArr = source;
  const area = cb_obj.value;
  
  const getPowerSource = (arr, areaName, query) => {
    const newArr = Object.entries(arr[areaName]);
    const filtered = newArr.filter((item) => item[0].includes(query));
    return filtered;
  };
    const x = years;
    console.log('x', x,)
    const y = getPowerSource(newData, area, "Electric").map(item => item[1]);

    console.log('y', y)
    source.data = { x, y }
    console.log('source.data', source.data);
""")

# custom_filter = CustomJSFilter(code='''
# const indices = [];

# // iterate through rows of data source and see if each satisfies some constraint
# for (let i = 0; i < source.get_length(); i++){
#     if (source.data['some_column'][i] == 'some_value'){
#         indices.push(true);
#     } else {
#         indices.push(false);
#     }
# }
# return indices;
# ''')

# auto_complete_input.js_on_change("value", CustomJS(code="""
#     console.log('value', cb_obj.value);
#     """))

auto_complete_input.js_on_change('value', callback)


# callback = CustomJS(args=dict(source=data), code="""
#     const inputValue = cb_obj.value
#     const x = source.data.x
#     const y = Array.from(x, (x) => Math.pow(x, f))
#     source.data = { x, y }
# """)

#Close the data file
f.close()

# create layout
layout = column(auto_complete_input, p)

# show the results
show(layout)


