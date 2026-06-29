# =========================================================
# NeuroMate PDF Engine V2
# Core Engine
# =========================================================

import os

import arabic_reshaper
from bidi.algorithm import get_display

from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate

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
# Arabic Support
# =========================================================

def fix_text(text):

    if text is None:
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

        os.makedirs(
            self.output_path,
            exist_ok=True
        )

        # Register Fonts
        self.fonts = FontManager()
        self.fonts.register()

        self.styles = NeuroMateStyles()

        self.components = NeuroMateComponents(
            self.styles
        )

        self.layouts = NeuroMateLayouts(
            self.components
        )

        self.story = []

        self.doc = None
        self.file_path = None

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
    # ADD COVER
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
    # ADD QUOTE
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
    # ADD SECTION
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
    # ADD INFO BOX
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
    # HELPERS
    # =====================================================

    def logo_path(self):

        return os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "assets",
            "images",
            "logo.png"
        )

    def cover_path(self):

        return os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "assets",
            "images",
            "cover_bg.jpg"
        )
            # =====================================================
    # DRAW STANDARD PAGE
    # =====================================================
def draw_page(self, canvas, doc):

    width, height = PAGE_SIZE

    canvas.saveState()

    # =====================================================
    # Background
    # =====================================================

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

    # =====================================================
    # Small Logo
    # =====================================================

    logo = self.logo_path()

    if os.path.exists(logo):

        try:

            canvas.drawImage(
                ImageReader(logo),
                LEFT_MARGIN,
                height - 42,
                width=22,
                height=22,
                preserveAspectRatio=True,
                mask="auto"
            )

        except:
            pass

    # =====================================================
    # Header
    # =====================================================

    canvas.setFillColor(BLUE)

    canvas.setFont(
        FONT_BOLD,
        11
    )

    canvas.drawString(
        LEFT_MARGIN + 32,
        height - 28,
        "NEUROMATE"
    )

    # =====================================================
    # Divider
    # =====================================================

    canvas.setStrokeColor(SILVER)

    canvas.setLineWidth(.4)

    canvas.line(
        LEFT_MARGIN,
        height - 36,
        width - RIGHT_MARGIN,
        height - 36
    )

    # =====================================================
    # Footer
    # =====================================================

    canvas.setFillColor(SILVER)

    canvas.setFont(
        FONT_REGULAR,
        9
    )

    canvas.drawRightString(
        width - RIGHT_MARGIN,
        20,
        f"Page {canvas.getPageNumber()}"
    )

    canvas.restoreState()


    # =====================================================
    # DRAW COVER PAGE
    # =====================================================

   def draw_cover(self, canvas, doc):

    width, height = PAGE_SIZE

    canvas.saveState()

    bg = self.cover_path()

    print("=" * 50)
    print("COVER BACKGROUND")
    print(bg)
    print("Exists:", os.path.exists(bg))

    if os.path.exists(bg):

        try:

            img = ImageReader(bg)

            print("Image Loaded Successfully")

            canvas.drawImage(
                img,
                0,
                0,
                width=width,
                height=height,
                preserveAspectRatio=False,
                mask="auto"
            )

        except Exception as e:

            print("IMAGE ERROR:", e)

            canvas.setFillColor(HexColor("#05070A"))
            canvas.rect(
                0,
                0,
                width,
                height,
                fill=1,
                stroke=0
            )

    else:

        print("Background NOT FOUND")

        canvas.setFillColor(HexColor("#05070A"))
        canvas.rect(
            0,
            0,
            width,
            height,
            fill=1,
            stroke=0
        )

    canvas.restoreState()