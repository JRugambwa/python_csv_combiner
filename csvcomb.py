"""

 Python Script:

  Combine/Merge multiple CSV files using the Pandas library

"""
# import pandas & glob packages
import pandas as pd
from glob import glob

#find all csv files in the folder(e.g on the C:/--- drive)

the_files = glob('C:/path/*.csv')

#create an empty list
df_list = []

#loop over the files appending them to the empty list(df_list)

for filename in sorted(the_files):
	df_list.append(pd.read_csv(filename))

#concatenate the files

full_df = pd.concat(df_list)

#A marged file will be created ('merged_pandas.csv')
full_df.to_csv('C:/path/merged_pandas.csv')