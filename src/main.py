import argparse
from plots import plot_comparison

# experiments
from exps.exp_a import exp_a
from exps.exp_b import exp_b
from exps.exp_c import exp_c
from exps.exp_d import exp_d
from exps.exp_e import exp_e
from exps.exp_f import exp_f


def main(args):
    # print exp to run
    print(f"Running experiment {args.exp}...")
    # todo Number of positive words |q.pos|
    if args.exp == "a":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_a()
    # todo Number of negative phrases |q.neg|
    elif args.exp == "b":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_b()
    # todo Length of negative phrases q.negLen
    elif args.exp == "c":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_c()
    # todo The effect of weighting factor
    elif args.exp == "d":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_d()
    # todo The effect of k
    elif args.exp == "e":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_e()
    # todo The effect of dataset size
    elif args.exp == "f":
        line_POWER, line_POWER_batch, x_labels, x_name = exp_f()
    else:
        raise ValueError("Invalid experiment")

    plot_comparison(line_POWER, line_POWER_batch, x_labels, x_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, default="a",
                        choices=["a", "b", "c", "d", "e", "f"], help="Experiment to run")
    args = parser.parse_args()
    main(args)
