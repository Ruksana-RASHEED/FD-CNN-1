import numpy as np
import pandas as pd
SOURCE_DATA_PATH = '../data/train.csv'
DATASET_FALL_PATH = '../data/dataset/sensor_data.csv'

data = pd.read_csv(SOURCE_DATA_PATH,index_col=False)
print(data.shape)
# data = data.drop(columns=['label'])
values = data.iloc[0:1, 1:1201].values
print(data.shape)
print(values)
data = pd.DataFrame(values)
data.to_csv(DATASET_FALL_PATH,index=False)