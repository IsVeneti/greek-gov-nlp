import spacy

from Utils.FeatherUtils import read_feather_local_dataset
from Utils.PathUtils import add_path_to_project_root
from Utils.doccanoUtils import save_docs_dataset

dataset = read_feather_local_dataset("DptOfHealth1000")

# nlp = spacy.load("el_core_news_lg")
nlp = spacy.load("../CustomNERData")


for i, row in dataset.iterrows():
    doc = nlp(row['subject'])
    print(i, ": " + row['subject'])
    for entity in doc.ents:
        print(entity.text, '--- ', entity.label_)
        # if entity.label_ == "MONEY":
        #     print(entity.text,'--- ',entity.label_)

# print(dataset['subject'].to_list())
# save_docs_dataset(dataset['subject'].to_list(), "subject_doccano_dataset1")