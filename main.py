import PyPDF2
import os

#Get the directory path where the PDF files are located
pdf_dir = 'dummy/'

#Create a new PDF object to hold all the merged PDFs
merged_pdf = PyPDF2.PdfMerger()

#List all the PDF files in the directory.
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
pdf_files.sort()
print(pdf_files, sep='\n')

#Combine pdfs.
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    with open(pdf_path, 'rb') as pdf:
        merged_pdf.append(pdf)

# Save the merged PDF to a new file
with open('merged.pdf', 'wb') as output:
    merged_pdf.write(output)
