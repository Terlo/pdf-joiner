import PyPDF2
import os

# Get the directory path where the PDF files are located
pdf_dir = 'dummy/'

# Create a new PDF object to hold all the merged PDFs
merged_pdf = PyPDF2.PdfMerger()

# List all the PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
pdf_files.sort()
print(pdf_files, sep='\n')
