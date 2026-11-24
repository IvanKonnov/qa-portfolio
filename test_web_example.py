from playwright.sync_api import Page, expect

def test_example_page_title(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")

def test_example_heading_and_link(page: Page):
    page.goto("https://example.com")
    expect(page.locator("p").first).to_contain_text("This domain is for use in documentation examples without needing permission. This is not a service; avoid relying on it for testing and monitoring purposes.")
    expect(page.locator("a")).to_have_attribute("href", "https://iana.org/help/example-domains")
