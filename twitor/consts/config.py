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

""" twitor.consts.config module """


class Config:
    """
    Drivers official website
    https://chromedriver.chromium.org/downloads
    """

    CHROME_DRIVER_VERSION = "86.0.4240.22"

    CHROME_DRIVER_DL_LINK = {
        "linux": f"https://chromedriver.storage.googleapis.com/{CHROME_DRIVER_VERSION}/chromedriver_linux64.zip",
        "windows": f"https://chromedriver.storage.googleapis.com/{CHROME_DRIVER_VERSION}/chromedriver_win32.zip",
        "mac": f"https://chromedriver.storage.googleapis.com/{CHROME_DRIVER_VERSION}/chromedriver_mac64.zip",
    }

    CHROME_DRIVER_PATH = {
        "linux": "./chromedriver.exe",
        "windows": "./chromedriver",
        "mac": "./chromedriver",
    }

    TWITTER_HOST = "https://twitter.com"
    TWITTER_LOGIN_PATH = "/login"
    TWITTER_USER_PATH = "/{id}"
    TWITTER_TWEET_PATH = "/compose/tweet"
