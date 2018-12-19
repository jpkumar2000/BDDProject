from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class WebObject(object):
    __TIMEOUT = 10

    def __init__(self, web_driver):
        print("WebObject Constructor called 3rd")
        super(WebObject, self).__init__()  # in python 3.6 you can just call super().__init__()
        self._web_driver_wait = WebDriverWait(web_driver, WebObject.__TIMEOUT)
        self._web_driver = web_driver

    def open(self, url):
        self._web_driver.get(url)

    def find_by_ID(self,id):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def switch_to_frame(self,frame_name):
        self._web_driver.switch_to.frame(self._web_driver.find_element_by_tag_name(frame_name))

    def switch_to_default(self):
        self._web_driver.switch_to.default_content()

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def find_ids(self,id):
        self.switch_to_frame("iframe")
        ids = self._web_driver.find_elements_by_xpath('//*[@id]')
        for ii in ids:

            if ii.get_attribute('id') == id:
                print("ID Match "+id)
                return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id)))
            else:
                print("No Match Found")
        self.switch_to_default()
