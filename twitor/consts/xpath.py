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

""" twitor.consts.xpath module """


class XPath:
    """
    xpath copied from chrome.

    *_INPUT: input form
    *_BUTTON: button
    """

    TWITTER_LOGIN_USER_ID_INPUT = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
    TWITTER_LOGIN_USER_PASSWORD_INPUT = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
    TWITTER_LOGIN_USER_BUTTON = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div'

    TWITTER_TWEET_SEND_INPUT = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
    TWITTER_TWEET_SEND_BUTTON = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'
