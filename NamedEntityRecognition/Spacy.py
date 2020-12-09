import spacy

from Preprocessing.ExtractJsonInfo import pdfparser

docUrl = 'https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ'
text = pdfparser(docUrl)

nlp = spacy.load("el_core_news_lg")

doc = nlp(text)
# print(text)

my_doc_cleaned = [token for token in doc if not token.is_stop and not token.is_punct]

# print("\tENTITIES")
# for entity in doc.ents:
#   print(entity.text,'--- ',entity.label_)
#
# print("\n\n\n\tPART OF SPEECH")
# for token in my_doc_cleaned:
#   print(token.text,'---- ',token.pos_)

print(doc)
# for token in doc:
#   if token.like_num and token.i<len(my_doc_cleaned)-1:
#     index_of_next_token = token.i + 1
#     next_token = doc[index_of_next_token]
#     print(token.text, " ", next_token.text)
#     if next_token.text == '€':
#       print("Euros: " , token.text)
