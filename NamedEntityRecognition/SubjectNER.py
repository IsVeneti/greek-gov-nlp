from datetime import datetime

import spacy
import pandas as pd

from Utils.FeatherUtils import read_feather_local_dataset, save_to_feather_local_dataset
from Utils.PathUtils import add_path_to_project_root
from Utils.doccanoUtils import save_docs_dataset

health_ds = read_feather_local_dataset("DptOfHealth1000")

nlp = spacy.load("el_core_news_lg")
# nlp = spacy.load("../CustomNERData")


def money_to_float(doc: spacy.tokens.doc.Doc) -> float:
    float_money = 0.0
    for entity in doc.ents:
        if entity.label_ == "MONEY":
            doc_money = nlp(entity.text)
            for token in doc_money:
                if token.like_num:
                    money = str(token).replace(".", "")
                    money = money.replace(",", ".")
                    float_money = float(money)
    return float_money


def label_count(doc: spacy.tokens.doc.Doc) -> int:
    count = 0
    for entity in doc.ents:
        count = count + 1
    return count


def subject_label_counter(dataset: pd.DataFrame) -> pd.DataFrame:
    label_count_list = []
    for i, row in dataset.iterrows():
        doc = nlp(row['subject'])
        labelc = label_count(doc)
        label_count_list.append({
            'ada': row['ada'],
            'labelCount': labelc
        })
    return pd.DataFrame(label_count_list)


def subject_money_meta(dataset: pd.DataFrame) -> pd.DataFrame:
    money_meta_list = []
    for i, row in dataset.iterrows():
        doc = nlp(row['subject'])
        float_money = money_to_float(doc)
        money_meta_list.append({
            'ada': row['ada'],
            'protocolNumber': row['protocolNumber'],
            'issueDate': datetime.strptime(row['issueDate'], '%d/%m/%Y %H:%M:%S'),
            'submissionTimestamp': datetime.strptime(row['submissionTimestamp'], '%d/%m/%Y %H:%M:%S'),
            'documentUrl': row['documentUrl'],
            'subject': row['subject'],
            'decisionTypeUid': row['decisionTypeUid'],
            'decisionTypeLabel': row['decisionTypeLabel'],
            'organizationUid': row['organizationUid'],
            'organizationLabel': row['organizationLabel'],
            'money': float_money
        })
    return pd.DataFrame(money_meta_list)


# save_to_feather_local_dataset(subject_label_counter(health_ds), "LabelCountCNERD")
save_to_feather_local_dataset(subject_label_counter(health_ds), "LabelCountLG")
# save_to_feather_local_dataset(subject_money_meta(health_ds), "MetadataWithMoney")


# money_test = subject_money_meta(health_ds)
# money_dict = list_decision_type_money(money_test)
# print(plot_decision_type_money_sum(money_dict))
# print(dataset['subject'].to_list())
# save_docs_dataset(dataset['subject'].to_list(), "subject_doccano_dataset1")
