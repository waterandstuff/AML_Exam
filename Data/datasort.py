import pandas as pd

input_file = r"Data\rawdata.csv"
Machinefail = r"Data\machine_Fail.csv"
Normal = r"Data\machine_Success.csv"
column = 'Machine failure'
workdata = r"Data\workdata.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Filter the data based on the column value
fail_df = df[df[column] == 1]  # Assuming '1' indicates failure
success_df = df[df[column] == 0]  # Assuming '0' indicates success

# Save the filtered data to different CSV files

#fail_df.to_csv(Machinefail, index=False)
#success_df.to_csv(Normal, index=False)

print(f"Data sorted and saved to '{Machinefail}' and '{Normal}'.")

# Sample 1200 records from the Normal operation data
Normal_df = pd.read_csv(Normal)

sampledNormal_df = Normal_df.sample(n=1200, random_state=42)

#Save the sampled data to a CSV file

#sampledNormal_df.to_csv(r"Data\sampled_Normal.csv", index=False)

# Combine the sampled normal and machine failure data to get approx 80 - 20 split
workdata_df = pd.concat([fail_df, sampledNormal_df])

workdata_df.to_csv(workdata, index=False)

print(f"Data combined and saved to '{workdata}'.")

