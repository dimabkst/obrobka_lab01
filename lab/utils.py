from typing import Tuple
import matplotlib.pyplot as plt


def draw_plot(xdata, ydata, xlabel: str, ylabel: str, title: str) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots()
    ax.plot(xdata, ydata)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    plt.grid(linestyle='--', color="black", alpha=0.4)

    plt.show()

    return fig, ax
