from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

website = 'https://www.irctc.co.in'

firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(firefox_options)

driver.maximize_window()

driver.get(website)

time.sleep(5)


from_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input'))
)

from_input.send_keys('NAGPUR - NGP (NAGPUR)')


from_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input'))
)

from_input.send_keys('MUMBAI CENTRAL - MMCT (MUMBAI)')

date_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input'))
)

date_field.send_keys(Keys.CONTROL + "a")
date_field.send_keys(Keys.DELETE)

date_field.send_keys('24/04/2024')


dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="journeyQuota"]'))
)
dropdown.click()

option_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "GENERAL")]'))
)
option_element.click()

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'train_Search'))
)
search_button.click()

train_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//strong[contains(text(), "CSMT DURONTO EX (12262)")]'))
)
train_element.click()

pre_avl_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "pre-avl")]//strong[contains(text(), "AC 3 Tier (3A)")]'))
)
pre_avl_element.click()

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "pre-avl") and contains(., "Mon, 29 Apr")]'))
)
element.click()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "train_Search") and contains(text(), "Book Now")]'))
)
button.click()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "ui-button-text") and contains(text(), "Yes")]'))
)
button.click()

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="userid"]'))
)
# from_input.click()

input_field.send_keys('RiteshBansod')


input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname="password"]'))
)
# from_input.click()

input_field.send_keys('42535162qQ')

time.sleep(15)

signin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button'))
)
signin_button.click()


passenger_name_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[1]/p-autocomplete/span/input'))
)
passenger_name_field.send_keys("alexander")


passenger_age_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[3]/div/app-passenger-input/div[5]/form/div/div[1]/div[4]/p-panel/div/div[2]/div/div[1]/div[2]/div/app-passenger/div/div[1]/span/div[2]/input'))
)
passenger_age_field.send_keys("25")


dropdown_gender = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="passengerGender"]'))
)

dropdown = Select(dropdown_gender)
dropdown.select_by_visible_text("Male")

dropdown_nation = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="passengerNationality"]'))
)

dropdown = Select(dropdown_nation)
dropdown.select_by_visible_text("India")

dropdown_pref = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="passengerBerthChoice"]'))
)

dropdown = Select(dropdown_pref)
dropdown.select_by_visible_text("Lower")

dropdown_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'select[formcontrolname="passengerFoodChoice"]'))
)

dropdown = Select(dropdown_menu)
dropdown.select_by_visible_text("No Food")


# add_element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "zeroPadding")]/a[@tabindex="0"]/span[contains(@class, "prenext")][1]'))
# )
# add_element.click()



label_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//label[contains(text(), "Consider for Auto Upgradation")]'))
)


label_element.click()


