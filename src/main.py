import argparse
from plots import plot_comparison

# experiments
from exps.exp_a import exp_a
from exps.exp_b import exp_b
from exps.exp_c import exp_c
from exps.exp_d import exp_d
from exps.exp_e import exp_e
from exps.exp_f import exp_f

EXP = "a"  # a, b, c, d, e, f

DATA_SIZES = "4"  # in millions, 2, 4, 6, 8, or 10
NUM_QUERY = 50


def main(args):
    exp = args.exp if args.exp else EXP
    size = args.size if args.size else DATA_SIZES
    path = f"../data/data_{size}"
    save = not args.only_show_figure
    
    print(f"Running experiment {exp}...")
    # Number of positive words |q.pos|
    if exp == "a":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_a(path, NUM_QUERY)
    # Number of negative phrases |q.neg|
    elif exp == "b":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_b(path, NUM_QUERY)
    # todo Length of negative phrases q.negLen
    elif exp == "c":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_c(path, NUM_QUERY)
    # todo The effect of weighting factor
    elif exp == "d":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_d(path, NUM_QUERY)
    # The effect of k
    elif exp == "e":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_e(path, NUM_QUERY)
    # The effect of dataset size
    elif exp == "f":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_f(path, NUM_QUERY)
        size = "2-10"
    else:
        raise ValueError("Invalid experiment")

    plot_comparison(line_POWER, line_POWER_batch, x_labels, x_name, exp, NUM_QUERY, size, save_figure=save)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, choices=["a", "b", "c", "d", "e", "f"], help="Experiment to run")
    parser.add_argument("--size", type=str, choices=["2", "4", "6", "8", "10"], help="Size of tweet dataset (millions)")
    parser.add_argument("--only-show-figure", type=bool, default=False)
    args = parser.parse_args()
    main(args)
