from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


app = Flask(__name__)

def generate_pdf(button_pressed):
   
    min_length = 0;max_length=0;
    print(button_pressed)
    if button_pressed == "Long":
        min_length=17;max_length=25
    if button_pressed == "Medium":
        min_length=10;max_length=17
    if button_pressed == "Short":
        min_length=6;max_length=10
    complete = False
    while complete == False:
        # Trying to open a random Wikipedia article
        res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        res.raise_for_status()

        # Parsing the HTML content
        wiki = BeautifulSoup(res.text, "html.parser")


        # Extracting the paragraphs
        paragraphs = [p.getText() for p in wiki.select("p")]
        print(f"LEN PARA:{len(paragraphs)}")



        if len(paragraphs)>min_length and len(paragraphs)<max_length:
            complete = True

    # Extracting the heading
    heading = wiki.find("h1").text
    body_content = "\n".join(paragraphs)

    filename = f"{heading}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    title = f"<para align='center'>{heading}.<font size=14></font></para>"
    body = f"<para align='justify'><font size=12>{body_content}.</font></para>"

    title = Paragraph(title, styles['Title'])
    body = Paragraph(body, styles['Normal'])

    elements = [title, body]
    
    doc.build(elements)
    return filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    button_pressed = request.form.get('button')
    
    filename = generate_pdf(button_pressed)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
