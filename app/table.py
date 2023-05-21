"""Table Class"""

import matplotlib.pyplot as plt  # pylint: disable=unused-import
import numpy as np

from matplotlib.patches import Rectangle


PCS = ["PC1", "PC2", "PC3",
        "PC4", "PC5", "PC6"]


def reserve(starttime: int, endtime: int, day: int, resouce: str):
    """
    reserve
    """
    height = abs(endtime-starttime)
    width = 1 / 6
    start_x = day - width/2
    start_y = starttime

    return start_x, start_y, height, width


def main():
    """
    Main
    """
    # time_range = np.arange(-1, -6)
    # day_range = np.arange(2, 7)
    fig = plt.figure()
    ax = fig.add_subplot()

    x, y, h, w = reserve(-1, -3, 2, PCS[1])
    print(x, y, w, h)
    ax.add_patch(Rectangle((x, y), width=w, height=-h, facecolor=(0, 1, 0, 0.75), ec='g'))

    ax.set_ylim([-5, 0])
    ax.set_xlim([1.5, 6.5])
    ax.grid(True)

    plt.show()


main()
