import sys

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import json
import dload


def pdfparser(data):
    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data = retstr.getvalue()

    print(data)

agrUrl = "https://www.diavgeia.gov.gr/luminapi/api/search/export?q=organizationUid:%22100010899%22&sort=recent&wt=json"
agrjsonurl = dload.json(agrUrl)
# agrJson = json.load(agrUrl)
print(agrjsonurl)

docUrl = 'https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ'
# pdfparser('https://diavgeia.gov.gr/doc/ΩΕΚ64653ΠΓ-2ΞΡ')

# if __name__ == '__main__':
#     pdfparser(sys.argv[1])
