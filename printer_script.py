# %%
import os
from PyPDF2 import PdfReader, PdfWriter

import tqdm
import pdfkit
import shutil
import pandoc

# %%
# OPTIONS
PRINT_TWO_SIDED = True # Will make sure experiments always start on an even page
PRINT_SPECIFIC_EXPERIMENTS = None # ["Plants", "Sweet Chromatography", "Potato Game", "Lung Model", "Greenhouse Effect", "Flame Tornado"]
# List of experiments to print - will override the conditions below. Set to None to use conditions below e.g. PRINT_SPECIFIC_EXPERIMENTS = ['Electrolysis', 'Air Streams']

# DEFINE CONDITIONS
def do_print_if(tags):
    return (
        ('Minor repairs needed' in tags or 
        'Active' in tags) and
        (('Standard' in tags) or 'Tour only' in tags) and
        not ('CBS only' in tags)
    )


# Read in all experiments
all_experiments = []
for directory in os.listdir('Experiments'):
    for file in os.listdir(f'Experiments/{directory}'):
        
        if file.endswith('.md'): # Skip files that are not markdown files
            
            with open(f'Experiments/{directory}/{file}', encoding='utf-8') as f:
                all_experiments.append((['Experiments', directory, file], f.read()))

# Extracting Tags
def extract_tags(string):
    tags_section = string.split('<!--- Start Tags (DO NOT REMOVE THIS COMMENT) --->')[1].split('<!--- End Tags (DO NOT REMOVE THIS COMMENT) --->')[0]
    tags_section = tags_section.replace('\n','')
    tags_list_with_comments = tags_section.split('**')
    tags_list_with_comments_cleaned = [x.strip() for x in tags_list_with_comments if x!='']
    tags_list = [x for x in tags_list_with_comments_cleaned if ((x[0]!='(') or (x[-1]!=')'))]
    return tags_list

if PRINT_SPECIFIC_EXPERIMENTS is None:
    
    printer_experiments = []
    
    for data in all_experiments:
        try:
            tags = extract_tags(data[1])
        except IndexError:
            print(f"No tags found in {data[0][2]}!")
        
        if do_print_if(tags) == True:
            printer_experiments.append(data)
            
else:
    printer_experiments = [
        data for data in all_experiments
        if (data[0][2][:-3] in PRINT_SPECIFIC_EXPERIMENTS) 
    ]
    
print(f"Found total of {len(printer_experiments)} risk assessments to export:")
for filename in sorted([expt[0][2] for expt in printer_experiments]):
    print(filename)
    
# %%

if not os.path.isdir('temp'):
    os.makedirs('temp')


# Copy all images into the temp/Images folder
if not os.path.isdir('temp/Images'):
    os.makedirs('temp/Images')
    
for dirpath, dirnames, files in os.walk('Experiments'):
    
    # Skip the rest of this iteration if the folder is not an image folder
    if not dirpath.endswith('Images'):
        continue
    
    for file in files:
        file_path = os.path.join(dirpath, file)
        shutil.copy(file_path, 'temp/Images')
        
# Copy the CHaOS logo
shutil.copy('CHaOS_Logo.svg', 'temp/Images')

# Code to insert the CHaOS logo
logo_md = '<img src="./Images/CHaOS_Logo.svg" style="width:5cm"> \n\n'

     
errors = []

for location, experiment in tqdm.tqdm(printer_experiments):
    try:
        # Add code for logo at beginning
        experiment = logo_md + experiment
        
        doc = pandoc.read(experiment, format='markdown')
        pandoc.write(doc, f'temp/{location[2][:-3]}.html', format='html', options=['-c pdf_format.css', '--webtex=https://latex.codecogs.com/svg.image?', '--standalone'])

        pdfkit.from_file(f'temp/{location[2][:-3]}.html', f'temp/{location[2][:-3]}.pdf', # css='pdf_format.css',
                         options={'encoding':'UTF-8', 'enable-local-file-access': None, 'user-style-sheet': 'pdf_format.css'})
        
    except Exception as e:
        errors.append(f'The script encountered a {str(e).split(":")[2].strip()} when converting the risk assessment for the experiment {location[2][:-3]}. This is often caused by an image linked in the Markdown which does not exist or is not in the correct location. While there may still be a PDF output for this, you should check there are no errors and correct the risk assessment.')
    # os.remove(f'temp/{location[2][:-3]}.html')
    

writer = PdfWriter()
for experiment_pdf in os.listdir('temp'):
    
    # Skip the rest of the iteration if file is not a pdf
    if not experiment_pdf.endswith('.pdf'): 
        continue
    
    reader = PdfReader(f"temp/{experiment_pdf}")
    number_of_pages = len(reader.pages)

    for page in reader.pages:
        writer.add_page(page)

    if PRINT_TWO_SIDED and (number_of_pages%2==1):
        writer.add_blank_page()

writer.write('printable.pdf')

# Delete the temp folder (and everything in it)
shutil.rmtree('temp')


print(f'{len(errors)} experiment(s) had errors in their conversion - the errors are listed below:')
print('\n'.join(errors))
# %%
