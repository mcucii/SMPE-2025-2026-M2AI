import subprocess
import sys

EXECUTABLE_PATH = "../src/parallelQuicksort"

def execute_quicksort(array_size):
    command = [EXECUTABLE_PATH, array_size]

    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"The program ran successfully.")
        return result
    except Exception as e:
        print(f"\nAn error occurred: {e}")

def get_times(result):
    lines = result.stdout.splitlines()
    sequential_time = float(lines[0].split()[3])
    parallel_time   = float(lines[1].split()[3])
    builtin_time    = float(lines[2].split()[3])
    return [sequential_time, parallel_time, builtin_time]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        size_arg = sys.argv[1]
    else:
        size_arg = "1000000"
    result = execute_quicksort(size_arg)
    times = get_times(result)
    print(f"Sequential time:  {times[0]} \n Paralllel time: {times[1]} \n Builtin time: {times[2]}")
