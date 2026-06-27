# =========================================================
# NeuroMate PDF Generator - MAIN ENTRY POINT
# =========================================================

import os
from neuromate.pdf_engine import NeuroMatePDF
from neuromate.config import PAGE_SIZE

# =========================================================
# Project Paths
# =========================================================

ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(ROOT, "output")

# =========================================================
# Create Output Folder if not exists
# =========================================================

os.makedirs(OUTPUT_PATH, exist_ok=True)

# =========================================================
# MAIN EXECUTION
# =========================================================

def main():

    print("===================================")
    print(" NeuroMate PDF Generator Started")
    print("===================================")

    # Create PDF Engine instance
    pdf = NeuroMatePDF(output_path=OUTPUT_PATH)

    # Initialize document
    pdf.create_document()

    # -------------------------------
    # Cover Page
    # -------------------------------
    pdf.add_cover(
        title="NEUROMATE",
        subtitle="THE BLACK MIND",
        description="A Cinematic Franchise Bible"
    )

    # -------------------------------
    # Quote Page
    # -------------------------------
    pdf.add_quote(
        "The world is not a board... it is a battlefield of minds."
    )

    # -------------------------------
    # Executive Section
    # -------------------------------
    pdf.add_section(
        title="EXECUTIVE SUMMARY",
        content="""
NeuroMate is a dark sci-fi cinematic universe exploring the fusion between human consciousness and neural AI systems.
The story unfolds in a world where free will becomes a programmable illusion.
        """
    )

    # -------------------------------
    # World Building
    # -------------------------------
    pdf.add_section(
        title="WORLD BUILDING",
        content="""
The world operates as a layered simulation where every human decision is influenced by predictive neural algorithms with 99.4% accuracy.
        """
    )

    # -------------------------------
    # Save PDF
    # -------------------------------
    output_file = pdf.save("NeuroMate_Franchise_Bible.pdf")

    print("\n===================================")
    print(" PDF Generated Successfully!")
    print(" File:", output_file)
    print("===================================")


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    main()
