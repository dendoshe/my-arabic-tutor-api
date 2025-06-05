# Swedish-Arabic Tutor API

A RESTful API built with FastAPI provides translation between Swedish and Arabic fus'ha using Hugging Face’s MarianMT models. Ideal for Swedish speakers seeking to learn Arabic, without having to learn the Arabic script.  

## Features

- Translate Swedish text to Arabic
- Translate English text to Arabic 
- Powered by MarianMT models from Hugging Face

## API Endpoints

The API exposes two main translation routes under the `/tutor` prefix, designed for Swedish speakers learning Arabic fus'ha:

### POST `/tutor/sv`

- **Description:**  
  Translates Swedish text into Arabic fus'ha.  
  Returns the Arabic translation in Arabic script, a transliteration (Latin script), and the English intermediate translation for clarity.

- **Request body:**  
  ```json
  {
    "text": "Swedish text here"
  }

- **Response example:**  
  ```json
  {
    "english": "English intermediate translation",
    "arabic_script": "النص العربي المترجم",
    "arabic_translit": "al-nass al-‘arabī al-mutarjam"
  }

## Local set-up

### Prerequisites

- Python 3.9+
- PyTorch (2.2 or higher recommended)
- Transformers library
- SentencePiece (required for MarianMT tokenizer)
- FastAPI, Uvicorn

### Installation

```bash
git clone https://github.com/dendoshe/swedish-arabic-tutor.git
cd swedish-arabic-tutor
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt

## Running Locally

After installation, start the FastAPI server with Uvicorn by running:

```bash
uvicorn app.main:app
