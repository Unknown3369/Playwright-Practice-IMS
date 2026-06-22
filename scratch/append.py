code = """      # Wait for the application to trigger print()
      try:
          self.page.wait_for_function("window.printCalled === true", timeout=15000)
          print("Print dialog intercepted successfully!")
          last_print = self.page.evaluate("window.lastPrint")
          
          if last_print == 'iframe':
              invoice_html = self.page.evaluate("window.printIframe.contentDocument.documentElement.outerHTML")
          else:
              invoice_html = self.page.content()

          # Ensure output directory exists
          import os
          from datetime import datetime
          os.makedirs("invoices", exist_ok=True)
          timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
          pdf_path = f"invoices/sales_invoice_{timestamp}.pdf"

          # Use a headless browser to generate the PDF from the captured HTML
          from playwright.sync_api import sync_playwright
          with sync_playwright() as p:
              headless_browser = p.chromium.launch(headless=True)
              headless_context = headless_browser.new_context()
              headless_page = headless_context.new_page()
              
              headless_page.set_content(invoice_html, wait_until="networkidle")
              headless_page.wait_for_timeout(2000)
              
              headless_page.pdf(path=pdf_path, format="A4", print_background=True)
              print(f"Invoice successfully saved to {pdf_path}")
              headless_browser.close()

      except Exception as e:
          print("Print was not triggered or error generating PDF:", e)
"""
with open("Pages/Transactions/sales_invoice.py", "a", encoding="utf-8") as f:
    f.write(code)
