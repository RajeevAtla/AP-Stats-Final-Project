import pandas as pd
import data
import matplotlib.pyplot as plt


def make_figs():
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
    fig_titles = ["Meme 1", "Meme 2", "Meme 3", "Meme 4", "Meme 5", "Meme 6"]

    for i in range(6):
        fig, ax = plt.subplots()
        ax.set_title(fig_titles[i])
        ax.axes.get_yaxis().set_visible(False)
        ax.set_xlabel("Rating")
        ax.boxplot(memes[i], vert = False)
        fig.savefig("Boxplots\{}.jpg".format(fig_titles[i]))
