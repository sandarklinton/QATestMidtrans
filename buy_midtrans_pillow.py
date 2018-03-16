import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BuyMidtransPillow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)

    def test_buying_midtrans_pillow(self):
        driver = self.driver
        #1. Visit https://demo.midtrans.com
        driver.get('https://demo.midtrans.com/')
        self.assertIn('Sample Store', self.driver.title)

        #2. Click "BUY NOW"
        driver.find_element_by_css_selector('.btn.buy').click()
        self.assertIn('CHECKOUT', driver.find_element_by_class_name('cart-checkout').text)

        # 3. Click "CHECKOUT"
        driver.find_element_by_class_name('cart-checkout').click()
        # find something better than time.sleep lol
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        WebDriverWait(driver, 50).until(expected_conditions.text_to_be_present_in_element((By.ID, 'app'), 'CONTINUE'))
        self.assertIn('Continue', driver.page_source)

        # 4. Click "CONTINUE"
        driver.find_element_by_xpath("//a[@href='#/select-payment']").click()
        self.assertIn('Credit Card', driver.page_source)
        # 5. Click "Credit Card"
        payment_list = [driver.find_element_by_class_name('list')]
        payment_list[0].click()
        self.assertIn('Card number', driver.page_source)
        # 6. Enter Card number: 4811111111111114
        input_group = driver.find_elements_by_tag_name('input')
        input_group[0].send_keys('4811111111111114')

        # 7. Enter Expiry date: 01/23
        input_group[1].send_keys('01/23')

        # 8. Enter CVV: 123
        input_group[2].send_keys('123')

        # 9. Click "PAY NOW"
        driver.find_element_by_xpath("//a[@href='#/']").click()

        # 10. Enter Password:112233
        # the frame is different right now, relocate.
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

        WebDriverWait(driver, 50).until(
            expected_conditions.text_to_be_present_in_element((By.TAG_NAME, 'div'), 'Issuing Bank'))
        driver.find_element_by_name('PaRes').send_keys('112233')
        # 11. Click OK
        driver.find_element_by_name('ok').click()
        # 12. Verify that the word "Transaction Successful" is visible.
        #iframe is changing again, relocate.
        driver.switch_to.parent_frame()
        driver.switch_to.parent_frame()
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

        WebDriverWait(driver, 50).until(
            expected_conditions.text_to_be_present_in_element((By.ID, 'app'), 'Transaction successful'))

        assert "Transaction successful" in driver.page_source

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


# Dibawah ini adalah script sebelum menggunakan unitTest Python.
#
# driver = webdriver.Chrome()
# driver.set_page_load_timeout(20)
# driver.implicitly_wait(20)
#
# driver.get('https://demo.midtrans.com/')
#
# driver.find_element_by_css_selector('.btn.buy').click()
# driver.find_element_by_class_name('cart-checkout').click()
#
# driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# try:
#     WebDriverWait(driver,5).until(expected_conditions.presence_of_all_elements_located)
# finally:
#     driver.find_element_by_css_selector('.button-main.show').click()
#
# try:
#     WebDriverWait(driver,5).until(expected_conditions.presence_of_all_elements_located)
# finally:
#     payment_list = [driver.find_element_by_class_name('list')]
# payment_list[0].click()
#
# form_input = driver.find_element_by_name('cardnumber')
# form_input.send_keys('4811111111111114'+Keys.TAB+'01/23'+Keys.TAB+'123')
#
# driver.find_element_by_css_selector('.button-main.show').click()
#
# driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# try:
#     WebDriverWait(driver,5).until(expected_conditions.presence_of_all_elements_located)
# finally:
#     driver.find_element_by_id('PaRes').send_keys('112233')
#
# driver.find_element_by_name('ok').click()
#
#
# WebDriverWait(driver,3)
# driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
# # print driver.page_source
# assert "Transaction successfuaaa" in driver.page_source

# Still using time.sleep, masih belum tahu bagaimana caranya menunda agar scriptnya nggak kecepetan.
# kadang suka kecepetan, abis itu suka nyari klik sebelum keload.
# Rupanya ada explicitnya, webDriverWait.