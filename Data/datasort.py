import pandas as pd

input_file = r"C:\Users\bayka\Documents\AAU Robot\7sem\AppliedMachineLearning\AML_Exam\AML_Exam\Data\rawdata.csv"
Machinefail = r"Data\machine_Fail.csv"
Machinesuccess = r"Data\machine_Success.csv"
column = 'Machine failure'

# Read the CSV file
df = pd.read_csv(input_file)

# Filter the data based on the column value
fail_df = df[df[column] == 1]  # Assuming '1' indicates failure
success_df = df[df[column] == 0]  # Assuming '0' indicates success

# Save the filtered data to different CSV files
fail_df.to_csv(Machinefail, index=False)
success_df.to_csv(Machinesuccess, index=False)

print(f"Data sorted and saved to '{Machinefail}' and '{Machinesuccess}'.")