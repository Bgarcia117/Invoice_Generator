import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Gets everything that ends with .xlsx and turns it into a list
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Path(filepath).stem contains the filepath and returns the file name
    filename = Path(filepath).stem
    # Splits the filename and returns a list with both halves
    invoice_nr, date = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice # {invoice_nr}", ln=1)
    
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")



    pdf.output(f"PDFs/{filename}.pdf")