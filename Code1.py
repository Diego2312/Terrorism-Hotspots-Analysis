import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets (1)\datasets\globalterrorismdb_0718dist.tar.bz2", compression="bz2")


df1 = df["success", "suicide", "attacktype1", "attacktype1_txt", "targtype1_txt", "targsubtype1_txt", "target1", "natlty1_txt", "gname", "gsubname", "nperps", "weaptype1_txt", "weapsubtype1_txt", "nkill", "nkillus" ]

print(df1.head())