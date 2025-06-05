from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI() 

def improve_translation_with_gpt(text: str, target_language: str = "Arabic") -> str:
    prompt = (
        f"Please improve the following {target_language} translation for fluency, "
        f"clarity, and natural style. Keep the meaning unchanged but the gender of speaker is male:\n\n{text}"
    )
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300,
    )
    
    return response.choices[0].message.content.strip()
