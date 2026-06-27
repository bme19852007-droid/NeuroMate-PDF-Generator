# =========================================================
# NeuroMate Components System
# Cinematic Layout Blocks
# =========================================================

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

from neuromate.config import BLUE, SILVER, WHITE
from neuromate.pdf_engine import fix_text


# =========================================================
# COMPONENT FACTORY
# =========================================================

class NeuroMateComponents:

    def __init__(self, styles):
        self.styles = styles

    # -----------------------------------------------------
    # COVER BLOCK (Reusable)
    # -----------------------------------------------------
    def cover_block(self, title, subtitle="", description=""):

        elements = []

        title_style = self.styles.title()
        subtitle_style = self.styles.subtitle()
        body_style = self.styles.body()

        elements.append(Spacer(1, 120))

        elements.append(
            Paragraph(fix_text(title), title_style)
        )

        if subtitle:
            elements.append(
                Paragraph(fix_text(subtitle), subtitle_style)
            )

        if description:
            elements.append(
                Paragraph(fix_text(description), body_style)
            )

        elements.append(Spacer(1, 30))

        return elements

    # -----------------------------------------------------
    # QUOTE BLOCK (Cinematic Quote)
    # -----------------------------------------------------
    def quote_block(self, text):

        quote_style = self.styles.quote()

        return [
            Spacer(1, 180),
            Paragraph(f"“{fix_text(text)}”", quote_style),
            Spacer(1, 30)
        ]

    # -----------------------------------------------------
    # INFO BOX (Tech Noir Card)
    # -----------------------------------------------------
    def info_box(self, title, content):

        title_style = self.styles.section_title()
        body_style = self.styles.body()

        table_data = [
            [Paragraph(fix_text(title), title_style)],
            [Spacer(1, 5)],
            [Paragraph(fix_text(content), body_style)]
        ]

        table = Table(table_data, colWidths=450)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0A0A0A")),
            ("BOX", (0, 0), (-1, -1), 1, SILVER),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]))

        return [Spacer(1, 15), table, Spacer(1, 15)]

    # -----------------------------------------------------
    # SECTION BLOCK
    # -----------------------------------------------------
    def section_block(self, title, content):

        elements = []

        title_style = self.styles.section_title()
        body_style = self.styles.body()

        elements.append(
            Paragraph(fix_text(title), title_style)
        )

        elements.append(Spacer(1, 10))

        for line in content.split("\n"):
            if line.strip():
                elements.append(
                    Paragraph(fix_text(line), body_style)
                )
                elements.append(Spacer(1, 8))

        elements.append(Spacer(1, 20))

        return elements
