import sys

import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import pdfminer
import io
import json
from urllib.request import urlopen


def pdfparser(data):
    codec = 'utf-8'
    response = requests.get(data)
    with io.BytesIO(response.content) as open_pdf_file:
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()

        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        # Create a PDF interpreter object.
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.

        for page in PDFPage.get_pages(open_pdf_file):
            interpreter.process_page(page)
            data = retstr.getvalue()

        return data


def jsontodocs(url):
    data = requests.get(url)
    jsonobj = json.loads(data.text)
    # jstring=json.dumps(obj, indent=4, ensure_ascii=False).encode('utf8')
    # print(jstring.decode())
    doclist = []
    # json in gov link is a json object, that contains a json array
    # which in turn contains each object with the information needed
    # as well as the document url
    inside_jsonobj = jsonobj['decisionResultList']
    for j in inside_jsonobj:
        doclist.append(j['documentUrl'])
    return doclist


agrUrl = "https://www.diavgeia.gov.gr/luminapi/api/search/export?q=organizationUid:%22100010899%22&sort=recent&wt=json"
docUrl = 'https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ'

# doclist = jsontodocs(agrUrl)
# pdfparser(doclist[5])
# print(pdfminer.__version__)
pdfparser(docUrl)

# if __name__ == '__main__':
#     pdfparser(sys.argv[1])
