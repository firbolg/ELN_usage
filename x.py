import os
import json
from collections import Counter
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import glob


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
    data_use = df['MB Used'].sum()
    notebooks = df['Notebooks Owned'].sum()
    logins = df['Total Logins'].sum()
    sums.append((name[0],name[1],activities,data_use,notebooks,logins))

df2 = pd.DataFrame(sums, columns=('Month','Year','Activities','Data Usage','Notebooks','Logins')) 
#df2['Name'] = pd.Categorical(df['Name'], categories=months, ordered=True)
print(df2)
