import pandas as pd

data = pd.read_csv("data.csv")

selection_0 = data[data["field"] == 0]
selection_0_num = data[data["field"] == 0].shape[0]

selection_1 = data[data["field"] == 1]
selection_1_random = selection_1.sample(selection_0_num)

frames = [selection_0, selection_1_random]
result = pd.concat(frames)
result.to_csv("./result.csv", index=False)