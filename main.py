from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telebot
from telebot import types
import time

# Import -----------------------------------------

s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36.')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('headless')
driver = webdriver.Chrome(service=s, options=options)


# WebDriver Settings -------------------------------
def get_screen():
    driver.get('http://abiturient.gsu.by/?page_id=291&lang=ru')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )
    except Exception as ex:
        print('Page not found')

    try:
        link_to_login = driver.find_elements(By.TAG_NAME, 'a')
        for name in link_to_login:
            if name.text == 'Кабинет абитуриента':
                url_1 = name.get_attribute('href')
                driver.get(url_1)
                break
    except Exception as ex:
        print('Login link not found')

    try:
        inputs_login = driver.find_elements(By.TAG_NAME, 'input')
        for name in inputs_login:
            if name.accessible_name == 'Логин':
                name.send_keys('d170105')
                print('Логин введен')
            if name.accessible_name == 'Пароль':
                name.send_keys('522454zzz')
                print('Пароль введен')
    except Exception as ex:
        print('Inputs to login/password not found')

    print('Данные введены')

    try:
        button_to_room = driver.find_elements(By.TAG_NAME, 'button')
        for name in button_to_room:
            if name.accessible_name == 'Войти':
                name.click()
                print('Вход в ЛК...')
                break
    except Exception as ex:
        print('Кнопка входа не найдена')

    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.TAG_NAME, "a"))
    #     )
    # except Exception as ex:
    #     print('Page not found')
    # print(element)

    time.sleep(10)

    # print(element.get_attribute('href'))

    # competition_button = driver.find_elements(By.TAG_NAME, 'li')
    # try:
    #     for name in competition_button:
    #         if 'Текущий конкурс' in name.text:
    #             name.click()
    #             print('Переход на страницу "Текущий конкурс"...')
    # except Exception as ex:
    #     print('Page "Текущий конкурс" not found')
    try:
        driver.get('https://abitur.gsu.by/personal/konkurs')
        time.sleep(3)
    except Exception as ex:
        print('Konkurs not found')

    # competition_button = driver.find_elements(By.TAG_NAME, 'a')
    # try:
    #     for name in competition_button:
    #         print(name.get_attribute('href'))
    #         # if 'Текущий конкурс' in name.text:
    #         #     name.click()
    #         #     print('Переход на страницу "Текущий конкурс"...')
    # except Exception as ex:
    #     print('Page "Текущий конкурс" not found')

    try:
        list_of_options = driver.find_elements(By.TAG_NAME, 'option')
        for value in list_of_options:
            if value.text == 'платная':
                value.click()
                print('Платная форма обучения выбрана')
                break
    except Exception as ex:
        print('Select not found')

    try:
        list_of_options = driver.find_elements(By.TAG_NAME, 'option')
        for option in list_of_options:
            if 'Математики и технологий программирования' in option.text:
                option.click()
                print('Факультет выбран')
                break
    except Exception as ex:
        print('Select not found')

    time.sleep(5)

    try:
        all_buttons = driver.find_elements(By.TAG_NAME, 'button')
        for button in all_buttons:
            if button.text == 'Получить данные':
                button.click()
                print('Получение данных')
                break
    except Exception as ex:
        print('Button not found')

    time.sleep(10)

    try:
        screen_table = driver.find_element(By.CSS_SELECTOR, '#current-konkurs-container > table')
        # for div in screen_tebles:
        #     if div.id == 'result-data':
        #         div.screenshot('board.png')
        #         print('Скрин готов')
        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)
        screen_table.screenshot('screen_m.png')
        print('Скриншот готов')
    except Exception as ex:
        print('Board not found')


# Math -------------------------------------------

    try:
        list_of_options = driver.find_elements(By.TAG_NAME, 'option')
        for option in list_of_options:
            if 'Физики и информационных технологий' in option.text:
                option.click()
                print('Факультет выбран')
                break
    except Exception as ex:
        print('Select not found')

    time.sleep(5)

    try:
        all_buttons = driver.find_elements(By.TAG_NAME, 'button')
        for button in all_buttons:
            if button.text == 'Получить данные':
                button.click()
                print('Получение данных')
                break
    except Exception as ex:
        print('Button not found')

    time.sleep(10)

    try:
        screen_table = driver.find_element(By.CSS_SELECTOR, '#current-konkurs-container > table')
        # for div in screen_tebles:
        #     if div.id == 'result-data':
        #         div.screenshot('board.png')
        #         print('Скрин готов')
        driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)
        screen_table.screenshot('screen_p.png')
        print('Скриншот готов')
    except Exception as ex:
        print('Board not found')

# Physics


bot = telebot.TeleBot('TOKEN')

try:
    @bot.message_handler(content_types=['text'])
    def get_start_message(message):
        if message.text == "/start":
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
            keyboard.add(key_yes)
            key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_no)
            bot.send_message(message.from_user.id, text='Привет, нужны балы ГГУ?', reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":
            bot.send_message(call.message.chat.id, 'Выполняется...')
            get_screen()
            img_1 = open('screen_m.png', 'rb')
            img_2= open('screen_p.png', 'rb')
            bot.send_message(call.message.chat.id, 'Математический')
            bot.send_photo(call.message.chat.id, img_1)
            bot.send_message(call.message.chat.id, 'Физический')
            bot.send_photo(call.message.chat.id, img_2)
            print('Скрин отправлен')
        elif call.data == "no":
            bot.send_message(call.message.chat.id, 'Пошел пить чай...')



except Exception as ex:
    print('Error send message')


    def error_message(message):
        bot.send_message(message.from_user.id, text='Упс... Ошибка. Скоро вернусь :)')

bot.polling(none_stop=True, interval=0)
