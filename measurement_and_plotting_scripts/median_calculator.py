import sys
import statistics

def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file, strip whitespace, and convert to float
            numbers = [float(line.strip()) for line in file.readlines()]
        return numbers
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def calculate_median(numbers):
    return statistics.median(numbers)

if __name__ == "__main__":
    # Ensure the file path is passed as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    numbers = read_numbers_from_file(file_path)

    if numbers:
        median_value = calculate_median(numbers)
        print(f"Median: {median_value}")
    else:
        print("Error: The file contains no numbers.")
