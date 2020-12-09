from urllib.request import urlopen

from pdfminer.high_level import extract_text


def pdf_to_text(data):
    with urlopen(data) as wFile:
        text = extract_text(wFile)
    return text

docUrl = 'https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ'
print(pdf_to_text(docUrl))

