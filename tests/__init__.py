import os

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(TEST_DIR)

CHROME_DRIVER = PROJ_DIR + '/browsers/chromedriver'

BASE_URL = "https://app.getmetastream.com/"