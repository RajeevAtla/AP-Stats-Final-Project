import pandas as pd
import data
import matplotlib.pyplot as plt
from memes import make_figs

df, emails, timestamp = data.get_data()
respondents, questions = (
    len(df.index),
    len(df.columns) - 1,
)  # get number of respondents and number of questions

# queries to filter responses by social media, labels are self-explanatory
tiktok = df[df["Social Media"] == "Tiktok"]
instagram = df[df["Social Media"] == "Instagram"]
youtube = df[df["Social Media"] == "Youtube"]
reddit = df[df["Social Media"] == "Reddit"]
twitter = df[df["Social Media"] == "Twitter"]
facebook = df[df["Social Media"] == "Facebook"]
snapchat = df[df["Social Media"] == "Snapchat"]
whatsapp = df[df["Social Media"] == "WhatsApp"]

social_medias = [
    tiktok,
    instagram,
    youtube,
    reddit,
    twitter,
    facebook,
    snapchat,
    whatsapp
]  # put all the filtered data into a list

for i in social_medias:
    i.reindex()  # reindex all of the filtered data

# compute averages for filtered data and put into list
avg1 = [i["#1"].mean() for i in social_medias]
avg2 = [i["#2"].mean() for i in social_medias]
avg3 = [i["#3"].mean() for i in social_medias]
avg4 = [i["#4"].mean() for i in social_medias]
avg5 = [i["#5"].mean() for i in social_medias]
avg6 = [i["#6"].mean() for i in social_medias]
avgs = [avg1, avg2, avg3, avg4, avg5, avg6]

make_figs()