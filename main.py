import pandas as pd

URL = 'https://docs.google.com/spreadsheets/d/1uuGMcZCRLYsdcoRp13unie8BIEuEUvjC_R-hRpCUVdA/edit#gid=1038305874' #URL for data
URL = URL.replace('/edit#gid=', '/export?format=csv&gid=') #Have gsheets convert it into a csv

names = ['Timestamp', 'Email Address', 'Social Media', '#1', '#2', '#3', '#4', '#5', '#6']
data = pd.read_csv(URL, header = 0, names = names, memory_map = True) #point Pandas to the data
emails = data.pop('Email Address') #remove emails from data
timestamp = data.pop('Timestamp')

respondents, questions = len(data.index), len(data.columns)-1 #get number of respondents and number of questions

#queries to filter responses by social media
tiktok = data[data['Social Media'] == 'Tiktok']
instagram = data[data['Social Media'] == 'Instagram']
youtube = data[data['Social Media'] == 'Youtube']
reddit = data[data['Social Media'] == 'Reddit']
twitter = data[data['Social Media'] == 'Twitter']
facebook = data[data['Social Media'] == 'Facebook']
snapchat = data[data['Social Media'] == 'Snaphchat']
whatsapp = data[data['Social Media'] == 'WhatsApp']

arr = [tiktok, instagram, youtube, reddit, twitter, facebook, snapchat, whatsapp]
