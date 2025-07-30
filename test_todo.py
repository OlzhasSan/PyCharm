from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    time.sleep(2)
    page.get_by_placeholder("What needs to be done?").click()
    time.sleep(2)
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    time.sleep(2)
    page.get_by_placeholder("What needs to be done?").press("Enter")
    time.sleep(2)
    page.get_by_role("checkbox", name="Toggle Todo").check()
    time.sleep(2)

    # ---------------------
    context.close()
    browser.close()