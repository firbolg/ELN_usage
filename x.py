import os
import json
from collections import Counter
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import glob

#path = "C:\Users\Levi\projects\ELN_usage\2021_test"

df = pd.read_excel((r'C:\Users\Levi\projects\ELN_usage\2021_test\August_2021_User_Stats.xlsx'))


activities = df['Total Activities'].sum()
data_use = df['MB Used'].sum()
notebooks = df['Notebooks Owned'].sum()
logins = df['Total Logins'].sum()

path = r"C:\Users\Levi\projects\ELN_usage\2021_test"
csv_files = glob.glob(os.path.join(path, "*.xlsx"))
  
  
# loop over the list of csv files
for f in csv_files:
    
    # read the csv file
    df = pd.read_excel(f)
      
    activities = df['Total Activities'].sum()
    data_use = df['MB Used'].sum()
    notebooks = df['Notebooks Owned'].sum()
    logins = df['Total Logins'].sum()
    print(activities, data_use, notebooks, logins)
  