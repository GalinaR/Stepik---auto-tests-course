from selenium import webdriver
import time
import os 

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Galina")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Ramaniuk")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("qwerty@we.ru")
    file = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    