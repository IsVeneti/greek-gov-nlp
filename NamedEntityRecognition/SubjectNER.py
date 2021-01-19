from datetime import datetime

import spacy
import pandas as pd

from Utils.FeatherUtils import read_feather_local_dataset
from Utils.PathUtils import add_path_to_project_root
from Utils.doccanoUtils import save_docs_dataset

health_ds = read_feather_local_dataset("DptOfHealth1000")

# nlp = spacy.load("el_core_news_lg")
nlp = spacy.load("../CustomNERData")


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
            'organizationUid': row['organizationUid'],
            'organizationLabel': row['organizationLabel'],
            'money': float_money
        })
    return pd.DataFrame(money_meta_list)


def plot_list_date_money(dataset: pd.DataFrame, date_type="submissionTimestamp"):
    date_money_dict = dict()
    date_options = ["issueDate", "submissionTimestamp"]

    if date_type not in date_options:
        raise ValueError("Invalid date_type. Expected one of: %s" % date_options)

    for i, row in dataset.iterrows():
        date_money_dict.setdefault(row[date_type].date(), []).append(row["money"])
    return date_money_dict


def plot_list_decision_type_money(dateset: pd.DataFrame):
    # FIXME: plot_list_decision_type_money
    print("FIXME")


money_test = subject_money_meta(health_ds)
print(plot_list_date_money(money_test))

# print(dataset['subject'].to_list())
# save_docs_dataset(dataset['subject'].to_list(), "subject_doccano_dataset1")
