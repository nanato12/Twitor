#  MIT License

#  Copyright (c) 2020 ななといつ

#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:

#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

""" twitor.driver.chrome module """

import os
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from ..consts.config import Config
from .utils import download_driver


class Driver:
    def __init__(self, os_type: str, headless: bool = False) -> None:
        driver_path = Config.CHROME_DRIVER_PATH[os_type]
        if not os.path.exists(driver_path):
            download_driver(os_type)
        os.chmod(driver_path, 755)

        # Driver setting
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        self.chrome = Chrome(options=options, executable_path=driver_path)

    def sleep(self, seconds: int) -> None:
        sleep(seconds)

    def access(self, url: str) -> None:
        self.chrome.get(url)

    def input_text_by_xpath(self, text: str, xpath: str) -> None:
        xpath_element = self.chrome.find_element_by_xpath(xpath)
        xpath_element.send_keys(text)

    def click_button_by_xpath(self, xpath: str) -> None:
        xpath_element = self.chrome.find_element_by_xpath(xpath)
        xpath_element.click()

    def get_title(self) -> str:
        return self.chrome.title

    def exit(self) -> None:
        self.chrome.quit()
