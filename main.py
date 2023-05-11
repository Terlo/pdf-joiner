import PyPDF2
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

#Get the directory path where the PDF files are located
pdf_dir = './'

#Create a new PDF object to hold all the merged PDFs
merged_pdf = PyPDF2.PdfMerger()

#List all the PDF files in the directory.
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
pdf_files.sort()
print(pdf_files, sep='\n')

page_array = []
#Combine pdfs.
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    # Create a PdfReader object from the file
    path_to_file = f"{pdf_dir}/{pdf_file}"
    pdf_reader = PyPDF2.PdfReader(path_to_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader._get_num_pages()
    page_array.append(num_pages)
    # Print the number of pages
    print(f'The PDF file has {num_pages} pages.')
    with open(pdf_path, 'rb') as pdf:
        merged_pdf.append(pdf)
#Create a new PDF object to hold all the merged PDFs
table_of_contents = PyPDF2.PdfMerger()
title_content = "TABLE OF CONTENTS"



titl = "TOC.pdf"
doc = SimpleDocTemplate(titl, pagesize=letter)
styles = getSampleStyleSheet()

title = f"<para align='center'>{title_content}.<font size=8></font></para>"
title = Paragraph(title, styles['Title'])
elements = []
elements.append(title)

cumulative_page_count=9

for x in range(len(pdf_files)):
    body = f"<para align='justify'><font size=6>{pdf_files[x]}.....................{cumulative_page_count}</font></para>"
    body = Paragraph(body, styles['Normal'])
    cumulative_page_count+=page_array[x]
    elements.append(body)

doc.build(elements) 
num_pages = 0
for input_pdf in table_of_contents.inputs:
    with open(input_pdf, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        num_pages += pdf_reader.getNumPages()
print(f"&&& {num_pages}")



# Save the merged PDF to a new file
with open('merged.pdf', 'wb') as output:
    merged_pdf.write(output)
