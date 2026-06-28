# =========================================================
# NeuroMate PDF Engine V3
# =========================================================

import os

import arabic_reshaper
from bidi.algorithm import get_display

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.colors import HexColor

from neuromate.config import (
    PAGE_SIZE,
    LEFT_MARGIN,
    RIGHT_MARGIN,
    TOP_MARGIN,
    BOTTOM_MARGIN,
    FONT_REGULAR,
    FONT_BOLD,
    BLUE,
    SILVER,
)

from neuromate.styles import NeuroMateStyles
from neuromate.font_manager import FontManager
from neuromate.components import NeuroMateComponents
from neuromate.layouts import NeuroMateLayouts


# =========================================================
# Arabic Text Support
# =========================================================

def fix_text(text):

    if not text:
        return ""

    try:
        reshaped = arabic_reshaper.reshape(str(text))
        return get_display(reshaped)
    except Exception:
        return str(text)


# =========================================================
# PDF ENGINE
# =========================================================

class NeuroMatePDF:

    def __init__(self, output_path="output"):

        self.output_path = output_path

        os.makedirs(self.output_path, exist_ok=True)

        self.file_path = None
        self.doc = None

        self.story = []

        # Styles

        self.styles = NeuroMateStyles()

        # Components

        self.components = NeuroMateComponents(
            self.styles
        )

        # Layout System

        self.layouts = NeuroMateLayouts(
            self.components
        )

    # =====================================================
    # CREATE DOCUMENT
    # =====================================================

    def create_document(self):

        self.file_path = os.path.join(
            self.output_path,
            "temp.pdf"
        )

        self.doc = SimpleDocTemplate(
            self.file_path,
            pagesize=PAGE_SIZE,
            leftMargin=LEFT_MARGIN,
            rightMargin=RIGHT_MARGIN,
            topMargin=TOP_MARGIN,
            bottomMargin=BOTTOM_MARGIN,
        )    
    # =====================================================
    # COVER PAGE
    # =====================================================

    def add_cover(
        self,
        title,
        subtitle="",
        description=""
    ):

        self.story.extend(

            self.layouts.cover(
                title,
                subtitle,
                description
            )

        )

    # =====================================================
    # QUOTE PAGE
    # =====================================================

    def add_quote(
        self,
        text
    ):

        self.story.extend(

            self.layouts.quote(
                text
            )

        )

    # =====================================================
    # SECTION PAGE
    # =====================================================

    def add_section(
        self,
        title,
        content
    ):

        self.story.extend(

            self.layouts.section(
                title,
                content
            )

        )

    # =====================================================
    # INFO BOX
    # =====================================================

    def add_info_box(
        self,
        title,
        content
    ):

        self.story.extend(

            self.layouts.info(
                title,
                content
            )

        )

    # =====================================================
    # PAGE TEMPLATE
    # =====================================================

    def draw_page(
        self,
        canvas,
        doc
    ):
# =====================================================
# COVER PAGE
# =====================================================

def draw_cover(self, canvas, doc):

    from reportlab.lib.utils import ImageReader

    width, height = PAGE_SIZE

    canvas.saveState()

    bg = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "assets",
        "images",
        "cover_bg.jpg"
    )

    if os.path.exists(bg):

        canvas.drawImage(
            ImageReader(bg),
            0,
            0,
            width=width,
            height=height,
            preserveAspectRatio=False,
            mask="auto"
        )

    canvas.restoreState()
        width, height = PAGE_SIZE

        canvas.saveState()
        # =====================================================
# LOGO
# =====================================================

logo_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "assets",
    "images",
    "logo.png"
)

logo_exists = os.path.exists(logo_path)

        # Background

        canvas.setFillColor(
            HexColor("#0D0F14")
        )

        canvas.rect(
            0,
            0,
            width,
            height,
            fill=1,
            stroke=0
        )

        # Header

        # =====================================================
# HEADER LOGO
# =====================================================

if logo_exists:

    try:

        canvas.drawImage(
            logo_path,
            LEFT_MARGIN,
            height - 45,
            width=90,
            preserveAspectRatio=True,
            mask="auto",
        )

        title_x = LEFT_MARGIN + 100

    except Exception:

        title_x = LEFT_MARGIN

else:

    title_x = LEFT_MARGIN


canvas.setFont(
    FONT_BOLD,
    11
)

canvas.setFillColor(BLUE)

canvas.drawString(
    title_x,
    height - 28,
    "NEUROMATE"
)

        # Separator

        canvas.setStrokeColor(
            SILVER
        )

        canvas.setLineWidth(
            0.6
        )

        canvas.line(
            LEFT_MARGIN,
            height - 36,
            width - RIGHT_MARGIN,
            height - 36
        )

        # Footer

        canvas.setFont(
            FONT_REGULAR,
            9
        )

        canvas.setFillColor(
            SILVER
        )

        canvas.drawRightString(
            width - RIGHT_MARGIN,
            22,
            f"Page {canvas.getPageNumber()}"
        )

        canvas.restoreState()
    # =====================================================
    # SAVE PDF
    # =====================================================

    def save(self, filename="NeuroMate.pdf"):

        if self.doc is None:
            self.create_document()

        output_file = os.path.join(
            self.output_path,
            filename
        )

       self.doc.build(
    self.story,
    onFirstPage=self.draw_cover,
    onLaterPages=self.draw_page,
)

        if os.path.exists(output_file):
            os.remove(output_file)

        os.replace(
            self.file_path,
            output_file
        )

        return output_file
