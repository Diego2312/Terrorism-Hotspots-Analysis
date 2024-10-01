import pandas as pd
from matplotlib import pyplot as plt


#Vizualize all columns in df when printing in terminal
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)


#Read filtered Data set

df = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets (1)\datasets\Filtered_Data.csv")

print(df.head())