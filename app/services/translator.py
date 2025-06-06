from transformers import MarianMTModel, MarianTokenizer

def load_translation_model(model_name):
    print(f"Loading model and tokenizer for: {model_name}")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name, use_safetensors=True)  
    print(f"Loaded {model_name} successfully")
    return tokenizer, model

sv_en_tokenizer, sv_en_model = load_translation_model("Helsinki-NLP/opus-mt-sv-en")
en_ar_tokenizer, en_ar_model = load_translation_model("Helsinki-NLP/opus-mt-en-ar")

def translate(text, tokenizer, model):
    print(f"Translating text: {text}")
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    print(f"Tokenized inputs: {inputs}")
    translated = model.generate(**inputs)
    decoded = tokenizer.decode(translated[0], skip_special_tokens=True)
    print(f"Translated text: {decoded}")
    return decoded

def translate_sv_to_ar(text_sv):
    print(f"Starting Swedish to Arabic translation for: {text_sv}")
    english = translate(text_sv, sv_en_tokenizer, sv_en_model)
    print(f"Intermediate English translation: {english}")
    arabic = translate(english, en_ar_tokenizer, en_ar_model)
    print(f"Final Arabic translation: {arabic}")
    return text_sv, arabic, english

def translate_en_to_ar(text_en):
    print(f"Starting English to Arabic translation for: {text_en}")
    arabic = translate(text_en, en_ar_tokenizer, en_ar_model)
    print(f"Translated Arabic text: {arabic}")
    return text_en, arabic

def transalte_en_to_ar_and_danish(text_en): 
    print(f"Starting English to Arabic translation for: {text_en}")
    arabic = translate(text_en, en_ar_tokenizer, en_ar_model)
    danish = translate(text_en, en_ar_tokenizer, en_ar_model)
    print(f"Translated Arabic text: {arabic}")
    return text_en, arabic, danish

