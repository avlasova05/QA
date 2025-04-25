from playwright.sync_api import Page, expect

def test_locator_role(page:Page):
    page.goto("https://www.litres.ru/", wait_until="domcontentloaded")
    #page.locator("xpath=//*[@id='artsSliderTitle-:rq:']/a/span")
    page.get_by_role("link", name="Хиты, проверенные временем").click()
    expect(page).to_have_title("Хиты, проверенные временем – подборка книг – Литрес")
    page.get_by_role("button", name="Найти").click()#кнопка по какому то типу
    expect(page.get_by_text("стивен кинг")).to_be_visible()#ожидается что увидим такой текст

def test_locator_placeholder(page:Page):
    page.goto("https://www.litres.ru/", wait_until="domcontentloaded")
    page.get_by_placeholder("Искать на Литрес").fill("игра престолов") #передача значения в поле
    page.keyboard.press("Enter") #нажатие enter
    expect(page.get_by_text("Результаты поиска «игра престолов»")).to_be_visible()

def test_locator_datatestid(page:Page): #удобно для авто тестирования
    page.goto("https://www.litres.ru/", wait_until="domcontentloaded" )
    page.get_by_test_id("user-button").click()
    expect(page.get_by_text("Введите почту или логин")).to_be_visible()
    page.goto("https://www.litres.ru/", wait_until="domcontentloaded" )
    page.get_by_test_id("header-catalog-button").click()
    expect(page.get_by_text("Бесплатные книги")).to_be_visible()

def test_locator_alt(page:Page):
    page.goto("https://www.litres.ru/", wait_until="domcontentloaded")
    page.get_by_role("link", name="Хиты, проверенные временем").click()
    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_url("https://www.litres.ru/")

def test_locator_xpath(page:Page):
    page.goto("https://www.litres.ru/", wait_until="domcontentloaded")
    expect(page.locator("xpath=//a[@title='YouTube']")).to_be_visible()