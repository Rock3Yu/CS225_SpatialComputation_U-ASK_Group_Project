import matplotlib.pyplot as plt


def plot_comparison(latencies1, latencies2, x_labels, x_name,
                    y_name="Query Latency (ms)", first_line_name='POWER', second_line_name='POWER_batch'):
    """
    modulize this code as a function, take input of two number array (same length n), x-row index (length also n), x name, y name, first line name(default POWER), second line name (default POWER_batch).
    """
    fig, ax = plt.subplots()
    ax.plot(x_labels, latencies1, "*", label=first_line_name, color='black', linestyle='solid')
    ax.plot(x_labels, latencies2, ".", label=second_line_name, color='black', linestyle='solid')
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.grid(True, alpha=0.25, linestyle='--')
    ax.set_ylim(bottom=0.0)
    plt.show()
