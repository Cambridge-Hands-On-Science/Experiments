# Experiments
This is the new system for storing the experiments and risk assessments. Risk assessments are written in markdown (specifcally commonmark) - https://commonmark.org

They can be edited on any text editor.

## Conversion Script
The conversion script is a python file that converts the experiments to a printable pdf.
The following libraries are needed `PyPDF2`, `commonmark`, `tqdm`, `pdfkit`. These can be installed with the following command:
```
pip install PyPDF2 commonmark tqdm pdfkit
```
It also requries wkhtmltopdf. On MacOS, this can be installed using `brew install homebrew/cask/wkhtmltopdf`.
Installation instructions for other operating systems can be found at https://wkhtmltopdf.org



