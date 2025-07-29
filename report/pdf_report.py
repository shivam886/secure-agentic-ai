# report/pdf_report.py

from fpdf import FPDF

class PDFReport:
    def __init__(self, outfile="report.pdf"):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def add_section(self, title, text):
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 8, text)

    def save(self):
        self.pdf.output("report.pdf")
