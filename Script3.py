import pandas as pd
from matplotlib import pyplot as plt


df_terr = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets1\datasets\Global_att_country.csv")

df_imm = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets1\datasets\estat_migr_imm8.tsv\estat_migr_imm8.tsv", sep=r"\t")


print(df_imm.columns)