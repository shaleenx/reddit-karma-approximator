import pandas as pd

df = pd.read_csv("data_cleaned.csv")
df = df.dropna()
keys = df.keys()
df = df[["#image_id", "unixtime", "username", "subreddit", "score"]]
grouped_df = df.groupby("#image_id")

for key, item in grouped_df:
    users = grouped_df.get_group(key)["username"].tolist()
    subreddits = grouped_df.get_group(key)["subreddit"].tolist()
    scores = grouped_df.get_group(key)["score"].tolist()
    first = users[0]
    for i in range(len(users)):
        print(first, users[i], subreddits[i], scores[i])
