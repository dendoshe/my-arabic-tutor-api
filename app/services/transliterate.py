
_mapping = {
    'ا': 'ā',   # long 'a' sound
    'ب': 'b',
    'ت': 't',
    'ث': 'th',  # voiceless dental fricative
    'ج': 'j',   # or 'dj' depending on dialect, 'j' is common
    'ح': 'ḥ',   # voiceless pharyngeal fricative (emphatic h)
    'خ': 'kh',  # voiceless velar fricative
    'د': 'd',
    'ذ': 'dh',  # voiced dental fricative
    'ر': 'r',
    'ز': 'z',
    'س': 's',
    'ش': 'sh',
    'ص': 'ṣ',   # emphatic s
    'ض': 'ḍ',   # emphatic d
    'ط': 'ṭ',   # emphatic t
    'ظ': 'ẓ',   # emphatic z
    'ع': 'ʿ',   # voiced pharyngeal fricative (ayn)
    'غ': 'gh',  # voiced velar fricative
    'ف': 'f',
    'ق': 'q',   # uvular stop
    'ك': 'k',
    'ل': 'l',
    'م': 'm',
    'ن': 'n',
    'ه': 'h',
    'و': 'w',   # or 'ū' when used as a long vowel
    'ي': 'y',   # or 'ī' when used as a long vowel
    'ء': 'ʾ',   # glottal stop hamza
    'ى': 'á',   # usually alif maqṣūrah, sounds like 'ā' or 'a' depending on context
    'ة': 'h',   # taa marbuta, sometimes 't' in construct forms
}


def transliterate_arabic(text_ar: str) -> str:
    return ''.join(_mapping.get(c, c) for c in text_ar)
