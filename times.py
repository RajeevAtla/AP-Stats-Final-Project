import data
import matplotlib.pyplot as plt
import numpy as np
import datetime


def time_graph():
    df, emails, timestamp = data.get_data()

    df = timestamp.to_numpy()

    s = np.arange(0, len(df))
    df = np.column_stack((df, s))

    for i in range(378):
        temp = df[i, 0]
        temp1, temp2 = temp.split()
        month, day, year = map(int, temp1.split("/"))
        hour, minute, second = map(int, temp2.split(":"))
        df[i, 0] = datetime.datetime(
            year=year, month=month, day=day, hour=hour, minute=minute, second=second
        )

    fig, ax = plt.subplots()
    ax.plot(df[:, 0], df[:, 1])
    ax.set_title("Number of Responses")
    fig.savefig("Response_times/graph.jpg")
    plt.close()
