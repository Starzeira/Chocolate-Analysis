import pandas as pd
import csv

def load_csv(caminho, sep=','):
    return pd.read_csv(caminho, sep=sep)

def save_csv(df, caminho):
    df.to_csv(caminho, index=False)

def clone_csv(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile:
            reader = csv.reader(infile)
            with open(output_file, mode='w', newline='') as outfile:
                writer = csv.writer(outfile)
                for row in reader:
                    writer.writerow(row)
        print(f"CSV file cloned successfully from {input_file} to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")