import logging
import socket
import sys
import urllib
from urllib.error import HTTPError, URLError
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import pdfminer
import io
import json
from urllib.request import urlopen


def pdfparser(url):
    codec = 'utf-8'
    response = requests.get(url)
    try:
        response = requests.get(url)
    except HTTPError as error:
        logging.error('Data not retrieved because %s\nURL: %s', error, url)
    except URLError as error:
        if isinstance(error.reason, socket.timeout):
            # logging.error('socket timed out - URL %s', url)
            pass
        else:
            logging.error('some other error happened')
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

    print("Extracting Json Objects...")
    for count, obj in enumerate(inside_jsonobj):
        if count > 80:
            doclist.append(pdfparser(obj['documentUrl']))
        # print(count)
        if count % 50 == 0:
            print("Json Object ", count)
        # print(obj)
        if count > 480:
            break
    return doclist


def to_doccano_dataset(textList: list,filename: str):
    print("Writing dataset to txt file...")
    textFile = open(filename, 'w')
    for element in textList:
        textFile.write(element + "\n")
    textFile.close()


def replace_newline_with_space(textList: list):
    print("Replacing newline with space in text dataset...")
    resultList = []
    for element in textList:
        resultList.append(element.replace('\n', ' '))
    return resultList


agrUrl = "https://www.diavgeia.gov.gr/luminapi/api/search/export?q=organizationUid:%22100015981%22&sort=recent&wt=json"
docUrl = 'https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ'

doclist = jsontodocs(agrUrl)
mylist = replace_newline_with_space(doclist)
to_doccano_dataset(mylist,"doccano_agr_dataset_400.txt")
# pdfparser(doclist[5])
# print(pdfminer.__version__)
# pdfparser(docUrl)

# if __name__ == '__main__':
#     pdfparser(sys.argv[1])
