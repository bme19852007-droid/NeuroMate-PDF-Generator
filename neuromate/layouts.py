# =========================================================
# NeuroMate Layout System
# Page Composition Layer
# =========================================================

from reportlab.platypus import PageBreak


class NeuroMateLayouts:

    def __init__(self, components):
        self.components = components

    # -----------------------------------------------------
    # Cover Page
    # -----------------------------------------------------

    def cover(self, title, subtitle="", description=""):

        elements = []

        elements.extend(
            self.components.cover_block(
                title,
                subtitle,
                description
            )
        )

        elements.append(PageBreak())

        return elements

    # -----------------------------------------------------
    # Quote Page
    # -----------------------------------------------------

    def quote(self, text):

        elements = []

        elements.extend(
            self.components.quote_block(text)
        )

        elements.append(PageBreak())

        return elements

    # -----------------------------------------------------
    # Standard Section
    # -----------------------------------------------------

    def section(self, title, content):

        elements = []

        elements.extend(
            self.components.section_block(
                title,
                content
            )
        )

        elements.append(PageBreak())

        return elements

    # -----------------------------------------------------
    # Info Card
    # -----------------------------------------------------

    def info(self, title, content):

        return self.components.info_box(
            title,
            content
        )
