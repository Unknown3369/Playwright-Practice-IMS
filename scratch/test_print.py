from playwright.sync_api import sync_playwright
import time
import random

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://automation.variantqa.himshang.com.np/#/login")
        page.locator("input[name='username']").fill("testuser")
        page.locator("input[name='password']").fill("Test@1234")
        page.locator("button[type='submit']").click()
        page.wait_for_url("**/dashboard")
        
        page.goto("https://automation.variantqa.himshang.com.np/#/pages/transaction/sales/add-sales-invoice")
        
        ref_no = "REF-" + str(random.randint(1000,9999))
        page.locator("input[formcontrolname='refBillNo']").fill(ref_no)
        
        page.locator("input#party").fill("C")
        page.wait_for_timeout(1000)
        page.locator("input#party").press("Enter")
        page.locator("td:has-text('C')").first.click()
        
        page.locator("input[id^='itemCode']").first.fill("1.360")
        page.locator("input[id^='itemCode']").first.press("Enter")
        page.locator("input[id^='quantity']").first.fill("5")
        
        # Override print on main window
        page.evaluate("window.print = function() { window.lastPrint = 'main'; window.printCalled = true; }")
        
        # Override print on all iframes periodically
        page.evaluate("""
            setInterval(() => {
                document.querySelectorAll('iframe').forEach(f => {
                    try {
                        if (!f.contentWindow.printOverridden) {
                            f.contentWindow.print = function() { window.lastPrint = 'iframe'; window.printCalled = true; };
                            f.contentWindow.printOverridden = true;
                        }
                    } catch(e) {}
                });
            }, 100);
        """)

        # save
        page.locator("//button[normalize-space()='SAVE [End]']").click(force=True)
        page.locator("//button[normalize-space()='Balance Amount']").click(force=True)
        page.locator("//button[normalize-space()='ADD']").click(force=True)
        
        page.locator("//button[normalize-space()='Final Save']").click(force=True)
        
        try:
            page.wait_for_function("window.printCalled === true", timeout=15000)
            print("PRINT WAS CALLED!")
            last_print = page.evaluate("window.lastPrint")
            print("Called from:", last_print)
            
            if last_print == 'iframe':
                 # get iframe content
                 iframe_html = page.evaluate("""() => {
                     let html = '';
                     document.querySelectorAll('iframe').forEach(f => {
                         if (f.contentDocument && f.contentDocument.body.innerHTML.length > 10) {
                             html = f.contentDocument.documentElement.outerHTML;
                         }
                     });
                     return html;
                 }""")
                 with open("scratch/print_content.html", "w", encoding="utf-8") as f:
                     f.write(iframe_html)
            else:
                 with open("scratch/print_content.html", "w", encoding="utf-8") as f:
                     f.write(page.content())
                     
        except Exception as e:
            print("Print not called or error:", e)
        
        time.sleep(2)
        browser.close()

if __name__ == '__main__':
    run()
