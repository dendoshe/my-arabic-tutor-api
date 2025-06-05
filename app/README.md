# Swedish-Arabic Tutor API

A RESTful API built with FastAPI provides translation between Swedish and Arabic fus'ha using Hugging Face’s MarianMT models. Ideal for swedish speakers seeking to learn arabic, without having to learn the arabic script.  

## Features

- Translate Swedish text to Arabic and vice versa
- Powered by MarianMT models from Hugging Face

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
