import json
from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import KeepTogether
import re
import os


def read_counter():
    counter = 0
    file_path = os.path.join(os.getcwd(), "counter.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            counter = data.get("counter", 0)
    return counter

def write_counter(counter):
    data = {"counter": counter}
    file_path = os.path.join(os.getcwd(), "counter.json")
    with open(file_path, "w") as file:
        json.dump(data, file)
        
def delete_pdf_files():
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        if filename.endswith(".pdf"):
            file_path = os.path.join(cwd, filename)
            os.remove(file_path)


def remove_number_in_brackets(text):
    # Use regular expression to match and remove number inside []
    result = re.sub(r'\[\d+\]', '', text)
    return result

app = Flask(__name__)

def draw_footer(canvas, doc,article_title,article_url):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)

    footer_text = f"Article sourced from Wikipedia:{article_title}"
    
    footer_text2 =f"Retrieved from {article_url}"
    footer_text3 =f"Page: {doc.page}"

    # Set the position of the footer text
    text_x = inch
    text_y = inch / 2

    # Draw the footer text
    canvas.drawString(text_x, text_y, footer_text)
    canvas.drawString(text_x, text_y/2, footer_text2)
    canvas.drawString(text_x, text_y/4, footer_text3)
    canvas.restoreState()

def generate_pdf(button_pressed):
    min_length = 0
    max_length = 0

    if button_pressed == "Long":
        min_length = 17
        max_length = 25
    elif button_pressed == "Medium":
        min_length = 10
        max_length = 17
    elif button_pressed == "Short":
        min_length = 6
        max_length = 10
    else:
        min_length = 8
        max_length = 17

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

        if min_length <= len(paragraphs) <= max_length:
            complete = True


    elements=[]
    pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))
   
    # Extracting the heading
    heading = wiki.find("h1").text

    article_title = heading
    article_route = heading.replace(" ","_")
    article_url = f"https://en.wikipedia.org/wiki/{article_route}"

    filename = f"{heading}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    title = f"<para align='left'>{heading}.<font size=14></font></para>"
    title = Paragraph(title, styles['Title'])
    elements.append(title)
    
    for p in paragraphs:
        body_content = f"{remove_number_in_brackets(p)}"
        body = f"<para align='justify'><font size=12>{body_content}</font></para>"
        body = Paragraph(body, styles['Normal'])
        elements.append(body)

    # Set the footer function as the onLaterPage callback
    doc.build(
        elements,
        onFirstPage=lambda canvas, doc: draw_footer(canvas, doc, article_title, article_url),
        onLaterPages=lambda canvas, doc: draw_footer(canvas, doc, article_title, article_url)
        )

    return filename




@app.route('/')
def index():
    delete_pdf_files()
    return render_template('index.html',counter = read_counter())

@app.route('/generate', methods=['POST'])
def generate():
    button_pressed = request.form.get('button')
    
    filename = generate_pdf(button_pressed)
    
    counter = read_counter()
    counter += 1
    write_counter(counter)
    return send_file(filename, as_attachment=True)
    # Example usage

if __name__ == '__main__':
    app.run(debug=False)
