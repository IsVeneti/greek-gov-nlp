import json
# from doccano_transformer.datasets import NERDataset
# from doccano_transformer.utils import read_jsonl
# # with open('custom_entities1.json1', 'r') as myfile:
# #     lines = myfile.readlines()
#
# dataset = read_jsonl(filepath='custom_entities1.json1', dataset=NERDataset, encoding='utf-8')
# spacy_obj = dataset.to_spacy(tokenizer=str.split)
# print(spacy_obj)
# # with open('dataset.json', 'w') as f:
# #   for item in spacy_obj:
# #     f.write(item['data'])
# for line in lines:
#     line = json.loads(line)
#     if "labels" in line:
#         line["entities"] = line.pop("labels")
#     else:
#         line["entities"] = []
# print(line["entities"])

# tmp_ents = []
#
# for e in line["entities"]:
#     tmp_ents.append({"start": e[0], "end": e[1], "label": e[2]})
#     line["entities"] = tmp_ents
#     print(line["entities"])

# print(json.dumps({"entities": line["entities"], "text": line["text"]},ensure_ascii=False).encode('utf8').decode())
# jsonobj = json.dumps(json_file, ensure_ascii=False).encode('utf8')
# print(lines)
