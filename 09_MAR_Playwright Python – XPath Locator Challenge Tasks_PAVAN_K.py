from playwright.sync_api import sync_playwright

def Task1TO9():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Task 1 – Login Using XPath
        page.goto("https://opensource-demo.orangehrmlive.com")

        page.locator("xpath=//input[@name='username']").fill("Admin")
        page.locator("xpath=//input[@name='password']").fill("admin123")
        page.locator("xpath=//button[@type='submit']").click()

        page.wait_for_timeout(3000)

        # Task 2 – XPath Using text()
        page.locator("xpath=//span[text()='Admin']").click()

        page.wait_for_timeout(2000)

        # Task 3 – XPath Using contains()
        search_box = page.locator("//input[contains(@class,'oxd-input')]").nth(1)
        search_box.fill("Admin")

        page.wait_for_timeout(2000)

        # Task 4 – XPath Using starts-with()
        page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()

        page.wait_for_timeout(2000)

        # Task 5 – Parent Child Relationship
        page.locator("xpath=//span[text()='Admin']/parent::a").click()

        page.wait_for_timeout(2000)

        # Task 6 – Following XPath
        page.locator("xpath=//span[text()='Admin']/following::span[text()='PIM'][1]").click()

        page.wait_for_timeout(2000)

        # Task 7 – Preceding XPath
        element = page.locator("xpath=//span[text()='PIM']/preceding::span[1]")
        print("Element before PIM:", element.text_content())

        # Task 8 – XPath with Index
        page.locator("xpath=(//ul[@class='oxd-main-menu']/li)[2]").click()

        page.wait_for_timeout(2000)

        # Task 9 – Dynamic XPath Challenge
        page.locator("xpath=//p[contains(@class,'oxd-userdropdown-name')]").click()

        page.wait_for_timeout(2000)


def Task_TEN():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login Using XPath
        page.goto("https://opensource-demo.orangehrmlive.com")
        # Task 10 – Advanced XPath Challenge

        # Login again
        page.locator("xpath=//input[@name='username']").fill("Admin")
        page.locator("xpath=//input[@name='password']").fill("admin123")
        page.locator("xpath=//button[@type='submit']").click()

        page.wait_for_timeout(3000)

        # Navigate to Admin
        page.locator("xpath=//span[text()='Admin']").click()

        page.wait_for_timeout(2000)

        # Click Add button
        page.locator("xpath=//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()

        page.wait_for_timeout(3000)

        # Select User Role dropdown
        page.locator(
            "xpath=//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()

        # Choose Admin
        page.locator("xpath=//div[@role='listbox']//span[text()='Admin']").click()

        # Employee name
        page.locator("xpath=//input[contains(@placeholder,'Type')]").fill("Paul")

        # Status dropdown
        page.locator("xpath=//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]").click()
        page.locator("xpath=//span[text()='Enabled']").click()

        # Username
        page.locator("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").fill("TestUser123")

        # Password
        page.locator("xpath=(//input[@type='password'])[1]").fill("Test@12345")

        # Confirm Password
        page.locator("xpath=(//input[@type='password'])[2]").fill("Test@12345")

        # Save button
        page.locator("xpath=//button[contains(@class,'oxd-button') and text()=' Save ']").click()

        page.wait_for_timeout(5000)

        browser.close()

Task1TO9()
Task_TEN()