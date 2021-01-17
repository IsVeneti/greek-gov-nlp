import json

from Utils.PathUtils import add_path_to_project_root


def convert_doccano_to_spacy(filepath):
    with open(filepath, 'rb') as fp:
        data = fp.readlines()
        training_data = []
        for record in data:
            entities = []
            read_record = json.loads(record)
            text = read_record['text']
            entities_record = read_record['labels']
            for start, end, label in entities_record:
                entities.append((start, end, label))
                training_data.append((text, {"entities": entities}))
    return training_data


def save_docs_dataset(textList: list, filename: str):
    print("Writing dataset to txt file...")
    path = add_path_to_project_root(["ToDoccanoDataset", filename + ".txt"])
    with open(path, "w", encoding="utf-8") as text_file:
        # TODO:give the choice to split
        for element in textList:
            text_file.write(element + "\n")
