import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def calculate_statistics(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    median = np.median(data)
    percentile_5th = np.percentile(data, 5)
    percentile_95th = np.percentile(data, 95)
    return mean, std_dev, median, percentile_5th, percentile_95th

def process_files(folder_path):
    stats = {}
    
    # List all files in the directory
    files = os.listdir(folder_path)

    # Filter out only files that contain numbers and sort them
    # This assumes the files have numbers somewhere in their names.
    sorted_files = sorted(files, key=lambda f: int(''.join(filter(str.isdigit, f)) or 0))
    for filename in sorted_files:
        filepath = os.path.join(folder_path, filename)
        
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r') as file:
                    data = np.array([float(line.strip()) for line in file])
                
                mean, std_dev, median, perc_5th, perc_95th = calculate_statistics(data)
                stats[filename] = {'mean': mean, 'std_dev': std_dev, 'median': median,
                                   '5th_percentile': perc_5th, '95th_percentile': perc_95th}
                
                # print(f"File: {filename}")
                # print(f"Mean: {mean}, Standard Deviation: {std_dev}, Median: {median}")
                # print(f"5th Percentile: {perc_5th}, 95th Percentile: {perc_95th}\n")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    
    return stats

def plot_medians(stats):
    labels = []
    medians = []
    p5 = []
    p95 = []

    for label, values in stats.items():
        labels.append(label)
        medians.append(values['median'])
        p5.append(values['5th_percentile'])
        p95.append(values['95th_percentile'])
    
    yerr_lower = np.subtract(medians, p5)
    yerr_upper = np.subtract(p95, medians)
    yerr = [yerr_lower,yerr_upper]

    print(labels)
    print([float(x) for x in medians])
    print([float(round(x,2)) for x in yerr_lower])
    print([float(round(x,2)) for x in yerr_upper])

    plt.figure(figsize=(10, 6))
    plt.bar(labels, medians, yerr = yerr)
    plt.xlabel('File Labels')
    plt.ylabel('Median')
    plt.title('Median of Numbers in Each File')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        sys.exit(1)

    stats = process_files(folder_path)
    plot_medians(stats)
