from datetime import datetime
from pathlib import Path

import pandas as pd

from Utils.PathUtils import make_recursive_dir

dt = "18/01/2021 02:00:00"
date_time_obj = datetime.strptime(dt, '%d/%m/%Y %H:%M:%S')


# print(date_time_obj.date())

def plot_list_date(dataset, date_type):
    date_options = ["issueDate", "submissionTimestamp"]
    if date_type not in date_options:
        raise ValueError("Invalid date type. Expected one of: %s" % date_options)
    print(date_type)


mydict = dict()
keys = [["a", 1], ["a", 2], ["a", 3], ["a", 4], ["b", 1], ["b", 2], ["b", 3], ["c", 1]]
df = pd.DataFrame(keys,columns=["chars","ints"])

# mydict.setdefault(df["chars"],[]).append(df["ints"])
# for i, row in df.iterrows():
#     mydict.setdefault(row["chars"],[]).append(row["ints"])

# plot_list_date("a", "nope")
