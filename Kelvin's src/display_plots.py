# display_plots.py

import matplotlib.pyplot as plt
import time
import os

def display_comparison(series1, series2, x_values, x_label, exp_id, query_count, dataset="NA",
                       y_label="Query Latency (ms)", label1="POWER", label2="POWER_batch", save=True):
    fig, ax = plt.subplots()
    ax.plot(x_values, series1, marker='*', linestyle='-', label=label1)
    ax.plot(x_values, series2, marker='.', linestyle='--', label=label2)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.25)
    ax.set_ylim(bottom=0)

    # Use a logarithmic scale if the spread is large.
    if min(x_values) > 0 and max(x_values) / min(x_values) > len(x_values):
        ax.set_xscale("log")

    if save:
        out_dir = "../exp_plots"
        os.makedirs(out_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = os.path.join(out_dir, f"{exp_id}_{dataset}m_{query_count}queries_{timestamp}.png")
        fig.savefig(file_path)
        print(f"Figure saved at {file_path}")
    else:
        plt.show()
