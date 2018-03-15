from selenium import webdriver

driver = webdriver.Chrome

driver.start_client()
driver.get('https://demo.midtrans.com/')

driver.find_element_by_class_name('btn buy').click()

driver.find_element_by_class_name('cart-checkout').click()
