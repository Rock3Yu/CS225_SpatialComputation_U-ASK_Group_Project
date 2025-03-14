# main.py

import argparse
from display_plots import display_comparison

# Experiment modules
from exps.exp_a import run_exp_a
from exps.exp_b import run_exp_b
from exps.exp_c import run_exp_c
from exps.exp_d import run_exp_d
from exps.exp_e import run_exp_e
from exps.exp_f import run_exp_f

DEFAULT_EXP = "a"
DEFAULT_SIZE = "4"  # dataset size in millions
QUERY_COUNT = 50

def run_experiment(exp, size, query_count, show_only):
    data_path = f"../data/data_{size}"
    save_figure = not show_only
    print(f"Starting experiment {exp}...")

    if exp == "a":
        l1, l2, x_ticks, x_label = run_exp_a(data_path, query_count)
    elif exp == "b":
        l1, l2, x_ticks, x_label = run_exp_b(data_path, query_count)
    elif exp == "c":
        l1, l2, x_ticks, x_label = run_exp_c(data_path, query_count)
    elif exp == "d":
        l1, l2, x_ticks, x_label = run_exp_d(data_path, query_count)
    elif exp == "e":
        l1, l2, x_ticks, x_label = run_exp_e(data_path, query_count)
    elif exp == "f":
        l1, l2, x_ticks, x_label = run_exp_f(data_path, query_count)
        size = "2-10"
    else:
        raise ValueError("Experiment not recognized.")

    display_comparison(l1, l2, x_ticks, x_label, exp, query_count, size, save_figure)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", choices=["a", "b", "c", "d", "e", "f"], help="Select experiment")
    parser.add_argument("--size", choices=["2", "4", "6", "8", "10"], help="Dataset size (in millions)")
    parser.add_argument("--only-show-figure", action="store_true", help="Display figure without saving")
    args = parser.parse_args()

    experiment = args.exp if args.exp else DEFAULT_EXP
    size = args.size if args.size else DEFAULT_SIZE
    run_experiment(experiment, size, QUERY_COUNT, args.only_show_figure)

if __name__ == "__main__":
    main()
