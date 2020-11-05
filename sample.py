import os

from dotenv import load_dotenv

from twitor import Twitor

load_dotenv(verbose=True)
load_dotenv(".env")

USER_ID: str = os.environ["USER_ID"]
PASSWORD: str = os.environ["PASSWORD"]

if __name__ == "__main__":
    twitter = Twitor("mac")
    # with Twitor("mac") as twitter:
    twitter.get_user(USER_ID)
    twitter.login(USER_ID, PASSWORD)
    for count in range(5):
        twitter.tweet(f'Tweet test {count}')
