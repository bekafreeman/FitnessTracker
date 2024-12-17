# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os

# Set the path to the folder where your CSV files are stored
folder_path = r"C:/Users/bekaf/OneDrive/Data/Fitness Tracker Project/FitBit fitness tracker data/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16"

# List to hold the dataframes
df_list = []

# Loop through all the CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)  # Read each CSV file into a dataframe
        df_list.append(df)  # Add the dataframe to the list

# Concatenate all dataframes into one
combined_df = pd.concat(df_list, ignore_index=True)

# Export the combined dataframe to an Excel file
combined_df.to_excel(r"C:/Users/bekaf/OneDrive/Data/Fitness Tracker Project/FitBit fitness tracker data/combined_data.xlsx", index=False)

print(os.listdir(folder_path))  # This will list the files in the folder
