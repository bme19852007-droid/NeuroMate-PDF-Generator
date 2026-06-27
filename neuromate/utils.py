import arabic_reshaper
from bidi.algorithm import get_display


def fix_text(text: str) -> str:
    if not text:
        return ""
    return get_display(arabic_reshaper.reshape(text))
