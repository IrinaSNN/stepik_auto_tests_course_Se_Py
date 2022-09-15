from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(" http://SunInJuly.github.io/execute_script.html")
    
    x_element = browser.find_element(By.ID, "input_value")
    #x = x_element.text
    y = calc(x_element.text)
    
    input1 = browser.find_element(By.ID, "answer")
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100)")
    input1.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    
    #button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла