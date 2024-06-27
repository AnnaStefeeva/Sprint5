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

        enter_button_title = driver.find_element(*locators.ENTER_BUTTON).text
        assert enter_button_title == "Войти"
