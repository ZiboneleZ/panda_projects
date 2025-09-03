import pandas as pd
import numpy as np

#Fetching the data

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep='\t')

print(chipo.head(10))

#Number of observations in the dataset
print(f"\nNumber of observations: {chipo.shape[0]}\n")
print(chipo.info())

#Number of columns in the dataset
print(f"\nNumber of columns: {chipo.shape[1]}")

#Printing the names of all columns
print(f"\nColumn names:\n{chipo.columns}")

#How the dataset is indexed
print(f"\n{chipo.index}")
