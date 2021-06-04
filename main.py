from selenium import webdriver
import time

BROWSER = webdriver.Chrome('./chromedriver.exe')
LOGIN = '123'
PASSWORD = '123'
ERROR_LOGIN = 'Неверный логин или пароль. Если не можете войти, восстановите доступ.'

def LoginValue(log, pas):
    BROWSER.find_element_by_id('loginByLogin').send_keys(log)
    BROWSER.find_element_by_id('password').send_keys(pas)
    return 0

def ErrorMessage (error_message):
    time.sleep(1) # задерка, чтобы попап или надпись успели появиться
    result = BROWSER.find_element_by_tag_name('p').text
    print(result)
    if result == error_message:
        return 'login and password wrong. Test case passed'
    else:
        return 'Login and password right. Test case failed'


BROWSER.get('https://online.sberbank.ru/#/')
button = BROWSER.find_element_by_xpath("//button[text()='Войти']")
LoginValue(LOGIN, PASSWORD)
button.click()
result = ErrorMessage(ERROR_LOGIN)
BROWSER.quit()
print(result)
