import pandas as pd

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

df = pd.read_csv("data_cleaned.csv")
df = df[["subreddit", "total_votes", "score"]]
print_full(df.groupby("subreddit").sum().sort_values(by="score", ascending=False))
