from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the Mumzworld webstore
    driver.get('https://www.mumzworld.com/')

    # Step 2: Wait for the search box to be present using the ID
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, 'search_textbox')))

    # Search for a product - Car seat
    search_box.send_keys('car seat')

    # Step 3: Click the search button
    search_button = wait.until(EC.element_to_be_clickable((By.ID, 'search_btn')))
    search_button.click()

    # Step 4: Wait for the product cards to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ProductCard_productCard__kFgss')))

    # Step 5: Click the "Add to Cart" button for the first product -
    add_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="add_cart_button"]')))
    add_cart_button.click()

    # Step 6:  Go to the cart page
    driver.get('https://www.mumzworld.com/en/cart')

    # Step 7: Increase quantity to 5 items
    qty_input = wait.until(EC.presence_of_element_located((By.NAME, 'qty')))
    qty_input.clear()
    qty_input.send_keys('5')

    # Step 8: Click Proceed to Checkout
    proceed_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Proceed to Checkout"]')))
    proceed_checkout_button.click()

    # Step 9: Click on Create Account Button
    create_account = wait.until(EC.element_to_be_clickable((By.ID, 'create_account_button')))
    create_account.click()

    # Step 10: Fill details for registration
    # Wait for the first name input to be present and fill it
    first_name_input = wait.until(EC.presence_of_element_located((By.ID, 'firstname')))
    first_name_input.send_keys('Hamza')

    # Wait for the last name input to be present and fill it
    last_name_input = wait.until(EC.presence_of_element_located((By.ID, 'lastname')))
    last_name_input.send_keys('Khalid')

    # Wait for the email input to be present and fill it - this email needs to be updated to avid error
    email_input = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    email_input.send_keys('mummztest@gmail.com')

    # Wait for the password input to be present and fill it
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_input.send_keys('Password123')

    # Step 11: Click the "Create Account" button
    register_button = wait.until(EC.element_to_be_clickable((By.ID, 'register_btn')))
    register_button.click()

finally:
    # Close the browser
    input("Press Enter to close the browser...")
    driver.quit()