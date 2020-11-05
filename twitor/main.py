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

""" twitor.main module """

from typing import Any, Optional

from .driver.chrome import Driver
from .consts.config import Config
from .consts.xpath import XPath


class Twitor:

    driver: Driver

    def __init__(self, os_type: str) -> None:
        """
        :param str 'mac' or 'windows' or 'linux'
        """
        self.driver = Driver(os_type)

    def login(self, mail: str, passwd: str) -> None:
        url: str = Config.TWITTER_HOST + Config.TWITTER_LOGIN_PATH
        self.driver.access(url)
        self.driver.sleep(1)
        self.driver.input_text_by_xpath(mail, XPath.TWITTER_LOGIN_USER_ID_INPUT)
        self.driver.input_text_by_xpath(passwd, XPath.TWITTER_LOGIN_USER_PASSWORD_INPUT)
        self.driver.click_button_by_xpath(XPath.TWITTER_LOGIN_USER_BUTTON)

    def tweet(self, text: str) -> None:
        url: str = Config.TWITTER_HOST + Config.TWITTER_TWEET_PATH
        self.driver.access(url)
        self.driver.sleep(1)
        self.driver.input_text_by_xpath(text, XPath.TWITTER_TWEET_SEND_INPUT)
        self.driver.click_button_by_xpath(XPath.TWITTER_TWEET_SEND_BUTTON)
        self.driver.sleep(1)

    def get_user(self, screen_name: str) -> None:
        url: str = Config.TWITTER_HOST + Config.TWITTER_USER_PATH.format(id=screen_name)
        self.driver.access(url)
        self.driver.sleep(1)
        if "@" not in self.driver.get_title():
            raise Exception("user not found.")

    def __enter__(self) -> Any:
        return self

    def __exit__(
        self, ex_type: Optional[Any], ex_value: Optional[Any], trace: Optional[Any]
    ) -> None:
        self.driver.exit()
