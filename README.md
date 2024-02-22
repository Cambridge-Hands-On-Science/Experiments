# Experiments

This is the new system for storing the experiments and risk assessments. Risk assessments are written in markdown (specifcally commonmark) - https://commonmark.org

They can be edited on any text editor.

## Conversion Script

The conversion script is a python file that converts the experiments to a printable pdf.

The Pandoc program needs to be installed; please follow the instructions on this website: https://pandoc.org/installing.html (Pandoc v. 2.19.2 is confirmed to be working; later versions may not be!)

It also requries Wkhtmltopdf. On MacOS, this can be installed using `brew install homebrew/cask/wkhtmltopdf`.
Installation instructions for other operating systems can be found at https://wkhtmltopdf.org (Wkhtmltopdf v. 0.12.6 is confirmed to be working; later versions may not be!)

The following Python libraries are also needed: `PyPDF2`, `commonmark`, `tqdm`, `pdfkit`. These can be installed with the following command:

```
pip install PyPDF2 pandoc tqdm pdfkit
```

### Troubleshooting

If you are having errors relating to Python not being able to find the executable, ensure that the wkhtmltopdf and pandoc bin folders are listed in the system path environment variable (it should do this automatically when installing, but sometimes doesn't)
