"""Export index.html to a 15-page PDF.  Usage: pip install playwright && playwright install chromium && python export_pdf.py"""
from pathlib import Path
from playwright.sync_api import sync_playwright

here = Path(__file__).parent.resolve()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.emulate_media(media="print")
    pg.goto((here / "index.html").as_uri())
    pg.wait_for_timeout(1500)
    pg.pdf(path=str(here / "Prompt_Engineering_Basics_Notebook.pdf"), width="1280px", height="720px", print_background=True)
    b.close()
print("Saved Prompt_Engineering_Basics_Notebook.pdf")
