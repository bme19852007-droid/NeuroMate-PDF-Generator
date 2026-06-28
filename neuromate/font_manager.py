# =========================================================
# NeuroMate Font Manager
# Handles font registration and fallback
# =========================================================

import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class FontManager:

    def __init__(self, assets_path="assets/fonts"):

        self.assets_path = assets_path

        self.font_regular = "Helvetica"
        self.font_bold = "Helvetica-Bold"
        self.font_semibold = "Helvetica-Bold"

    # -----------------------------------------------------
    # Register Fonts
    # -----------------------------------------------------

    def register(self):

        regular = os.path.join(self.assets_path, "Cairo-Regular.ttf")
        bold = os.path.join(self.assets_path, "Cairo-Bold.ttf")
        semibold = os.path.join(self.assets_path, "Cairo-SemiBold.ttf")

        if (
            os.path.exists(regular)
            and os.path.exists(bold)
            and os.path.exists(semibold)
        ):

            pdfmetrics.registerFont(TTFont("Cairo", regular))
            pdfmetrics.registerFont(TTFont("Cairo-Bold", bold))
            pdfmetrics.registerFont(TTFont("Cairo-SemiBold", semibold))

            self.font_regular = "Cairo"
            self.font_bold = "Cairo-Bold"
            self.font_semibold = "Cairo-SemiBold"

            print("✔ Cairo fonts loaded")

        else:

            print("⚠ Cairo fonts not found -> Using Helvetica")

    # -----------------------------------------------------
    # Getters
    # -----------------------------------------------------

    def regular(self):
        return self.font_regular

    def bold(self):
        return self.font_bold

    def semibold(self):
        return self.font_semibold