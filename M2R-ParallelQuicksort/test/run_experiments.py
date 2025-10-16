import sys
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

from run_quicksort import execute_quicksort, get_times
from plot import plot_results


NUM_REPETITIONS = 30

ARRAY_SIZES = [str(i) for i in range(300000, 3000001, 100000)]


def save_results_to_csv(results_data, filename):
    if not results_data:
        print(f"No data collected to save to {filename}.")
        return

    fieldnames = ['size', 'run', 'sequential_time', 'parallel_time', 'builtin_time']

    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results_data)
        return True
    except Exception as e:
        print(f"\nERROR - Failed to save results to CSV: {e}")
        return False


def conduct_experiments(array_sizes, repetitions):
    all_results = []
    output_filename = "quicksort_results.csv"

    print(f"Starting Experiment: {repetitions} repetitions per array size.")
    print(f"Results will be saved to: {output_filename}")

    for size in array_sizes:
        for i in range(1, NUM_REPETITIONS+1):
            result = execute_quicksort(size)
            if result and result.returncode == 0:
                try:
                    sequential_time, parallel_time, builtin_time = get_times(result)
                    print(f" Success. Times (s/p/b): {sequential_time:.4f} / {parallel_time:.4f} / {builtin_time:.4f}")

                    all_results.append({
                        'size': size,
                        'run': i,
                        'sequential_time': sequential_time,
                        'parallel_time': parallel_time,
                        'builtin_time': builtin_time,
                    })
                except Exception as e:
                    print(f" ERROR: {e}")
            elif result is None:
                print(" FAILED ")
                # Save partial results before exiting
                save_results_to_csv(all_results, "quicksort_results_partial.csv")
                sys.exit(1)
            else:
                print(f" FAILED - Program returned non-zero code: {result.returncode}")


    if save_results_to_csv(all_results, output_filename):
        return output_filename
    else:
        return None


final_csv_file = conduct_experiments(ARRAY_SIZES, NUM_REPETITIONS)

if final_csv_file:
    print("Plotting...")
    plot_results(final_csv_file)
