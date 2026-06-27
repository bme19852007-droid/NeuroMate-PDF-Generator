# =========================================================
# NeuroMate Styles System
# Visual Identity (Cinematic Design)
# =========================================================

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib import colors

from neuromate.config import (
    FONT_REGULAR,
    FONT_BOLD,
    FONT_SEMIBOLD,
    BLUE,
    WHITE,
    SILVER,
    GOLD
)

# =========================================================
# STYLE FACTORY CLASS
# =========================================================

class NeuroMateStyles:

    def __init__(self):
        self.styles = getSampleStyleSheet()

    # -----------------------------------------------------
    # TITLE STYLE (Cinematic Cover)
    # -----------------------------------------------------
    def title(self):

        return ParagraphStyle(
            "NM_Title",
            parent=self.styles["Heading1"],
            fontName=FONT_BOLD,
            fontSize=34,
            alignment=TA_CENTER,
            textColor=BLUE,
            spaceAfter=20
        )

    # -----------------------------------------------------
    # SUBTITLE STYLE
    # -----------------------------------------------------
    def subtitle(self):

        return ParagraphStyle(
            "NM_Subtitle",
            parent=self.styles["Normal"],
            fontName=FONT_REGULAR,
            fontSize=14,
            alignment=TA_CENTER,
            textColor=SILVER,
            spaceAfter=25
        )

    # -----------------------------------------------------
    # SECTION TITLE (Tech Noir Header)
    # -----------------------------------------------------
    def section_title(self):

        return ParagraphStyle(
            "NM_SectionTitle",
            parent=self.styles["Heading2"],
            fontName=FONT_BOLD,
            fontSize=18,
            alignment=TA_RIGHT,
            textColor=BLUE,
            spaceBefore=20,
            spaceAfter=10
        )

    # -----------------------------------------------------
    # BODY TEXT
    # -----------------------------------------------------
    def body(self):

        return ParagraphStyle(
            "NM_Body",
            parent=self.styles["Normal"],
            fontName=FONT_REGULAR,
            fontSize=11,
            leading=18,
            alignment=TA_RIGHT,
            textColor=WHITE
        )

    # -----------------------------------------------------
    # QUOTE STYLE (Cinematic Impact)
    # -----------------------------------------------------
    def quote(self):

        return ParagraphStyle(
            "NM_Quote",
            parent=self.styles["Normal"],
            fontName=FONT_SEMIBOLD,
            fontSize=13,
            leading=22,
            alignment=TA_CENTER,
            textColor=SILVER,
            italic=True,
            spaceBefore=30,
            spaceAfter=30
        )

    # -----------------------------------------------------
    # GOLD STYLE (Jallen Hask Special Identity)
    # -----------------------------------------------------
    def gold_title(self):

        return ParagraphStyle(
            "NM_Gold",
            parent=self.styles["Heading2"],
            fontName=FONT_BOLD,
            fontSize=18,
            alignment=TA_RIGHT,
            textColor=GOLD,
            spaceAfter=10
        )
