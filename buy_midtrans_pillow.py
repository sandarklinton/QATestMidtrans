import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)

driver.get('https://demo.midtrans.com/')

driver.find_element_by_css_selector('.btn.buy').click()
driver.find_element_by_class_name('cart-checkout').click()

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
try:
    WebDriverWait(driver,5).until(expected_conditions.presence_of_all_elements_located)
finally:
    driver.find_element_by_css_selector('.button-main.show').click()

payment_list = [driver.find_element_by_class_name('list')]
payment_list[0].click()

form_input = driver.find_element_by_name('cardnumber')
form_input.send_keys('4811111111111114'+Keys.TAB+'01/23'+Keys.TAB+'123')

driver.find_element_by_css_selector('.button-main.show').click()

driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
try:
    WebDriverWait(driver,5).until(expected_conditions.presence_of_all_elements_located)
finally:
    driver.find_element_by_id('PaRes').send_keys('112233')

driver.find_element_by_name('ok').click()


WebDriverWait(driver,3)
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# print driver.page_source
if("Transaction successful" in driver.page_source):
    print "buy_midtrans_pillow Success"
else:
    print "buy_midtrans_pillow Failed"
driver.close()

# Still using time.sleep, masih belum tahu bagaimana caranya menunda agar scriptnya nggak kecepetan.
# kadang suka kecepetan, abis itu suka nyari klik sebelum keload.
# Rupanya ada explicitnya, webDriverWait.