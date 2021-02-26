import codecs
import io
from datetime import datetime
from pathlib import Path

import pandas as pd
import spacy
# nlp = spacy.load("../CustomNERData")
nlp = spacy.load("el_core_news_lg")

# with open("zeroUrlText.txt", "r", encoding='utf8') as text_file:
#     text = text_file.read()

with open("zeroUrlSubject.txt", "r", encoding='utf8') as text_file:
    text = text_file.read()

doc = nlp(text)

for entity in doc.ents:
  print(entity.text,'--- ',entity.label_)


# from matplotlib.ticker import EngFormatter
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# example_dict = {"A random very long string to showcase the example": 50000000,
#                 "Another random smaller string": 3500000000,
#                 "A small string": 700000000,
#                 "String": 100000000,
#                 "Another larger than usual example string that will get sadly cut": 70000000}
#
#
# def categorical_horizontal_bar_numbers1(dataset, fig_dim=(10, 5), title="", x_label="",
#                                         y_label=""):
#     fmt = EngFormatter(places=0)
#
#     fig, ax = plt.subplots(figsize=fig_dim)
#     width = 0.75  # the width of the bars
#     ind = np.arange(len(dataset.values()))  # the x locations for the groups
#     ax.barh(ind, dataset.values(), width, color="blue")
#     ax.set_yticks(ind + width / 2)
#     ax.set_yticklabels(dataset.keys(), minor=False)
#
#     plt.grid(False)
#     plt.title(title)
#     plt.xlabel(x_label)
#     plt.ylabel(y_label)
#     ax.xaxis.set_major_formatter(fmt)
#
#     for i, v in enumerate(dataset.values()):
#         ax.text(v + 500, i, s=fmt.format_eng(v), color='blue', va='center')
#
#     plt.show()
#
# categorical_horizontal_bar_numbers1(example_dict,fig_dim=(30,10))