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
    activities = df['Total Activities'].sum()
    data_use_MB = df['MB Used'].sum()
    data_use_GB = data_use_MB / 1000
    notebooks = df['Notebooks Owned'].sum()
    logins = df['Total Logins'].sum()
    sums.append((name[0],name[1],activities,data_use_GB,notebooks,logins))

df2 = pd.DataFrame(sums, columns=('Month','Year','Activities','Data Usage','Notebooks','Logins')) 
#df2['Month'] = pd.Categorical(df['Month'], categories=months, ordered=True)
print(df2)




fig2 = go.Figure()

fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Notebooks'],
     name = 'Notebooks',
     mode = 'lines',
     line=dict(width=0.5, color='orange'),
     stackgroup = 'one'))

fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Data Usage'],
     name = 'Data Usage',
     mode = 'lines',
     line=dict(width=0.5,color='lightgreen'),
     stackgroup = 'one'))
     
fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Activities'],
     name = 'Activities',
     mode = 'lines', 
     line=dict(width=0.5, color='blue'),
     stackgroup = 'one'))
     
fig2.add_trace(go.Scatter(
     x= df2['Month'], y = df2['Logins'],
     name = 'Logins',
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
     title_text = "ELN Usage", range = (0,500000),
     title_font=dict(size=30, family='Verdana', color='black'),
     tickfont=dict(family='Calibri', color='darkred', size=25))
     
fig2.write_image(path + "figarea2.png")

fig2.show()

