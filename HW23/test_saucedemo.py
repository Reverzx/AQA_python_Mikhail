import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


def test_saucedemo_buy_path():
    try:
        # Autorization
        driver.get("https://www.saucedemo.com/")
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Cart
        add_to_cart_button = wait.until(
            EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        add_to_cart_button.click()
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Checkout: Your Information
        first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys("Миша")
        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Заходин")
        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("1111")
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        finish_button = driver.find_element(By.ID, "finish")
        finish_button.click()

        # Assert
        message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert "Thank you for your order!" == message.text

    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("error.png")
    finally:
        driver.quit()
        time.sleep(3)


def test_saucedemo_add_and_remove():
    try:
        # Autorization
        driver.get("https://www.saucedemo.com/")
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("standard_user")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Cart
        add_to_cart_button = wait.until(
            EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        add_to_cart_button.click()
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Assert
        message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                               "inventory_item_name")))
        assert "Sauce Labs Bolt T-Shirt" == message.text
        # Cart_remove
        remove_icon = wait.until(EC.visibility_of_element_located
                                 ((By.ID, "remove-sauce-labs-bolt-t-shirt")))
        remove_icon.click()
        message_void = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                    "removed_cart_item")))
        assert len(message_void.text) == 0

    except Exception as e:
        print(f"Ошибка: {e}")
        driver.save_screenshot("error.png")
    finally:
        driver.quit()
        time.sleep(3)
