import pandas as pd
from matplotlib import pyplot as plt


#Vizualize all columns in df when printing in terminal
pd.set_option('display.max_columns', 14)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)


#Read filtered Data set

df = pd.read_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets1\datasets\Filtered_Data.csv")


#Attacks over the years (Global)


att_yrs = df["iyear"].value_counts() #Create series with count of attacks per year
df_att_yrs = pd.DataFrame(att_yrs).reset_index(drop=False) #Convert to a df and fix index
df_att_yrs.rename(columns={"iyear":"Year"}, inplace=True) #Rename column
df_att_yrs.sort_values(["Year"], ascending=False, inplace=True) #Sort by year

#Plot

plt.figure(figsize=(8, 6))

plt.bar(df_att_yrs["Year"], df_att_yrs["count"])

plt.xticks(range(1970, 2020, 5))
plt.xlabel("Year")
plt.ylabel("Attacks")

plt.title("Terrorist attacks over the years", fontweight="bold")

plt.show()


#Average attacks over the years (Global)


#Create a new df with the number of attacks per country per year. Column year and one column for each country and one for average

#Use groupby year, then by country and then sum

#I need to count per country. How many times do we find

df_global_att = df[["iyear", "country_txt"]] #Filter df

df_global_att =df_global_att.groupby(["iyear", "country_txt"]).size() #Group by year, then by country and then count the incidents of these groups

df_global_att = df_global_att.unstack(fill_value=0) #Pivot the table so the countries become columns

df_global_att_filered = df_global_att.loc[:, (df_global_att != 0).any()] #Create a df with countries that do not contain only zeroes

df_global_att_filered["Average"] = df_global_att_filered.mean(axis=1) #Create new column with the average attacks throughout countries each year

df_global_att_filered.to_csv(r"C:\Users\Owner\ACSAI\Extra\Terrorism-Hotspots-Analysis\datasets1\datasets\Global_att_country.csv")


#Select countries to plot
highest_gdp_countries = ["United States", "China", "Germany", "Japan", "India", "United Kingdom", "France", "Italy", "Brazil", "Canada", "Average"]
lowest_gdp_countries = ["Tuvalu", "Nauru", "Kiribati", "Palau", "Micronesia", "Marshall Islands", "Tonga", "Dominica", "Comoros", "São Tomé and Príncipe", "Average"]
highest_HDI_countries = ["Switzerland", "Norway", "Iceland", "Hong Kong", "Denmark", "Sweden", "Ireland", "Germany", "Singapore", "Netherlands", "Average"]
lowest_HDI_countries = ["South Sudan", "Chad", "Niger", "Central African Republic", "Burundi", "Mali", "Mozambique", "Burkina Faso", "Yemen", "Guinea", "Average"]
select_countries = ["United States", "China", "Germany", "Japan", "Average"]

plt.figure(figsize=(10,8)) #graph size

#Plot a line for every country in the list
for i in select_countries:
    if i == "Average":
        plt.plot(df_global_att_filered.index, df_global_att_filered[i], label=i, linewidth=3, linestyle="--", color= "purple") #Highlight the average line
    else:
        plt.plot(df_global_att_filered.index, df_global_att_filered[i], label= i)

plt.legend() #Show line labels

plt.xlabel("Year")
plt.ylabel("Attacks")

plt.title("Average attacks per country over years", fontweight="bold") #title
plt.show()





