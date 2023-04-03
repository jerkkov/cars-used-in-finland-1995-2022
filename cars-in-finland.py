# -*- coding: utf-8 -*-
from bokeh.layouts import column, row
from bokeh.plotting import ColumnDataSource, figure, show
from bokeh.models import AutocompleteInput, CustomJS, CheckboxGroup
from enum import Enum
import json
class PowerSource(str, Enum):
    GAS = "Gas"
    ELECTRIC = "Electric"
    GASOLINE = "Gasoline"
    HYDROGEN = "Hydrogen"
    DIESEL = "Diesel"
    OVERALL = "Overall"
class LineColors(str, Enum): 
    BLUE = "#0b84a5"
    YELLOW = "#f6c85f"
    PURPLE = "#6f4e7c"
    GREEN = "#9dd866"
    ORANGE = "#ca472f"
    CYAN = "#8dddd0",
    AMMONITE = "#ddd8cf",


DEFAULT_AREA = "Finland"

TOOLTIPS = [
    ("index", "$index"),
    ("(Year,Power Source)", "($x, $y)"),
]

TOOLS="hover,pan,wheel_zoom,zoom_in,zoom_out,box_zoom"

LABELS = [PowerSource.OVERALL,
          PowerSource.ELECTRIC,
          PowerSource.GASOLINE,
          PowerSource.GAS,
          PowerSource.DIESEL,
          PowerSource.HYDROGEN]

f = open("cars-in-finland-1995-2022.json", encoding="utf-8")
data = json.load(f)
f.close()

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


areas = get_areas(data)

years = get_years(data[DEFAULT_AREA])
gasoline = get_power_source_values(data[DEFAULT_AREA], PowerSource.GASOLINE)
gas = get_power_source_values(data[DEFAULT_AREA], PowerSource.GAS)
electric = get_power_source_values(data[DEFAULT_AREA], PowerSource.ELECTRIC)
hydrogen = get_power_source_values(data[DEFAULT_AREA], PowerSource.HYDROGEN)
diesel = get_power_source_values(data[DEFAULT_AREA], PowerSource.DIESEL)
overall = get_power_source_values(data[DEFAULT_AREA], PowerSource.OVERALL)

auto_complete_input = AutocompleteInput(title="Enter a city:",
                                        completions=areas,
                                        value=DEFAULT_AREA,
                                        case_sensitive=False)

source = ColumnDataSource(data=dict(y=years,
                                    o=overall,
                                    e=electric,
                                    ga=gasoline,
                                    d=diesel,
                                    g=gas,
                                    h=hydrogen
                                    ))

p = figure(title="Cars in Use with Power Sources in Finland from 1995 to 2022",
           y_axis_label="Cars in Use",
           tools=TOOLS,
           tooltips=TOOLTIPS,
           toolbar_location="below",
           x_axis_type="linear"
           )
p.left[0].formatter.use_scientific = False

overall_line = p.line('y', 'o', source=source, line_color=LineColors.AMMONITE, legend_label="Overall", line_width=2)
electric_line = p.line('y', 'e', source=source, line_color=LineColors.BLUE, legend_label="Electric", line_width=2)
gasoline_line = p.line('y', 'ga', source=source, line_color=LineColors.ORANGE, legend_label="Gasoline", line_width=2)
diesel_line = p.line('y', 'd', source=source, line_color=LineColors.PURPLE, legend_label="Diesel", line_width=2)
gas_line = p.line('y', 'g', source=source, line_color=LineColors.GREEN, legend_label="Gas (Biofuel)", line_width=2)
hydrogen_line = p.line('y', 'h', source=source, line_color=LineColors.YELLOW, legend_label="Hydrogen", line_width=2)

p.legend.location = "top_left"

checkbox_group = CheckboxGroup(labels=LABELS, active=[0, 1, 2, 3, 4, 5])
checkbox_group.js_on_change(
    'active', CustomJS(args=dict(
     overall_line=overall_line,
     electric_line=electric_line,
     gasoline_line=gasoline_line,
     diesel_line=diesel_line,
     gas_line=gas_line,
     hydrogen_line=hydrogen_line,
     checkbox_group = checkbox_group),
     code="""
     overall_line.visible = checkbox_group.active.includes(0);
     electric_line.visible = checkbox_group.active.includes(1);
     gasoline_line.visible = checkbox_group.active.includes(2);
     diesel_line.visible = checkbox_group.active.includes(4);
     gas_line.visible = checkbox_group.active.includes(3);
     hydrogen_line.visible = checkbox_group.active.includes(5);
     """))

callback = CustomJS(args=dict(source=source,
                              years=years,
                              areas=areas,
                              newData=data,
                              ), code="""
  const oldArr = source;
  const area = cb_obj.value;
  
  const getPowerSource = (arr, areaName, query) => {
    const newArr = Object.entries(arr[areaName]);
    const filtered = newArr.filter((item) => item[0].split(" ")[1] === query);
    return filtered.reverse();
  };
    const y = years;
    const o = getPowerSource(newData, area, "Overall").map(item => item[1]);
    const e = getPowerSource(newData, area, "Electric").map(item => item[1]);
    const ga = getPowerSource(newData, area, "Gasoline").map(item => item[1]);
    const d = getPowerSource(newData, area, "Diesel").map(item => item[1]);
    const g = getPowerSource(newData, area, "Gas").map(item => item[1]);
    const h = getPowerSource(newData, area, "Hydrogen").map(item => item[1]);

    console.log('fgas', h)

    source.data = {y, o, e, ga, d, g, h, }
""")

auto_complete_input.js_on_change('value', callback)

layout = row(column(auto_complete_input, p), checkbox_group)
show(layout)


