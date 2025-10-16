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

        plt.figure(figsize=(10, 6))

        plt.plot(avg_times.index, avg_times['sequential_time'], marker='o', label='Sequential Quicksort')
        plt.plot(avg_times.index, avg_times['parallel_time'], marker='s', label='Parallel Quicksort')
        plt.plot(avg_times.index, avg_times['builtin_time'], marker='^', label='Built-in (Reference) Sort')

        # Formatting
        plt.title('Quicksort Performance: Time vs. Array Size (Avg. of 30 Runs)')
        plt.xlabel('Array Size')
        plt.ylabel('Average Execution Time (s)')

        ax = plt.gca()
        ax.xaxis.set_major_formatter(ScalarFormatter())
        ax.ticklabel_format(style='plain', axis='x')
        ticks = [300000, 500000, 1000000, 2000000, 3000000]
        plt.xticks(ticks, rotation=45)

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


