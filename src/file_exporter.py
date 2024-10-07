import os
from fpdf import FPDF

class PdfExporter:
    def __init__(self):
        # Set the directory for PDF files
        self.files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdf files')
        # Create the directory if it doesn't exist
        os.makedirs(self.files_dir, exist_ok=True)

    def export_to_pdf(self, fantasy_recap, filename="fantasy_recap.pdf"):
        # Create a PDF object
        pdf = FPDF()
        
        # Add a page
        pdf.add_page()
        
        # Set font
        pdf.set_font("Arial", size=12)
        
        # Split the recap into lines
        lines = fantasy_recap.split('\n')
        
        # Add each line to the PDF
        for line in lines:
            pdf.multi_cell(0, 10, txt=line, align='L')
        
        # Construct the full file path
        file_path = os.path.join(self.files_dir, filename)
        
        # Save the pdf
        pdf.output(file_path)
