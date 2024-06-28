# GOOGLE CHROME BROWSER ------------------------------------------------------------------------------------------------

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Initialize the Chrome Webdriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# LOGIN PAGE ON GOOGLE CHROME ------------------------------------------------------------------------------------------
UserName = driver.find_element(By.CSS_SELECTOR,
                               '#user-name')
UserName.send_keys("standard_user")
time.sleep(5)

Password = driver.find_element(By.CSS_SELECTOR,
                               '#password')
Password.send_keys("secret_sauce")

LoginButton = driver.find_element(By.CSS_SELECTOR,
                                  '#login-button')
LoginButton.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# PRODUCTS ORDERED ON GOOGLE CHROME ------------------------------------------------------------------------------------
# SAUCE LABS BACKPACK --------------------------------------------------------------------------------------------------
SauceLabsBackpack_AddToCart_Button = driver.find_element(By.XPATH,
                                                         '//*[@id="add-to-cart-sauce-labs-backpack"]')
SauceLabsBackpack_AddToCart_Button.click()
time.sleep(5)

# SAUCE LABS BIKE LIGHT -----------------------------------------------------------------------------------------------
SauceLabsBikeLight_AddToCart_Button = driver.find_element(By.XPATH,
                                                          '//*[@id="add-to-cart-sauce-labs-bike-light"]')
SauceLabsBikeLight_AddToCart_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# SHOPPING CART BUTTON ON GOOGLE CHROME --------------------------------------------------------------------------------
ShoppingCart_Button = driver.find_element(By.CSS_SELECTOR,
                                          '#shopping_cart_container')
ShoppingCart_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CHECKOUT PAGE ON GOOGLE CHROME ---------------------------------------------------------------------------------------
Checkout_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#checkout')
Checkout_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------
# YOUR INFORMATION PAGE ON GOOGLE CHROME -------------------------------------------------------------------------------
FirstName = driver.find_element(By.CSS_SELECTOR,
                                '#first-name')
FirstName.send_keys("Martha")
time.sleep(5)

LastName = driver.find_element(By.CSS_SELECTOR,
                               '#last-name')
LastName.send_keys("Automation")
time.sleep(5)

ZipPostalCode = driver.find_element(By.CSS_SELECTOR,
                                    '#postal-code')
ZipPostalCode.send_keys("12345")
time.sleep(5)

Continue_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#continue')
Continue_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CHECKOUT: OVERVIEW PAGE ON GOOGLE CHROME -----------------------------------------------------------------------------
Finish_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#finish')
Finish_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------
# BACK HOME BUTTON ON GOOGLE CHROME ------------------------------------------------------------------------------------
BackHome_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#back-to-products')
BackHome_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------------------------

# COLLAPSIBLE BUTTON ON GOOGLE CHROME ----------------------------------------------------------------------------------
Collapsible_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#react-burger-menu-btn')
Collapsible_Button.click()
time.sleep(5)

# LOG-OUT BUTTON ON GOOGLE CHROME---------------------------------------------------------------------------------------
LogOut_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#logout_sidebar_link')
LogOut_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CLOSE THE BROWSER ON GOOGLE CHROME -----------------------------------------------------------------------------------
driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# MICROSOFT EDGE BROWSER -----------------------------------------------------------------------------------------------
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# INITIALIZE THE MICROSOFT EDGE WEBDRIVER USING WEBDRIVER MANAGER ------------------------------------------------------
driver = webdriver.Edge()

# OPEN THE WEBSITE -----------------------------------------------------------------------------------------------------
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# LOGIN PAGE ON MICROSOFT EDGE -----------------------------------------------------------------------------------------
UserName = driver.find_element(By.CSS_SELECTOR,
                               '#user-name')
UserName.send_keys("standard_user")
time.sleep(5)

Password = driver.find_element(By.CSS_SELECTOR,
                               '#password')
Password.send_keys("secret_sauce")

LoginButton = driver.find_element(By.CSS_SELECTOR,
                                  '#login-button')
