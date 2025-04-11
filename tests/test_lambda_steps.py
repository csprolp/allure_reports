import allure
from selene import browser, have, by, be


def test_dynamic_steps():
    with allure.step("Открыть гит"):
        browser.open("https://github.com")
        browser.driver.fullscreen_window()
    with allure.step('Найти в поиске проект'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').send_keys("eroshenkoam/allure-example").press_enter()
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step('Нажать на таб issue'):
        browser.element("#issues-tab").click()
    with allure.step('Проверить наличие конкретного issue'):
        browser.element("[data-testid='list-row-repo-name-and-number']").should(have.text('#95'))


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_text('Привет от 27го потока QA.GURU!!!')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').send_keys(repo)
    browser.element('#query-builder-test').submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с текстом {value}")
def should_see_issue_with_text(value):
    browser.element(by.link_text(value)).should(be.visible)