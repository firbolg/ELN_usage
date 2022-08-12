import os
import pandas as pd
import glob
import plotly.graph_objects as go


path = r"C:\Users\dolanl\Projects\ELN_usage\O365-IN-RLML-RLML Librarians - Lab Archives Metrics"

# Loop over directories, check for subdirectories, populate list of paths to files
def get_files(dir_tree):
    # Directory names in the given directory 
    list_dir = os.listdir(dir_tree)
    all_files = list()
    for name in list_dir:
        # Construct path name
        full_path = os.path.join(dir_tree, name)
        # If name is a directory then check for files or subdirectories  
        if os.path.isdir(full_path):
            all_files = all_files + get_files(full_path)
        else:
            all_files.append(full_path)
                
    return all_files


files_list = get_files(path)


def monthly_data(files):    
     sums = []  
# Loop over the list of files
     for f in files:
    # TODO endswith not catching filename.  fix to remove df.columns check
          if f.endswith("User_Stats.xlsx"):
               df = pd.read_excel(f)
               if 'Logins Last 30 days' in df.columns:
    # Create list with totals for desired columns from each workbook
                    name = f.split("\\")[-1]  
                    name = name.split("_")
                    logins = df['Logins Last 60 days'].sum()
                    data_use_MB = df['MB Used'].sum()
                    data_use_GB = data_use_MB / 1000
                    notebooks = df['Notebooks Owned'].sum()
                    users = df.shape[0]
                    sums.append((name[0],name[1],logins,data_use_GB,notebooks,users))
               else:
                    pass
          else:
               pass
     return(sums)


data = monthly_data(files_list)

    
df2 = pd.DataFrame(data, columns=('Month','Year','Logins','Data Usage','Notebooks','Users'))

df2 = df2.groupby('Year')

# Create a list of dataframes sorted by year and month, then concatenate list items
dfs = []
for yr, data in df2:
     dfs.append(data)

dfs = pd.concat(dfs)

print(dfs)

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
     x= dfs['Month'], y = dfs['Users'],
     name = 'Total Users',
     mode = 'lines',
     line=dict(width=5, color='orange'),
     ))

fig2.add_trace(go.Scatter(
     x= dfs['Month'], y = dfs['Notebooks'],
     name = 'Total Notebooks',
     mode = 'lines',
     line=dict(width=5,color='lightgreen')
     ))
     
fig2.add_trace(go.Scatter(
     x= dfs['Month'], y = dfs['Data Usage'],
     name = 'GB Data',
     mode = 'lines', 
     line=dict(width=5, color='blue')
     ))
     
fig2.add_trace(go.Scatter(
     x= dfs['Month'], y = dfs['Logins'],
     name = 'Monthly Logins',
     mode = 'lines', 
     line=dict(width=5, color='darkred')
     ))
     
fig2.update_layout(
     title = "LabArchives ELN Usage",
     title_font_size = 40, legend_font_size = 20,
     width = 1600, height = 1400)
     
fig2.update_xaxes(
     title_text = 'Month',
     title_font=dict(size=30, family='Verdana', color='black'),
     tickfont=dict(family='Calibri', color='darkred', size=25))
     
fig2.update_yaxes(
     title_text = "ELN Usage", range = (0,2500),
     title_font=dict(size=30, family='Verdana', color='black'),
     tickfont=dict(family='Calibri', color='darkred', size=25))
     
fig2.write_image(path + "figarea2.png")

fig2.show()

