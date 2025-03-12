import matplotlib.pyplot as plt
import time
import os

def plot_comparison(latencies1, latencies2, x_labels, x_name, from_exp, num_query, data_size="NA",
                    y_name="Query Latency (ms)", first_line_name='POWER', second_line_name='POWER_batch', save_figure=True):

    fig, ax = plt.subplots()
    ax.plot(x_labels, latencies1, "*", label=first_line_name, linestyle='solid', color='blue')
    ax.plot(x_labels, latencies2, ".", label=second_line_name, linestyle='dashed', color='red')

    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.grid(True, alpha=0.25, linestyle='--')
    ax.set_ylim(bottom=0.0)

    if min(x_labels) > 0 and max(x_labels) / min(x_labels) > len(x_labels):  
        ax.set_xscale("log")

    if save_figure:
        save_dir = "../exp_plots"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        path = f"{save_dir}/{from_exp}_{data_size}m_{num_query}queries_{time.strftime('%Y%m%d-%H%M%S')}.png"
        fig.savefig(path)
        print(f"Plot saved to {path}")
    else:
        plt.show()