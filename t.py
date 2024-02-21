from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from helper.pages.base import *


driver = webdriver.Chrome()
driver.maximize_window()
option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)

url = 'https://killa.com.ua/uk'
driver.get(url)

# home = BasePage(driver)
fish_hunt = FishHunt(driver)
accses = AccessoriesSorting(driver)

# home.open_about()
# home.open_delivery_and_payment()
# home.open_return()
# home.open_contacts()
# home.open_help()
# home.open_reviews()
# home.open_dropshopping()
# home.open_homepage()
# home.cat_menu()
fish_hunt.cat_button()
# print(fish_hunt.fish_hunt_list())
accses.fish_accessories()
accses.sort_button()


time.sleep(5)