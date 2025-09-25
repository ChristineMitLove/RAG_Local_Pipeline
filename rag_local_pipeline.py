# Download PDF file
# %% 
# Section 1: Download PDF

import os
import requests

# Get PDF document
pdf_path = "human-nutrition-text.pdf"

# Download PDF if it doesn't already exist
if not os.path.exists(pdf_path):
    print("File doesn't exist, downloading...")

    url = "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"

    response = requests.get(url)
    if response.headers.get('Content-Type') == 'text/html':
        print('Your url is of text/html format. Please find a correct url of your PDF document.')
    else:
        filename = pdf_path
        
        # Check if the request was successful
        if response.status_code == 200:
        # Open a file in binary write mode and save the content to it
            with open(filename, "wb") as file:
                file.write(response.content)
                print(f"The file has been downloaded and saved as {filename}")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")
else:
    print(f"File {pdf_path} exists.")

  
# %%
# After download the file, here we open it and process it. 

import fitz
from tqdm.auto import tqdm

def text_
