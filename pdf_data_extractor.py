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

import tabula

file = "payslips/W_E_13_Dec_2020.pdf"

tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)
# output just the first table in the PDF to a CSV
tabula.convert_into(file, "output.csv", output_format="csv", pages='all')
