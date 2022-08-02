import os
import json
from collections import Counter
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import glob
import plotly.graph_objects as go


path = r"C:\Users\Levi\projects\ELN_usage\2021_test"
csv_files = glob.glob(os.path.join(path, "*.xlsx"))
  
sums = []  
# loop over the list of csv files
for f in csv_files:
    
    # read the csv file
    df = pd.read_excel(f)

    name = f.split("\\")[-1]  
    name = name.split("_")
    logins = df['Logins Last 30 days'].sum()
    data_use_MB = df['MB Used'].sum()
    data_use_GB = data_use_MB / 1000
    notebooks = df['Notebooks Owned'].sum()
    users = df.shape[0]
    sums.append((name[0],name[1],logins,data_use_GB,notebooks,users))

df2 = pd.DataFrame(sums, columns=('Month','Year','Logins','Data Usage','Notebooks','Users'))

sort_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                'September', 'October', 'November', 'December']

df2.index = pd.CategoricalIndex(df2['Month'], categories=sort_order, ordered=True)

df2 = df2.sort_index().reset_index(drop=True)
print(df2)




fig2 = go.Figure()

fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Users'],
     name = 'Total Users',
     mode = 'lines',
     line=dict(width=0.5, color='orange'),
     stackgroup = 'one'))

fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Notebooks'],
     name = 'Total Notebooks',
     mode = 'lines',
     line=dict(width=0.5,color='lightgreen'),
     stackgroup = 'one'))
     
fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Data Usage'],
     name = 'GB Data Used',
     mode = 'lines', 
     line=dict(width=0.5, color='blue'),
     stackgroup = 'one'))
     
fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Logins'],
     name = 'Monthly Logins',
     mode = 'lines', 
     line=dict(width=0.5, color='darkred'),
     stackgroup = 'one'))
     
fig2.update_layout(
     title = "LabArchives ELN Usage",
     title_font_size = 40, legend_font_size = 20,
     width = 1600, height = 1400)
     
fig2.update_xaxes(
     title_text = 'Month',
     title_font=dict(size=30, family='Verdana', color='black'),
     tickfont=dict(family='Calibri', color='darkred', size=25))
     
fig2.update_yaxes(
     title_text = "ELN Usage", range = (0,6500),
     title_font=dict(size=30, family='Verdana', color='black'),
     tickfont=dict(family='Calibri', color='darkred', size=25))
     
fig2.write_image(path + "figarea2.png")

fig2.show()

