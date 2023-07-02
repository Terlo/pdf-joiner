import PyPDF2
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


def createpdf(title_content,body_content):
        
        # titl = pdfGenerator.sanitize_filename(title_content)
        
        titl = f"{title_content}.pdf"
        doc = SimpleDocTemplate(titl, pagesize=letter)
        styles = getSampleStyleSheet()

        title = f"<para align='center'>{title_content}.<font size=14></font></para>"
        body = f"<para align='justify'><font size=12>{body_content}.</font></para>"

        title = Paragraph(title, styles['Title'])
        body = Paragraph(body, styles['Normal'])

        elements = []
        elements.append(title)
        elements.append(body)

        doc.build(elements)

# Trying to open a random Wikipedia article
# Special:Random opens random articles
res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
res.raise_for_status()

# Parsing the HTML content
wiki = BeautifulSoup(res.text, "html.parser")

# Extracting the heading
heading = wiki.find("h1").text

# Extracting the paragraphs
paragraphs = [p.getText() for p in wiki.select("p")]
pgs = ''.join(str(element) for element in paragraphs)

print(paragraphs,sep="\n")



createpdf(heading,pgs)