LoginButton.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# PRODUCTS ORDERED ON MICROSOFT EDGE -----------------------------------------------------------------------------------
# SAUCE LABS FLEECE JACKET ----------------------------------------------------------------------------------------------
SauceLabsFleeceJacket_AddToCart_Button = driver.find_element(By.XPATH,
                                                             '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
SauceLabsFleeceJacket_AddToCart_Button.click()
time.sleep(5)

# SAUCE LABS BOLT T-SHIRT ----------------------------------------------------------------------------------------------
SauceLabsBoltTShirt_AddToCart_Button = driver.find_element(By.XPATH,
                                                           '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
SauceLabsBoltTShirt_AddToCart_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# SHOPPING CART BUTTON ON MICROSOFT EDGE -------------------------------------------------------------------------------
ShoppingCart_Button = driver.find_element(By.CSS_SELECTOR,
                                          '#shopping_cart_container')
ShoppingCart_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CHECKOUT PAGE ON MICROSOFT EDGE --------------------------------------------------------------------------------------
Checkout_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#checkout')
Checkout_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------
# YOUR INFORMATION PAGE ON MICROSOFT EDGE ------------------------------------------------------------------------------
FirstName = driver.find_element(By.CSS_SELECTOR,
                                '#first-name')
FirstName.send_keys("Martha")
time.sleep(5)

LastName = driver.find_element(By.CSS_SELECTOR,
                               '#last-name')
LastName.send_keys("Automation")
time.sleep(5)

ZipPostalCode = driver.find_element(By.CSS_SELECTOR,
                                    '#postal-code')
ZipPostalCode.send_keys("12345")
time.sleep(5)

Continue_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#continue')
Continue_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CHECKOUT: OVERVIEW PAGE ON MICROSOFT EDGE ----------------------------------------------------------------------------
Finish_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#finish')
Finish_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# BACK HOME BUTTON ON MICROSOFT EDGE -----------------------------------------------------------------------------------
BackHome_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#back-to-products')
BackHome_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# COLLAPSIBLE BUTTON ON MICROSOFT EDGE ---------------------------------------------------------------------------------
Collapsible_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#react-burger-menu-btn')
Collapsible_Button.click()
time.sleep(5)

# LOG-OUT BUTTON ON MICROSOFT EDGE -------------------------------------------------------------------------------------
LogOut_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#logout_sidebar_link')
LogOut_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CLOSE THE BROWSER ON MICROSOFT EDGE
driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# MOZILLA FIREFOX BROWSER ----------------------------------------------------------------------------------------------
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# INITIALIZE
# Initialize the Chrome Webdriver using WebDriver manager
driver = webdriver.Firefox()

# Open a website
driver.get("https://www.saucedemo.com")
driver.maximize_window()
time.sleep(5)

# --------------------------------# ------------------------------------------------------------------------------------

# LOGIN PAGE ON MOZILLA FIREFOX ----------------------------------------------------------------------------------------
UserName = driver.find_element(By.CSS_SELECTOR,
                               '#user-name')
UserName.send_keys("standard_user")
time.sleep(5)

Password = driver.find_element(By.CSS_SELECTOR,
                               '#password')
Password.send_keys("secret_sauce")

LoginButton = driver.find_element(By.CSS_SELECTOR,
                                  '#login-button')
LoginButton.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# PRODUCTS ORDERED ON MOZILLA FIREFOX ----------------------------------------------------------------------------------
# SAUCE LABS ONESIE ----------------------------------------------------------------------------------------------------
SauceLabsOnesie_AddToCart_Button = driver.find_element(By.XPATH,
                                                       '//*[@id="add-to-cart-sauce-labs-onesie"]')
SauceLabsOnesie_AddToCart_Button.click()

# TEST ALL THINGS() T-SHIRT (RED) --------------------------------------------------------------------------------------
TestAllThings_AddToCart_Button = driver.find_element(By.XPATH,
                                                     '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
TestAllThings_AddToCart_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# SHOPPING CART BUTTON ON MOZILLA FIREFOX ------------------------------------------------------------------------------
ShoppingCart_Button = driver.find_element(By.CSS_SELECTOR,
                                          '#shopping_cart_container')
ShoppingCart_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CHECKOUT PAGE ON MICROSOFT EDGE --------------------------------------------------------------------------------------
Checkout_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#checkout')
Checkout_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------
# YOUR INFORMATION PAGE ON MOZILLA FIREFOX -----------------------------------------------------------------------------
FirstName = driver.find_element(By.CSS_SELECTOR,
                                '#first-name')
FirstName.send_keys("Martha")
time.sleep(5)

LastName = driver.find_element(By.CSS_SELECTOR,
                               '#last-name')
LastName.send_keys("Automation")
time.sleep(5)

ZipPostalCode = driver.find_element(By.CSS_SELECTOR,
                                    '#postal-code')
ZipPostalCode.send_keys("12345")
time.sleep(5)

Continue_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#continue')
Continue_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CHECKOUT: OVERVIEW PAGE ON MOZILLA FIREFOX ---------------------------------------------------------------------------
Finish_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#finish')
Finish_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# BACK HOME BUTTON ON MOZILLA FIREFOX ----------------------------------------------------------------------------------
BackHome_Button = driver.find_element(By.CSS_SELECTOR,
                                      '#back-to-products')
BackHome_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# COLLAPSIBLE BUTTON ON MOZILLA FIREFOX --------------------------------------------------------------------------------
Collapsible_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#react-burger-menu-btn')
Collapsible_Button.click()
time.sleep(5)

# LOG-OUT BUTTON ON MOZILLA FIREFOX ------------------------------------------------------------------------------------
LogOut_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#logout_sidebar_link')
LogOut_Button.click()
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------

# CLOSE THE BROWSER ON MOZILLA FIREFOX ---------------------------------------------------------------------------------
driver.quit()
