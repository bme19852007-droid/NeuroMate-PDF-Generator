# =========================================================
# NeuroMate Utilities
# =========================================================

import arabic_reshaper
from bidi.algorithm import get_display


def fix_text(text):
    """
    Fix Arabic text rendering for ReportLab.
    """
    if not text:
        return ""

    reshaped = arabic_reshaper.reshape(str(text))
    return get_display(reshaped)
