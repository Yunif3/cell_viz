from matplotlib import pyplot as plt
import numpy as np

def line_plot(data, **kwargs):
    # taking the columns
    columns = np.array(data).T
    print(columns)
    x = columns[0]
    x_label, x_data = x[0], x[1:].astype(np.float)
    for y in columns[1:]:
        y_label, y_data = y[0], y[1:].astype(np.float)
        plt.plot(x_data, y_data, '-', label=y_label)
    plt.xlabel(x_label)
    plt.legend()
    plt.show()