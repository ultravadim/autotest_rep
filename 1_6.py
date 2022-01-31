from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# ссылка на форму регистрации
link = "http://suninjuly.github.io/registration2.html"

# названия полей для заполнения
# если обязательные поля для теста поменяются, можно будет здесь добавить/удалить
fields_name = ['first', 'second', 'third']

try:
    # объявляем веб-драйвер
    browser = webdriver.Chrome()
    # переходим по ссылке в браузере
    browser.get(link)

    # циклом перебираем названия полей и заполняем их
    for field_name in fields_name:
        element = browser.find_element(By.CSS_SELECTOR, f".{field_name}[required]")
        element.send_keys('test')

    # ищем кнопку, кликаем.
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    # ждем открытие страницы
    sleep(1)

    # грабим текст со страницы
    test_text = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = test_text.text

    # проверяем результат
    assert "Congratulations! You have successfully registered!" == welcome_text

# независимо от успешности выполнения try выполняем действия по закрытию браузера
finally:
    sleep(10)

    browser.quit()