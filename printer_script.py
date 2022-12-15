# OPTIONS
import os
from PyPDF2 import PdfReader, PdfWriter

import commonmark
import tqdm
import pdfkit


PRINT_TWO_SIDED = True # Will make sure experiments always start on an even page
PRINT_SPECIFIC_EXPERIMENTS = None # List of experiments to print - will override the conditions below. Set to 'None' to use conditions below e.g. PRINT_SPECIFIC_EXPERIMENTS = ['Electrolysis', 'Air Streams']

# DEFINE CONDITIONS
def do_print_if(tags):
    return (
        ('Biology' in tags) and 
        ('Active' in tags)
    )

# Define CSS:
css = """<style>
    * {
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    }
</style>"""

# Read in all experiments
all_experiments = []
for directory in os.listdir('Experiments'):
    for file in os.listdir(f'Experiments/{directory}'):
        with open(f'Experiments/{directory}/{file}') as f:
            all_experiments.append((['Experiments', directory, file], f.read()))

# Extracting Tags
def extract_tags(string):
    tags_section = string.split('<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->')[1].split('<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->')[0]
    tags_section = tags_section.replace('\n','')
    tags_list_with_comments = tags_section.split('**')
    tags_list_with_comments_cleaned = [x.strip() for x in tags_list_with_comments if x!='']
    tags_list = [x for x in tags_list_with_comments_cleaned if ((x[0]!='(') or (x[-1]!=')'))]
    return tags_list

if not os.path.isdir('temp'):
    os.makedirs('temp')
to_print = []

if PRINT_SPECIFIC_EXPERIMENTS is None:
    printer_experiments = [
        data for data in all_experiments
        if do_print_if(extract_tags(data[1]))
    ]
else:
    printer_experiments = [
        data for data in all_experiments
        if (data[0][2][:-3] in PRINT_SPECIFIC_EXPERIMENTS) 
    ]
    
errors = []
for location, experiment in tqdm.tqdm(printer_experiments):
    parser = commonmark.Parser()
    ast = parser.parse(experiment)
    renderer = commonmark.HtmlRenderer()
    html = css + '\n' + renderer.render(ast)
    with open(f'temp/{location[2][:-3]}.html', "w") as f:
        f.write(html)
    try:
        pdfkit.from_file(f'temp/{location[2][:-3]}.html', f'temp/{location[2][:-3]}.pdf')
    except Exception as e:
        errors.append(f'The script encountered a {str(e).split(":")[2].strip()} when converting the risk assessment for the experiment {location[2][:-3]}. This is often caused by an old image still being listed in the markdown. While there may still be a PDF output for this, you should check there are no errors and correct the risk assessment.')
    os.remove(f'temp/{location[2][:-3]}.html')

writer = PdfWriter()
for experiment_pdf in os.listdir('temp'):
    reader = PdfReader(f"temp/{experiment_pdf}")
    number_of_pages = len(reader.pages)

    for page in reader.pages:
        writer.add_page(page)

    if PRINT_TWO_SIDED and (number_of_pages%2==1):
        writer.add_blank_page()

writer.write('printable.pdf')

for experiment_pdf in os.listdir('temp'):
    os.remove(f"temp/{experiment_pdf}")
os.removedirs('temp')
print(f'{len(errors)} experiment(s) had errors in their conversion - the errors are listed below:')
print('\n'.join(errors))