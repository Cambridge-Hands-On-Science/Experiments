# Experiments

This is the new system for storing the experiments and risk assessments. Risk assessments are written in markdown (specifcally commonmark) - https://commonmark.org

They can be edited on any text editor.

## Conversion Script

The conversion script is a python file that converts the experiments to a printable pdf.

The Pandoc program needs to be installed; please follow the instructions on this website: https://pandoc.org/installing.html (Pandoc v. 3.8.3 is confirmed to be working; later versions may not be!)

Git must also be installed, instructions for which can be found at https://git-scm.com/install (Windows v 2.52.0 x64 is definitely working)

It also requries Wkhtmltopdf. On MacOS, this can be installed using `brew install homebrew/cask/wkhtmltopdf`.
Installation instructions for other operating systems can be found at https://wkhtmltopdf.org (Wkhtmltopdf v. 0.12.6 is confirmed to be working; later versions may not be!)

The following Python libraries are also needed: `PyPDF2`, `commonmark`, `tqdm`, `pdfkit`. These can be installed with the following command:

```
pip install PyPDF2 pandoc tqdm pdfkit
```

### Troubleshooting

If you are having errors relating to Python not being able to find the executable, ensure that the wkhtmltopdf and pandoc bin folders are listed in the system path environment variable (it should do this automatically when installing, but sometimes doesn't)

### Running the script (Windows)

First edit the script to print the specific files you want and change the name of the output pdf

To run the script in windows, first ensure all the above programs are installed. Then use PowerShell and enter:
```
git clone https://github.com/Cambridge-Hands-On-Science/Experiments.git
cd Experiments
```
Then check the required binaries are on PATH:
```
pandoc --version
wkhtmltopdf --version
```
Finally run printer_script.py
```
python printer_script.py
```
