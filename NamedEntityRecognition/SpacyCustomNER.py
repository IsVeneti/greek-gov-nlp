import json
import warnings

import spacy
import random

from spacy import gold
from spacy.util import minibatch, compounding
from pathlib import Path
from Preprocessing.ExtractJsonInfo import pdfparser
from Utils.doccanoUtils import convert_doccano_to_spacy
import spacy
import pandas as pd

from Utils.documentUtils import replace_newline_with_space
pd.set_option('display.max_rows', None)

# Load pre-existing spacy model
nlp = spacy.load('el_core_news_lg')

# Getting the pipeline component
ner = nlp.get_pipe("ner")

train_data_origin = convert_doccano_to_spacy("custom_entities1.json1")
# fine up to 50
train_data = train_data_origin[:100]
# print(type(train_data[1]['entities']))

# for i,text in enumerate(train_data):
#     # print(list(text))
#     entities = text[1]['entities']
#     print(pd.DataFrame(gold.biluo_tags_from_offsets(nlp.make_doc(text[0]),entities)))
#     print("\n",i,"\n\n")

for _, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable pipeline components you dont need to change
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes), warnings.catch_warnings():
    # show warnings for misaligned entity spans once
    warnings.filterwarnings("once", category=UserWarning, module='spacy')
    # Training for 30 iterations
    for iteration in range(30):

        # shuffling examples  before every iteration
        random.shuffle(train_data)
        losses = {}
        # batch up the examples using spaCy's minibatch
        batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp.update(
                        texts,  # batch of texts
                        annotations,  # batch of annotations
                        drop=0.5,  # dropout - make it harder to memorise data
                        losses=losses,
                    )
            print("Losses", losses)
# Save the  model to directory
output_dir = Path('customNerSpacy/')
nlp.to_disk(output_dir)
print("Saved model to", output_dir)

doc_url = "https://diavgeia.gov.gr/doc/ΨΥΦΩ465ΦΥΟ-ΨΟ6"
text = pdfparser(doc_url)
text = replace_newline_with_space(text)
doc = nlp(text)
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])


