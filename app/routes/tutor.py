from fastapi import APIRouter
from pydantic import BaseModel
from app.services.translator import translate_sv_to_ar
from app.services.translator import translate_en_to_ar
from app.services.transliterate import transliterate_arabic
from app.services.gpt_helper import improve_translation_with_gpt
import os

router = APIRouter(prefix="/tutor", tags=["Tutor"])
USE_GPT = os.getenv("USE_GPT").lower() == "true"

class TranslateRequest(BaseModel):
    text: str

class TranslateResponse(BaseModel):
    arabic_script: str
    arabic_translit: str

class TranslateResponseSV(BaseModel):
    english: str
    arabic_script: str
    arabic_translit: str

@router.post("/sv", response_model=TranslateResponseSV)
async def translate_text(req: TranslateRequest):
    raw_arabic, english_text = translate_sv_to_ar(req.text)

    if USE_GPT:
        improved_arabic = improve_translation_with_gpt(raw_arabic, target_language="Arabic")
    else:
        improved_arabic = raw_arabic
        
    translit_text = transliterate_arabic(improved_arabic)

    return TranslateResponseSV(
        english=english_text,
        arabic_script=improved_arabic,
        arabic_translit=translit_text
    )

@router.post("/en", response_model=TranslateResponse)
async def translate_text(req: TranslateRequest):
    arabic_text = translate_en_to_ar(req.text)
    translit_text = transliterate_arabic(arabic_text)
    return TranslateResponse(arabic_script=arabic_text, arabic_translit=translit_text)



    