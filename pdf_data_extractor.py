"""
 file resposble for extracting data from recently collected payslips
 and constucting a payslip class then adding such classes to our postgres database
"""

# import PyPDF2
# # pdf file object
# # you can find find the pdf file with complete code in below
# pdfFileObj = open('payslips/W_E_13_Dec_2020.pdf', 'rb')
# # pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# # number of pages in pdf
# # a page object
# pageObj = pdfReader.getPage(0)
# # extracting text from page.
# # this will print the text you can also save that into String
# grossEarningIdx = pageObj.extractText().find("Total Earnings: ")
# netEarningIdx = pageObj.extractText().find("Net Pay: ")
#
# print(pageObj.extractText()[grossEarningIdx:netEarningIdx])
#print(pageObj.extractText())

# import tabula
#
file = "payslips/W_E_13_Dec_2020.pdf"
#
# tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)
# # output just the first table in the PDF to a CSV
# tabula.convert_into(file, "output.csv", output_format="csv", pages='all')
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re
import csv


def convert_pdf_to_html(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0 #is for all
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

print(convert_pdf_to_html(file))
