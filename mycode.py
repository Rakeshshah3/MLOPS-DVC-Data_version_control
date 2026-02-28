import pandas as pd
import os


# Create a sample DataFrame with Column names
data={'Name':['Alice','Bob','Charlie'],
       'Age':[20,32,25],
       'City':['Panipat','Karnal','Rohtak']
      }
df=pd.DataFrame(data)



# Ensures the "data" directory exists at the root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

# Define the file path
file_path=os.path.join(data_dir,'sample_data.csv')

# Save the DataFrame to csv file, including column names
df.to_csv(file_path,index=False)
print(f"CSV file saved to {file_path}")
