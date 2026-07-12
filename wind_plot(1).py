import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import glob
import os
import openpyxl # allow editing and creating excel files
from openpyxl.drawing.image import Image as XLImage # insert image in excel
from openpyxl.utils.dataframe import dataframe_to_rows # transfer data to excel

    


files = glob.glob("wind_data_*.csv")
FILE = max(files, key=os.path.getctime)
print(f"Loading: {FILE}") 

df = pd.read_csv(FILE) # File CSV table is now df
i = 0
df["Time in S"] = [(i) * 0.2 for i in range(len(df))] # adds column Time in S
time = df["Time in S"] # df = from the table
Power = df["Power_mW"]
Voltage = df["RealVoltage_V"]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,4)) # sublots = 2 graphs in 1 img, ax1 and ax2 being the graphs

ax1.plot(                            # First Graph Design
    time,                             # X variable
    Power,                            # Y variable
    color="steelblue",                # graph color
    linewidth=1.5, 
    marker="o", 
    markersize=3)
for x,y in zip(time,Power):            
    if y > 0:
        ax1.annotate(f"{y}", (x, y))    # shows variable stats

ax1.set_title(                      # title adjustments
    "Power Over Time",
    color = "black",
    size = 14,
    weight = "bold")

ax1.set_xlabel(                    #label adjusments
    "Time (s)",
    color = "Green",
    size = 13,
    weight = "bold")

ax1.set_ylabel( 
    "Power (mW)",
    color = "Red",
    size = 13,
    weight = "bold")

ax1.minorticks_on()           #activate small grids
ax1.grid(                      #grid adjustments
    True, 
    which = "both" ,
    linestyle="-", 
    color = "black", 
    alpha=0.5,
    linewidth = 0.5)

ax2.plot(
    time, 
    Voltage, 
    color="orange", 
    linewidth=1.5, 
    marker="o", 
    markersize=3)

for x,y in zip(time, Voltage):
    if y > 0:
        ax2.annotate(f"{y}", (x,y))

ax2.set_title(
    "Voltage Over Time",
    color = "black",
    size = 13,
    weight = "bold")
ax2.set_xlabel(
    "Time (s)",
    color = "Green",
    size = 11,
    weight = "bold")
ax2.set_ylabel(
    "Voltage (V)",
    color = "blue",
    size = 11,
    weight = "bold")

ax2.minorticks_on()
ax2.grid(
    True, 
    which = "both",
    linestyle="-", 
    color = "black", 
    alpha=0.5,
    linewidth = 0.5)



plt.tight_layout()               #layout cleanup

workbook = openpyxl.Workbook() # creates brand new excel file
ws_data = workbook.active #grab first sheet
ws_data.title = 'Data'
for rows in dataframe_to_rows(df,index=False, header = True): #insert df in workbook, for loop to go row by row
    ws_data.append(rows)

ws_chart = workbook.create_sheet("Graph")
plt.savefig('wind_data_chart.png',dpi = 400) # saves the graph image
img = XLImage('wind_data_chart.png')
ws_chart.add_image(img, 'D1') 
workbook.save('wind_data.xlsx') # save to disk as xlsx

plt.subplots_adjust(hspace=0.4)
plt.legend()
plt.show()
