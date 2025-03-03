import logging
import socket

from urllib.error import HTTPError, URLError
import requests
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import pdfminer
import pandas as pd
import io
import json

from Utils.FeatherUtils import save_dict_list_to_feather, read_feather_local_dataset
from Utils.PathUtils import add_path_to_local_dataset_str
from Utils.documentUtils import replace_newline_with_space
from Utils.generalUtils import save_to_txt


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


def json_to_docs(url):
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
    return doclist


def json_to_meta(url: str, max_results: int):
    print("Requesting Json Objects...")
    data = requests.get(url)
    jsonobj = json.loads(data.text)
    meta_list = []

    # json in gov link is a json object, that contains a json array
    # which in turn contains each object with the information needed
    # as well as the document url
    inside_jsonobj = jsonobj['decisionResultList']

    print("Extracting ", max_results, " Json Objects...")
    for count, obj in enumerate(inside_jsonobj):
        if count < max_results:
            meta_list.append({
                'ada': obj['ada'],
                'protocolNumber': obj['protocolNumber'],
                'issueDate': obj['issueDate'],
                'submissionTimestamp': obj['submissionTimestamp'],
                'documentUrl': obj['documentUrl'],
                'subject': obj['subject'],
                'decisionTypeUid': obj['decisionTypeUid'],
                'decisionTypeLabel': obj['decisionTypeLabel'],
                'organizationUid': obj['organizationUid'],
                'organizationLabel': obj['organizationLabel']
            })
            if count % 50 == 0:
                print("Json Object ", count)
    return meta_list


def json_to_meta_obj(url: str, ada_q: str):
    print("Requesting Json Objects...")
    data = requests.get(url)
    jsonobj = json.loads(data.text)
    meta_obj = []

    # json in gov link is a json object, that contains a json array
    # which in turn contains each object with the information needed
    # as well as the document url
    inside_jsonobj = jsonobj['decisionResultList']

    for count, obj in enumerate(inside_jsonobj):
        if count % 50 == 0:
            print("Json Object ", count)
        if obj['ada'] == ada_q:
            meta_obj = {
                'ada': obj['ada'],
                'protocolNumber': obj['protocolNumber'],
                'issueDate': obj['issueDate'],
                'submissionTimestamp': obj['submissionTimestamp'],
                'documentUrl': obj['documentUrl'],
                'subject': obj['subject'],
                'decisionTypeUid': obj['decisionTypeUid'],
                'decisionTypeLabel': obj['decisionTypeLabel'],
                'organizationUid': obj['organizationUid'],
                'organizationLabel': obj['organizationLabel']
            }
            print(count)
            break

    return meta_obj


agrUrl = "https://www.diavgeia.gov.gr/luminapi/api/search/export?q=organizationUid:%22100015981%22&sort=recent&wt=json"
docUrl = 'https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ'
health_url = "https://diavgeia.gov.gr/luminapi/api/search/export?q=organizationUid:%22100010899%22&sort=recent&wt=json"
zeroUrl = "https://diavgeia.gov.gr/doc/ΨΤΙΦ465ΦΥΟ-45Π"
zeroADA = "ΨΤΙΦ465ΦΥΟ-45Π"
# data_list = json_to_meta(health_url, 60)
# feather_file = "DptOfHealth1000"
# save_dict_list_to_feather(data_list, feather_file)
# readF = read_feather_local_dataset(feather_file)
# print(readF)
# print(pdfminer.__version__)
# doclist = jsontodocs(Url)
# mylist = replace_newline_with_space(doclist)
# to_doccano_dataset(mylist,"doccano_agr_dataset_400.txt")
meta_obj = json_to_meta_obj(health_url,zeroADA)
text_save = replace_newline_with_space(pdfparser(meta_obj['documentUrl']))
save_to_txt(text_save, "zeroUrlText")
# save_to_txt(meta_obj['subject'],"zeroUrlSubject")
# print(pdfminer.__version__)
# pdfparser(docUrl)
