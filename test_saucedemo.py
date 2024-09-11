import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Предполагается, что у вас установлен ChromeDriver
        self.driver.get("https://www.saucedemo.com/")

    def test_purchase_flow(self):
        # Авторизация
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # Выбор товара
        add_to_cart_button = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")
        add_to_cart_button.click()

        # Переход в корзину
        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

        # Проверка наличия товара в корзине
        cart_item = self.driver.find_element(By.CLASS_NAME, "cart_item")
        self.assertIsNotNone(cart_item)

        # Оформление покупки
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Заполнение информации
        first_name = self.driver.find_element(By.ID, "first-name")
        last_name = self.driver.find_element(By.ID, "last-name")
        postal_code = self.driver.find_element(By.ID, "postal-code")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        postal_code.send_keys("12345")

        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

        # Завершение покупки
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

        # Проверка успешного завершения покупки
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        self.assertEqual(success_message.text, "Thank you for your order!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()