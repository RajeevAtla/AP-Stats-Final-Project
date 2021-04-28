import pandas as pd
import data
import matplotlib.pyplot as plt
import numpy as np


def boxplots():
    df, emails, timestamp = data.get_data()

    # get data for each meme and put it into an array
    # for ease of access
    meme1 = df["#1"]
    meme2 = df["#2"]
    meme3 = df["#3"]
    meme4 = df["#4"]
    meme5 = df["#5"]
    meme6 = df["#6"]

    memes = [meme1, meme2, meme3, meme4, meme5, meme6]
    fig_titles = ["Meme1", "Meme2", "Meme3", "Meme4", "Meme5", "Meme6"]

    for i in range(6):
        fig, ax = plt.subplots()
        ax.set_title(fig_titles[i])
        ax.axes.get_yaxis().set_visible(False)
        ax.set_xlabel("Rating")
        ax.boxplot(memes[i], vert=False)
        fig.savefig("Boxplots\{}.jpg".format(fig_titles[i]))
        plt.close()

    headers = ["#{}".format(i) for i in range(1, 7)]

    s = []

    for i, j in df.iteritems():
        if i in headers:
            s.append(j)

    s = pd.concat(s).reindex()

    fig, ax = plt.subplots()
    ax.set_title("Overall")
    ax.axes.get_yaxis().set_visible(False)
    ax.set_xlabel("Rating")
    ax.boxplot(s, vert=False)
    fig.savefig("Boxplots\Overall.jpg")
    plt.close()


def histograms():
    df, emails, timestamp = data.get_data()
    meme1 = df["#1"]
    meme2 = df["#2"]
    meme3 = df["#3"]
    meme4 = df["#4"]
    meme5 = df["#5"]
    meme6 = df["#6"]

    memes = [meme1, meme2, meme3, meme4, meme5, meme6]
    fig_titles = ["Meme1", "Meme2", "Meme3", "Meme4", "Meme5", "Meme6"]

    for i in range(6):
        fig, ax = plt.subplots()
        memes[i].plot.kde(ax=ax, legend=False)
        ax.set_title(fig_titles[i])
        ax.set_xlabel("Rating")
        ax.set_xlim([0, 10])
        ax.set_xticks(np.arange(1, 11))
        ax.hist(memes[i], bins="auto", density=True)
        fig.savefig("Histograms\{}.jpg".format(fig_titles[i]))
        plt.close()

    headers = ["#{}".format(i) for i in range(1, 7)]

    s = []

    for i, j in df.iteritems():
        if i in headers:
            s.append(j)

    s = pd.concat(s).reindex()

    fig, ax = plt.subplots()
    s.plot.kde(ax=ax, legend=False)
    ax.set_title("Overall")
    ax.set_xlabel("Rating")
    ax.set_xlim([0, 10])
    ax.set_xticks(np.arange(1, 11))
    ax.hist(s, bins="auto", density=True)
    fig.savefig("Histograms\Overall.jpg")
    plt.close()
