import pandas as pd
import data
import matplotlib.pyplot as plt


def pie_chart():
    df, emails, timestamp = data.get_data()

    # queries to filter responses by social media, labels are self-explanatory
    tiktok = df[df["Social Media"] == "Tiktok"]
    instagram = df[df["Social Media"] == "Instagram"]
    youtube = df[df["Social Media"] == "Youtube"]
    reddit = df[df["Social Media"] == "Reddit"]
    twitter = df[df["Social Media"] == "Twitter"]
    facebook = df[df["Social Media"] == "Facebook"]
    snapchat = df[df["Social Media"] == "Snapchat"]
    whatsapp = df[df["Social Media"] == "WhatsApp"]

    # put all the filtered data into a list
    social_medias = [
        tiktok,
        instagram,
        youtube,
        reddit,
        twitter,
        facebook,
        snapchat,
        whatsapp
    ]

    #create labels for each social media
    labels = [
        "Tiktok",
        "Instagram",
        "Youtube",
        "Reddit",
        "Twitter",
        "Facebook",
        "Snapchat",
        "WhatsApp"
    ]

    for i in social_medias:
        i.reindex()  # reindex all of the filtered data

    #get number of each social media's users
    data1 = [len(i.index) for i in social_medias]

    fig, ax = plt.subplots()
    ax.pie(data1, labels=labels, autopct='%1.1f%%', pctdistance=0.9, normalize=True)
    ax.axis("equal")

    fig.savefig("Piechart\piechart.jpg")
