import pandas as pd

URL = 'https://docs.google.com/spreadsheets/d/1uuGMcZCRLYsdcoRp13unie8BIEuEUvjC_R-hRpCUVdA/edit#gid=1038305874' #URL for data
URL = URL.replace('/edit#gid=', '/export?format=csv&gid=') #Have gsheets convert it into a csv

data = pd.read_csv(URL) #point Pandas to the data
emails = data.pop('Email Address') #remove emails from data

n1, n2 = len(data.index), len(data.columns) #get number of respondents and number of questions
df = (n1 - 1) * (n2 - 1) #degrees of freedom
