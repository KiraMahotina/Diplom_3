import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        self.scroll_to_element_and_click(locator)

    def input_text(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def input_enter(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait_for_visibility_of_element_located(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_presence_of_element_located(self, locator, timeout=7):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_for_presence_of_changing_elements_located(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        WebDriverWait(self.driver, timeout).until(lambda driver: self.driver.find_element(*locator).text.strip() != text)

    def wait_for_element_to_be_clickable(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_url_contains(self, locator, timeout=7):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(locator))

    def wait_for_text_not_in_url(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda text: locator not in text.current_url)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_attribute(self, locator):
        div = self.driver.find_element(*locator)
        return div.get_attribute('class')

    @allure.step('Скролл до элемента и клик')
    def scroll_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Переключение Webdriver на новооткрытую вкладку')
    def change_webdriver_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание присутствия элемента по локатору')
    def wait_for_presence_of_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидание видимости элемента по локатору')
    def wait_for_visibility_of_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
