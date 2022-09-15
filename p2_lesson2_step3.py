from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/selects1.html")
    
    x1_element = browser.find_element(By.ID, "num1").text
    x2_element = browser.find_element(By.ID, "num2").text
    print (x1_element, x2_element)
    y = int(x1_element) + int(x2_element)
    
    sum1 = Select(browser.find_element(By.ID, "dropdown"))
    sum1.select_by_visible_text(str(y))
    #input1.send_keys(x1_element + x2_element)
        
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла