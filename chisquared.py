import numpy as np
import data
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.stats import chisquare


def chisquare_and_tables():
    df, emails, timestamp = data.get_data()

    # get number of respondents and number of questions
    respondents, questions = (
        len(df.index),
        len(df.columns) - 1,
    )

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
        whatsapp,
    ]

    social_media_names = [
        "TikTok",
        "Instagram",
        "YouTube",
        "Reddit",
        "Twitter",
        "Facebook",
        "Snapchat",
        "WhatsApp",
    ]

    # reindex all of the filtered data
    for i in social_medias:
        i.reindex()

    # compute averages for each mean in the filtered data and put into a list
    avg1 = [i["#1"].mean() for i in social_medias]
    avg2 = [i["#2"].mean() for i in social_medias]
    avg3 = [i["#3"].mean() for i in social_medias]
    avg4 = [i["#4"].mean() for i in social_medias]
    avg5 = [i["#5"].mean() for i in social_medias]
    avg6 = [i["#6"].mean() for i in social_medias]
    avgs = [avg1, avg2, avg3, avg4, avg5, avg6]
    avgs = np.concatenate(avgs).reshape(8, 6)

    # create observed table
    fig, ax = plt.subplots()
    im = ax.imshow(avgs, cmap=plt.get_cmap("brg"))
    cbar = ax.figure.colorbar(im)
    ax.set_xticks(np.arange(6))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels(["#{}".format(i) for i in range(1, 7)])
    ax.set_yticklabels(social_media_names)
    ax.set_title("Observed Means")
    for i in range(8):
        for j in range(6):
            text = ax.text(
                j, i, round(avgs[i, j], 2), ha="center", va="center", color="w"
            )
    fig.tight_layout()
    fig.savefig("Chi-squared\Observed.jpg")

    # copy means for later
    avgs_copy = avgs

    # create expected table
    sum_rows = avgs.sum(axis=1)
    avgs = np.column_stack((avgs, sum_rows))
    sum_cols = avgs.sum(axis=0)
    avgs = np.row_stack((avgs, sum_cols))

    for i in range(8):
        for j in range(6):
            avgs[i, j] = (avgs[8, j] * avgs[i, 6]) / avgs[8, 6]

    plt.close()
    fig, ax = plt.subplots()
    im = ax.imshow(
        avgs,
        norm=colors.LogNorm(vmin=avgs.min(), vmax=avgs.max()),
        cmap=plt.get_cmap("brg"),
        interpolation=None,
    )
    cbar = ax.figure.colorbar(im)

    ax.set_title("Expected Means")
    ax.set_xticks(np.arange(7))
    ax.set_yticks(np.arange(9))
    arr = ["#{}".format(i) for i in range(1, 7)]
    arr.append("Sum")
    ax.set_xticklabels(arr)
    social_media_names.append("Sum")
    ax.set_yticklabels(social_media_names)

    for i in range(9):
        for j in range(7):
            text = ax.text(
                j, i, round(avgs[i, j], 1), ha="center", va="center", color="w"
            )

    fig.tight_layout()
    fig.savefig("Chi-squared\Expected.jpg")
    plt.close()

    avgs = avgs[:-1, :-1]

    chisq, p = chisquare(f_obs=avgs_copy, f_exp=avgs)

    chisq = sum(chisq)

    print("Chi-squared: ", chisq)
