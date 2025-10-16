import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

filename="quicksort_results.csv"

def plot_results(filename):
    try:
        df = pd.read_csv(filename)

        df['size'] = pd.to_numeric(df['size'])

        avg_times = df.groupby('size')[['sequential_time', 'parallel_time', 'builtin_time']].mean()
        NUM_REPETITIONS = df.groupby('size').size().iloc[0]

        plt.figure(figsize=(10, 6))


        array_sizes = [int(x) for x in avg_times.index]  # konverzija u int

        plt.plot(array_sizes, avg_times['sequential_time'], 'o-', label='Sequential Quicksort')
        plt.plot(array_sizes, avg_times['parallel_time'], 's-', label='Parallel Quicksort')
        plt.plot(array_sizes, avg_times['builtin_time'], '^-', label='Built-in (Reference) Sort')

        # Formatting
        title_string = f'Quicksort Performance: Time vs. Array Size (Avg. of {NUM_REPETITIONS} Runs)'
        plt.title(title_string)
        plt.xlabel('Array Size')
        plt.ylabel('Average Execution Time (s)')

        plt.grid(True, which="both", ls="--", alpha=0.6)
        plt.legend()

        # Save the plot
        plot_filename = filename.replace('.csv', '.png')
        plt.savefig(plot_filename)
        print(f"[SUCCESS] Plot saved to {plot_filename}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    plot_results(filename)


