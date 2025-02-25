import PyPDF2
import glob
from pathlib import Path

# Create a list of PDF filepaths
filepaths = glob.glob("files/*.pdf")

# Create a PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# Go through each PDF file and append to the merger object
for filepath in filepaths:
    # Append the current PDF file to the merger
    pdf_merger.append(filepath)

# Output the merged PDF
with open("merged.pdf", "wb") as output_pdf:
    pdf_merger.write(output_pdf)

print("PDFs merged successfully into 'merged.pdf'")
