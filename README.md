# Merge PDFs Using Python

This Python project demonstrates how to merge multiple PDF files into one using the `PyPDF2` library. It's a simple solution that combines multiple PDF documents into a single file, which can be useful in various situations such as combining reports, invoices, or documents.

## How It Works

The script uses the `PyPDF2` library to append the pages from each PDF file into a merged PDF document. The code scans the folder for all `.pdf` files and merges them into a single PDF, which is then saved as `merged.pdf`.

## Requirements

- Python 3.x
- `PyPDF2` library

To install the required dependency, run:

```bash
pip install PyPDF2
```

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Srimathi10/Merge_pdf.git
   ```

2. Place the PDF files you want to merge in the `files/` directory.

3. Run the Python script to merge the PDFs:
   ```bash
   python main.py
   ```

4. After the script runs successfully, the merged PDF will be saved as `merged.pdf` in the same directory.

## Blog Post

For a detailed explanation and tutorial on how this script works, check out my blog post:  
[Blog Post: Merging PDF Files Using Python](https://dev.to/srimathi10/blog-post-merging-pdf-files-using-python-3n5j)

## License

This project is licensed under the MIT License.

