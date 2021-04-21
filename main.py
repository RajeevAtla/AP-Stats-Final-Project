import pandas as pd

URL = "https://docs.google.com/spreadsheets/d/1uuGMcZCRLYsdcoRp13unie8BIEuEUvjC_R-hRpCUVdA/edit#gid=1038305874"  # URL for data
URL = URL.replace(
    "/edit#gid=", "/export?format=csv&gid="
)  # Have gsheets convert it into a csv

names = [
    "Timestamp",
    "Email Address",
    "Social Media",
    "#1",
    "#2",
    "#3",
    "#4",
    "#5",
    "#6",
]

data = pd.read_csv(
    URL, header=0, names=names, memory_map=True
)  # point Pandas to the data
emails = data.pop("Email Address")  # remove emails from data
timestamp = data.pop("Timestamp")

respondents, questions = (
    len(data.index),
    len(data.columns) - 1,
)  # get number of respondents and number of questions

# queries to filter responses by social media, labels are self-explanatory
tiktok = data[data["Social Media"] == "Tiktok"]
instagram = data[data["Social Media"] == "Instagram"]
youtube = data[data["Social Media"] == "Youtube"]
reddit = data[data["Social Media"] == "Reddit"]
twitter = data[data["Social Media"] == "Twitter"]
facebook = data[data["Social Media"] == "Facebook"]
snapchat = data[data["Social Media"] == "Snaphchat"]
whatsapp = data[data["Social Media"] == "WhatsApp"]

social_medias = [
    tiktok,
    instagram,
    youtube,
    reddit,
    twitter,
    facebook,
    snapchat,
    whatsapp,
]  # put all the filtered data into a list
for i in social_medias:
    i.reindex()  # reindex all of the filtered data

# compute averages
avg1 = [i["#1"].mean() for i in social_medias]
avg2 = [i["#2"].mean() for i in social_medias]
avg3 = [i["#3"].mean() for i in social_medias]
avg4 = [i["#4"].mean() for i in social_medias]
avg5 = [i["#5"].mean() for i in social_medias]
avg6 = [i["#6"].mean() for i in social_medias]
avgs = [avg1, avg2, avg3, avg4, avg5, avg6]

