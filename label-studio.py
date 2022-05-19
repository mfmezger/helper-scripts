import os
import pandas as pd

data_path = "/Users/marc.mezger/Downloads/labelstudio.csv"
target_path = "/path/to/target/"


def main():
    # read pandas csv.
    df = pd.read_csv(data_path)

    print(df.head(5))



if __name__ == '__main__':
    main()
