# =========================================================
# NeuroMate Style System
# =========================================================

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT

from neuromate.config import (
    FONT_REGULAR,
    FONT_BOLD,
    FONT_SEMIBOLD,
    BLUE,
    WHITE,
    SILVER,
    GOLD,
)


class NeuroMateStyles:

    def __init__(self):
        self.styles = getSampleStyleSheet()

    # -------------------------------------------------
    # Main Title
    # -------------------------------------------------

    def title(self):

        return ParagraphStyle(
            "Title",
            parent=self.styles["Heading1"],
            fontName=FONT_BOLD,
            fontSize=30,
            leading=36,
            alignment=TA_CENTER,
            textColor=BLUE,
            spaceAfter=18,
        )

    # -------------------------------------------------
    # Subtitle
    # -------------------------------------------------

    def subtitle(self):

        return ParagraphStyle(
            "Subtitle",
            parent=self.styles["Heading2"],
            fontName=FONT_SEMIBOLD,
            fontSize=16,
            leading=22,
            alignment=TA_CENTER,
            textColor=SILVER,
            spaceAfter=12,
        )

    # -------------------------------------------------
    # Section Title
    # -------------------------------------------------

    def section_title(self):

        return ParagraphStyle(
            "SectionTitle",
            parent=self.styles["Heading2"],
            fontName=FONT_BOLD,
            fontSize=20,
            leading=28,
            alignment=TA_RIGHT,
            textColor=BLUE,
            spaceAfter=12,
        )

    # -------------------------------------------------
    # Body
    # -------------------------------------------------

    def body(self):

        return ParagraphStyle(
            "Body",
            parent=self.styles["BodyText"],
            fontName=FONT_REGULAR,
            fontSize=12,
            leading=24,
            alignment=TA_RIGHT,
            textColor=WHITE,
            spaceAfter=8,
        )

    # -------------------------------------------------
    # Quote
    # -------------------------------------------------

    def quote(self):

        return ParagraphStyle(
            "Quote",
            parent=self.styles["BodyText"],
            fontName=FONT_SEMIBOLD,
            fontSize=15,
            leading=26,
            alignment=TA_CENTER,
            textColor=SILVER,
            italic=True,
            spaceAfter=20,
        )

    # -------------------------------------------------
    # Highlight
    # -------------------------------------------------

    def highlight(self):

        return ParagraphStyle(
            "Highlight",
            parent=self.styles["BodyText"],
            fontName=FONT_BOLD,
            fontSize=14,
            leading=22,
            alignment=TA_RIGHT,
            textColor=GOLD,
            spaceAfter=10,
        )
