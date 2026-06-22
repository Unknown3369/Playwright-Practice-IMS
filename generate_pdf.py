"""
Helper script called by sales_invoice.py to generate a PDF from an HTML file.
Run as: python generate_pdf.py <html_file> <output_pdf>
"""
import sys
from playwright.sync_api import sync_playwright

def main():
    html_file = sys.argv[1]
    pdf_file  = sys.argv[2]

    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.set_content(html_content, wait_until="networkidle")
        page.wait_for_timeout(2000)
        page.pdf(path=pdf_file, format="A4", print_background=True)
        browser.close()

    print(f"PDF saved to {pdf_file}")

if __name__ == "__main__":
    main()
