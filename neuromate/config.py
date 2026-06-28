# =========================================================
# NeuroMate Configuration
# =========================================================

import os

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# =========================================================
# PAGE SETTINGS
# =========================================================

PAGE_SIZE = LETTER

LEFT_MARGIN = 50
RIGHT_MARGIN = 50
TOP_MARGIN = 50
BOTTOM_MARGIN = 50


# =========================================================
# PROJECT PATHS
# =========================================================

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

FONTS_DIR = os.path.join(ROOT_DIR, "fonts")


# =========================================================
# REGISTER FONTS
# =========================================================

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_SEMIBOLD = "Helvetica-Bold"

try:

    pdfmetrics.registerFont(
        TTFont(
            "Cairo-Regular",
            os.path.join(FONTS_DIR, "Cairo-Regular.ttf")
        )
    )

    pdfmetrics.registerFont(
        TTFont(
            "Cairo-Bold",
            os.path.join(FONTS_DIR, "Cairo-Bold.ttf")
        )
    )

    pdfmetrics.registerFont(
        TTFont(
            "Cairo-SemiBold",
            os.path.join(FONTS_DIR, "Cairo-SemiBold.ttf")
        )
    )

    FONT_REGULAR = "Cairo-Regular"
    FONT_BOLD = "Cairo-Bold"
    FONT_SEMIBOLD = "Cairo-SemiBold"

    print("✓ Cairo Fonts Loaded")

except Exception:

    print("⚠ Cairo fonts not found -> Using Helvetica")


# =========================================================
# COLORS
# =========================================================

BLACK = HexColor("#050505")
WHITE = HexColor("#F4F4F4")

BLUE = HexColor("#00BFFF")

SILVER = HexColor("#BFC6CE")

GOLD = HexColor("#D4AF37")
