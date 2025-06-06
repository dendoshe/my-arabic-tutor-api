from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.translator import translate_sv_to_ar, translate_en_to_ar
from app.services.transliterate import transliterate_arabic
from app.services.gpt_helper import improve_translation_with_gpt
import os

router = APIRouter(prefix="/tutor", tags=["Tutor"])
USE_GPT = False; #os.getenv("USE_GPT", "false").lower() == "true"

class TranslateRequest(BaseModel):
    text: str

class TranslateResponse(BaseModel):
    english: str
    arabic_script: str
    arabic_translit: str

class TranslateResponseSV(BaseModel):
    swedish: str
    english: str
    arabic_script: str
    arabic_translit: str

async def process_translation(
    text: str,
    translator_func,
    include_english: bool = False
):
    swedish_text = None
    english_text = None

    if translator_func == translate_sv_to_ar and include_english:
        swedish_text, arabic_text, english_text = translator_func(text)
    elif translator_func == translate_en_to_ar and include_english:
        english_text, arabic_text = translator_func(text)
    else:
        arabic_text = translator_func(text)

    if USE_GPT:
        improved_arabic = improve_translation_with_gpt(arabic_text, target_language="Arabic")
    else:
        improved_arabic = arabic_text

    translit_text = transliterate_arabic(improved_arabic)

    return swedish_text, english_text, improved_arabic, translit_text


@router.post("/sv", response_model=TranslateResponseSV)
async def translate_sv(req: TranslateRequest):
    try:
        swedish, english, arabic_script, arabic_translit = await process_translation(
            req.text, translate_sv_to_ar, include_english=True
        )
        return TranslateResponseSV(
            swedish=swedish,
            english=english,
            arabic_script=arabic_script,
            arabic_translit=arabic_translit
        )
    except Exception as e:
        print(f"Error in /tutor/sv: {e}")
        raise HTTPException(status_code=500, detail="Translation failed")

@router.post("/en", response_model=TranslateResponse)
async def translate_en(req: TranslateRequest):
    try:
        _, english, arabic_script, arabic_translit = await process_translation(
            req.text, translate_en_to_ar, include_english=True
        )
        return TranslateResponse(
            english=english,
            arabic_script=arabic_script,
            arabic_translit=arabic_translit
        )
    except Exception as e:
        print(f"Error in /tutor/en: {e}")
        raise HTTPException(status_code=500, detail="Translation failed")
