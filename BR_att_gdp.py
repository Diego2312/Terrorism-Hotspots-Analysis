import pandas as pd
from matplotlib import pyplot as plt


df_terr = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets1\datasets\Global_att_country.csv")
df_gdp_br = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets1\datasets\UNdata_Export_20241003_192202257\UNdata_Export_20241003_192202257.csv")

df_terr_year = df_terr[(df_terr["iyear"] >= 1990)] #Filter data to 1990 -> 2017
df_gdp_br_year = df_gdp_br[(df_gdp_br["Year"] != 1993) & (df_gdp_br["Year"]<= 2017)] #Filter data to 1990 -> 2017. Not include 1993 (missing data)


plt.scatter(df_gdp_br_year["Value"], df_terr_year["Brazil"])

plt.title("Brazil terrorist attacks as GDP cahnges", fontdict={"weight": "bold"})
plt.xlabel("GDP U$D (Billions)")
plt.ylabel("Attacks")

plt.show()

