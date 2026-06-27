# =========================================================
# NeuroMate PDF Engine - CLEAN VERSION
# =========================================================

import os
from reportlab.platypus import SimpleDocTemplate, Spacer, PageBreak

from neuromate.config import (
    PAGE_SIZE,
    LEFT_MARGIN,
    RIGHT_MARGIN,
    TOP_MARGIN,
    BOTTOM_MARGIN
)

from neuromate.styles import NeuroMateStyles
from neuromate.components import NeuroMateComponents

import arabic_reshaper
from bidi.algorithm import get_display


# =========================================================
# TEXT FIX
# =========================================================

def fix_text(text: str) -> str:
    if not text:
        return ""
    return get_display(arabic_reshaper.reshape(text))


# =========================================================
# ENGINE
# =========================================================

class NeuroMatePDF:

    def __init__(self, output_path="output"):

        self.output_path = output_path
        self.file_path = None
        self.story = []

        self.styles = NeuroMateStyles()
        self.components = NeuroMateComponents(self.styles)

        self.doc = None

    # -----------------------------------------------------
    # INIT DOCUMENT
    # -----------------------------------------------------

    def create_document(self):

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        self.file_path = os.path.join(self.output_path, "temp.pdf")

        self.doc = SimpleDocTemplate(
            self.file_path,
            pagesize=PAGE_SIZE,
            rightMargin=RIGHT_MARGIN,
            leftMargin=LEFT_MARGIN,
            topMargin=TOP_MARGIN,
            bottomMargin=BOTTOM_MARGIN
        )

    # -----------------------------------------------------
    # COVER
    # -----------------------------------------------------

    def add_cover(self, title, subtitle="", description=""):

        block = self.components.cover_block(title, subtitle, description)
        self.story.extend(block)
        self.story.append(PageBreak())

    # -----------------------------------------------------
    # QUOTE
    # -----------------------------------------------------

    def add_quote(self, text):

        block = self.components.quote_block(text)
        self.story.extend(block)
        self.story.append(PageBreak())

    # -----------------------------------------------------
    # SECTION
    # -----------------------------------------------------

    def add_section(self, title, content):

        block = self.components.section_block(title, content)
        self.story.extend(block)
        self.story.append(PageBreak())

    # -----------------------------------------------------
    # INFO BOX
    # -----------------------------------------------------

    def add_info_box(self, title, content):

        block = self.components.info_box(title, content)
        self.story.extend(block)

    # -----------------------------------------------------
    # SAVE
    # -----------------------------------------------------

    def save(self, filename="NeuroMate.pdf"):

        output_file = os.path.join(self.output_path, filename)
        self.doc.build(self.story)

        os.rename(self.file_path, output_file)

        return output_file
