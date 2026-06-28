# =========================================================
# NeuroMate Components System
# Cinematic Layout Blocks
# =========================================================

from reportlab.platypus import (
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from reportlab.lib import colors

from neuromate.config import (
    BLUE,
    SILVER,
    WHITE,
)

from neuromate.utils import fix_text


# =========================================================
# COMPONENT FACTORY
# =========================================================

class NeuroMateComponents:

    def __init__(self, styles):
        self.styles = styles

    # -----------------------------------------------------
    # COVER BLOCK (Cinematic Cover)
    # -----------------------------------------------------

    def cover_block(
        self,
        title,
        subtitle="",
        description=""
    ):

        elements = []

        title_style = self.styles.title()
        subtitle_style = self.styles.subtitle()
        body_style = self.styles.body()

        # Space from top
        elements.append(Spacer(1, 220))

        # Main Title
        elements.append(
            Paragraph(
                f"<font size='34'><b>{fix_text(title)}</b></font>",
                title_style,
            )
        )

        elements.append(Spacer(1, 18))

        # Subtitle
        if subtitle:

            elements.append(
                Paragraph(
                    f"<font size='18'>{fix_text(subtitle)}</font>",
                    subtitle_style,
                )
            )

        elements.append(Spacer(1, 28))

        # Description
        if description:

            elements.append(
                Paragraph(
                    fix_text(description),
                    body_style,
                )
            )

        elements.append(Spacer(1, 220))

        return elements

    # -----------------------------------------------------
    # QUOTE BLOCK
    # -----------------------------------------------------

    def quote_block(self, text):

        quote_style = self.styles.quote()

        return [

            Spacer(1, 180),

            Paragraph(
                f"“{fix_text(text)}”",
                quote_style
            ),

            Spacer(1, 40),

        ]

    # -----------------------------------------------------
    # INFO BOX
    # -----------------------------------------------------

    def info_box(
        self,
        title,
        content
    ):

        title_style = self.styles.section_title()
        body_style = self.styles.body()

        table_data = [

            [
                Paragraph(
                    fix_text(title),
                    title_style
                )
            ],

            [Spacer(1, 6)],

            [
                Paragraph(
                    fix_text(content),
                    body_style
                )
            ],

        ]

        table = Table(
            table_data,
            colWidths=450
        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor("#0B0F18"),
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    1,
                    SILVER,
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    16,
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    16,
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    12,
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    12,
                ),

            ])

        )

        return [

            Spacer(1, 20),

            table,

            Spacer(1, 20),

        ]

    # -----------------------------------------------------
    # STANDARD SECTION
    # -----------------------------------------------------

    def section_block(
        self,
        title,
        content
    ):

        elements = []

        title_style = self.styles.section_title()
        body_style = self.styles.body()

        elements.append(

            Paragraph(
                fix_text(title),
                title_style
            )

        )

        elements.append(
            Spacer(1, 12)
        )

        for line in content.split("\n"):

            line = line.strip()

            if not line:
                continue

            elements.append(

                Paragraph(
                    fix_text(line),
                    body_style
                )

            )

            elements.append(
                Spacer(1, 8)
            )

        elements.append(
            Spacer(1, 20)
        )

        return elements