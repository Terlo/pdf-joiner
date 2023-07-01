import os
from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger  ,PdfReader, PdfWriter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Create uploads directory if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Get the uploaded files
    files = request.files.getlist('pdfs')


    # Merge the PDFs
    output_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
    merger = PdfMerger()

    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        pdf = PdfReader(file_path)
        merger.append(pdf)

    merger.write(output_pdf_path)
    merger.close()

    return render_template('download.html')

@app.route('/download')
def download():
    merged_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
    return send_file(merged_pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
