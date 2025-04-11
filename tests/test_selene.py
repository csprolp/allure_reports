from selene import browser, have,  by


def test_clear_selene():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys("eroshenkoam/allure-example").press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element("[data-testid='list-row-repo-name-and-number']").should(have.text('#95'))