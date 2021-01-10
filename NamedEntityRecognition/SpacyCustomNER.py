import json
import spacy
import random
from spacy.util import minibatch, compounding
from pathlib import Path
from Preprocessing.ExtractJsonInfo import pdfparser
from Utils.doccanoUtils import convert_doccano_to_spacy
import spacy

from Utils.documentUtils import replace_newline_with_space


# Load pre-existing spacy model
nlp = spacy.load('el_core_news_lg')

# Getting the pipeline component
ner = nlp.get_pipe("ner")

train_data_origin = convert_doccano_to_spacy("custom_entities1.json1")
# fine up to 50
train_data = train_data_origin[:2]

for _, annotations in train_data:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable pipeline components you dont need to change
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes):

  # Training for 30 iterations
  for iteration in range(2):

    # shuufling examples  before every iteration
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

# doc_url = "https://diavgeia.gov.gr/doc/ΨΥΦΩ465ΦΥΟ-ΨΟ6"
# text = pdfparser(doc_url)
# text = replace_newline_with_space(text)
# doc = nlp(text)
# print("Entities", [(ent.text, ent.label_) for ent in doc.ents])