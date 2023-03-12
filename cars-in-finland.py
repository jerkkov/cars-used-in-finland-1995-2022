# -*- coding: utf-8 -*-

from bokeh.plotting import figure, show
from enum import Enum
import json

class PowerSource(str, Enum):
    GAS = 'Gas'
    ELECTRIC = 'Electric'
    GASOLINE = 'Gasoline'
    HYDROGEN = 'Hydrogen'
    DIESEL = 'Diesel'
    OVERALL = 'Overall'

f = open('cars-in-finland-1995-2022.json', encoding='utf-8')
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
        year = dict_key.split(' ')[0]
        if years.count(year) == 0:
            years.append(year)
    return years
            
def get_power_source_values(list: list, power_source_name: PowerSource):
    power_source_values = []
    for x, y in list.items():
        dict_key = str(x)
        power_source = dict_key.split(' ')[1]
        if power_source == power_source_name:
            power_source_values.append(y)
    return power_source_values

print(get_areas(data))
# for i in data:
#     print(data[i], ':')
#     for x in data[i]:
#      print(data[x], ' ',  data[i][x])
# ALL -> MA1 MANNER0SUOMI
area = 'Kajaani'
years = get_years(data[area])
gasoline = get_power_source_values(data[area], PowerSource.GASOLINE)
gas = get_power_source_values(data[area], PowerSource.GAS)
electric = get_power_source_values(data[area], PowerSource.ELECTRIC)
hydrogen = get_power_source_values(data[area], PowerSource.HYDROGEN)
diesel = get_power_source_values(data[area], PowerSource.DIESEL)
overall = get_power_source_values(data[area], PowerSource.OVERALL)

# print(gas)

f.close()
# prepare some data
x = years
y = electric

# create a new plot with a title and axis labels
p = figure(title="Electric cars in use from 1995 to 2022", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Electric cars", line_width=2)

# show the results
# show(p)

