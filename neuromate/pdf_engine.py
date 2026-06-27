# =========================================================
# NeuroMate PDF Engine
# Core PDF Generator
# =========================================================

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib import colors

import arabic_reshaper
from bidi.algorithm import get_display

from neuromate.config import (
    PAGE_SIZE,
    LEFT_MARGIN,
    RIGHT_MARGIN,
    TOP_MARGIN,
    BOTTOM_MARGIN,
    FONT_REGULAR,
    FONT_BOLD,
    BLACK,
    WHITE,
    BLUE,
    SILVER
)

# =========================================================
# TEXT PROCESSING (Arabic Fix)
# =========================================================

def fix_text(text: str) -> str:
    """
    Fix Arabic text direction for ReportLab
    """
    if not text:
        return ""

    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    return bidi_text


# =========================================================
# MAIN ENGINE CLASS
# =========================================================

class NeuroMatePDF:

    def __init__(self, output_path="output"):
        self.output_path = output_path
        self.story = []

        self.file_path = None

        # Styles
        self.styles = getSampleStyleSheet()

        self.title_style = ParagraphStyle(
            "TitleStyle",
            parent=self.styles["Heading1"],
            fontSize=28,
            alignment=TA_CENTER,
            textColor=BLUE,
            spaceAfter=20
        )

        self.subtitle_style = ParagraphStyle(
            "SubtitleStyle",
            parent=self.styles["Normal"],
            fontSize=14,
            alignment=TA_CENTER,
            textColor=SILVER,
            spaceAfter=30
        )

        self.section_title_style = ParagraphStyle(
            "SectionTitle",
            parent=self.styles["Heading2"],
            fontSize=18,
            alignment=TA_RIGHT,
            textColor=BLUE,
            spaceAfter=10
        )

        self.body_style = ParagraphStyle(
            "BodyStyle",
            parent=self.styles["Normal"],
            fontSize=11,
            alignment=TA_RIGHT,
            textColor=WHITE,
            leading=18
        )

        self.quote_style = ParagraphStyle(
            "QuoteStyle",
            parent=self.styles["Normal"],
            fontSize=12,
            alignment=TA_CENTER,
            textColor=SILVER,
            italic=True,
            spaceAfter=20
        )

    # =====================================================
    # DOCUMENT INIT
    # =====================================================

    def create_document(self):
        """
        Initialize PDF document
        """
        self.file_path = os.path.join(self.output_path, "temp.pdf")

        self.doc = SimpleDocTemplate(
            self.file_path,
            pagesize=PAGE_SIZE,
            rightMargin=RIGHT_MARGIN,
            leftMargin=LEFT_MARGIN,
            topMargin=TOP_MARGIN,
            bottomMargin=BOTTOM_MARGIN
        )

    # =====================================================
    # COVER PAGE
    # =====================================================

    def add_cover(self, title, subtitle="", description=""):

        self.story.append(Spacer(1, 120))

        self.story.append(
            Paragraph(fix_text(title), self.title_style)
        )

        if subtitle:
            self.story.append(
                Paragraph(fix_text(subtitle), self.subtitle_style)
            )

        if description:
            self.story.append(
                Paragraph(fix_text(description), self.body_style)
            )

        self.story.append(PageBreak())

    # =====================================================
    # QUOTE PAGE
    # =====================================================

    def add_quote(self, text):

        self.story.append(Spacer(1, 200))

        self.story.append(
            Paragraph(f"“{fix_text(text)}”", self.quote_style)
        )

        self.story.append(PageBreak())

    # =====================================================
    # SECTION PAGE
    # =====================================================

    def add_section(self, title, content):

        self.story.append(
            Paragraph(fix_text(title), self.section_title_style)
        )

        self.story.append(Spacer(1, 10))

        paragraphs = content.strip().split("\n")

        for p in paragraphs:
            if p.strip():
                self.story.append(
                    Paragraph(fix_text(p.strip()), self.body_style)
                )
                self.story.append(Spacer(1, 10))

        self.story.append(PageBreak())

    # =====================================================
    # SAVE PDF
    # =====================================================

    def save(self, filename="output.pdf"):

        output_file = os.path.join(self.output_path, filename)

        self.doc.build(self.story)

        os.rename(self.file_path, output_file)

        return output_file
