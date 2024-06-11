from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


class TestTransitionToAccount:
    def test_account_button(self, driver):
        driver.find_element(*locators.ACCOUNT_LINK).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locators.ENTER_BUTTON
            )
        )
