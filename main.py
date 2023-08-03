import PyPDF2
import os
import openai
import subprocess

openai.organization = os.getenv('OPENAI_ORGANIZATION_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')
PROMPT = "You are the world's best translator into Polish. The user will provide you with content that you only need to translate into Polish and nothing else. You must keep the original meaning of the text. Reformat to markdown and good view this tekst."

def extract_text_from_pdf(pdf_path: str) -> str:
  with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    file_name = pdf_path.split(os.path.sep)[-1]
    for page_number, page in enumerate(reader.pages):
      print("Page: " + str(page_number + 1) + "/" + str(len(reader.pages)))
      text = page.extract_text()
      translated_text = openAI_request(text)
      save_to_file(translated_text, file_name.split('.')[0])
  return text

def save_to_file(translated_text: str, file_title: str) -> None:
  output_file_path = os.path.join('./output_md', f'{file_title}.md')
  with open(output_file_path, 'a', encoding='utf-8') as output_file:
    output_file.write(translated_text)

def openAI_request(text: str) -> str:
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "user", "content": PROMPT + """
Text:###
        """ + text + "###"}
    ]
  )
  return completion.choices[0].message['content']

def convert_markdown_to_pdf(input_file: str, output_file: str) -> None:
    try:
        subprocess.run(['pandoc', input_file, '-o', output_file, '--pdf-engine=xelatex'], check=True)
        print(f'Plik {input_file} został pomyślnie przekonwertowany na {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Wystąpił błąd podczas konwersji: {e}')

input_directory = "./input"
for filename in os.listdir(input_directory):
  if filename.endswith(".pdf"):
    pdf_path = os.path.join(input_directory, filename)
    print(f"Processing {pdf_path}...")
    extract_text_from_pdf(pdf_path)

output_md_directory = "./output_md/"
output_pdf_directory = "./output_pdf/"
for filename in os.listdir(output_md_directory):
  if filename.endswith(".md"):
    convert_markdown_to_pdf(output_md_directory + filename, output_pdf_directory + filename.split('.')[0] + ".pdf")

