# PDF to Polish Translation Tool
This tool extracts text from PDF files, translates it into Polish using OpenAI's API, saves the translated content into Markdown files, and finally converts the Markdown files into PDFs.

## What the Program Does

**PDF Extraction**: Reads PDF files from the `./input` directory and extracts the text.

**Translation**: Uses OpenAI's API to translate the extracted text into Polish.

**Save to Markdown**: Saves the translated text into Markdown files in the `./output_md` directory.

**Markdown to PDF Conversion**: Converts the Markdown files into PDF format and saves them in the `./output_pdf` directory.


## Installation
### Required Packages and Software
You will need to have the following packages and software installed:

*Python 3*
*PyPDF2*
*openai*
*pandoc*
*xelatex*

You can install the necessary Python packages using pip:

```bash
pip install PyPDF2 openai
```

For *pandoc* and *xelatex*, please follow the respective installation guides for your operating system.

### Environment Variables
Set the following environment variables:

- **OPENAI_ORGANIZATION_KEY**: Your OpenAI organization key.
- **OPENAI_API_KEY**: Your OpenAI API key.
You can set these using the following commands:

```bash
export OPENAI_ORGANIZATION_KEY=your-organization-key
export OPENAI_API_KEY=your-api-key
```

## How to Run
1. Place the PDF files you want to translate into the `./input` folder.
Run the script using:
```bash
python your_script_name.py
```
The translated files will be saved in the `./output_md` directory, and the converted PDFs will be stored in the `./output_pdf` directory.