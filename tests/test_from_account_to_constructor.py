from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


class TestFromAccountToConstructor:
    def test_account_to_constructor(self, driver):
        driver.find_element(*locators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )

        driver.find_element(*locators.CONSTRUCTOR_TITLE).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.MAKE_BURGER_TITLE
            )
        )

    def test_account_to_logo(self, driver):
        driver.find_element(*locators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )

        driver.find_element(*locators.MAIN_LOGO).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.MAIN_LOGO
            )
        )
