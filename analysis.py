import pandas as pd

df1 = pd.read_csv("./final_data/final_data_EUCA000846")
df2 = pd.read_csv("./final_data/final_data_EUCA000875")
df3 = pd.read_csv("./final_data/final_data_EUCA000918")
df4 = pd.read_csv("./final_data/final_data_EUCA000876")


frames = [df1,df2,df3,df4]


data = pd.concat(frames, ignore_index=True)

stocks = data.value_counts(['stock'])
stocks.to_csv("final_stocks")