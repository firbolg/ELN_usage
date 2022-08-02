import os
import json
from collections import Counter
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

path = r"C:\Users\Levi\projects\ELN_usage\2021_test"

df = pd.read_excel((r'C:\Users\Levi\projects\ELN_usage\2021_test\August_2021_User_Stats.xlsx'))


activities = df['Total Activities'].sum()
data_use = df['MB Used'].sum()
notebooks = df['Notebooks Owned'].sum()
logins = df['Total Logins'].sum()
print(df.head(), "activities:", activities, "data used:", data_use, 
"notebooks:", notebooks, "logins:", logins)