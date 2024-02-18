from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="logo"]')))
        button.click()

    def open_about(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"o-nas.html")]')))
        button.click()

    def open_delivery_and_payment(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"dostavka-i-oplata.html")]')))
        button.click()

    def open_return(self):
        r_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"zamena")]')))
        r_button.click()

    def open_contacts(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"kontakty")]')))
        button.click()

    def open_help(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"help")]')))
        button.click()

    def open_reviews(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"testim")]')))
        button.click()

    def open_dropshopping(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//header//ul[contains(@class,"top-menu")]/li/a[contains(@href,"drop")]')))
        button.click()

#
# class Categories(BasePage):
#     def __init__(self):
#         super().__init__(self)

    def cat_menu(self):
        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        new_items = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH,'//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"novinki")]')))
        new_items.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        tactical_clothing = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"odezhda")]')))
        tactical_clothing.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        tactical_shoes = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"obuv")]')))
        tactical_shoes.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        tourism_camp = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"pohodnoe")]')))
        tourism_camp.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        military = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"ekipirovka")]')))
        military.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        tactical_equipment = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"takticheskoe")]')))
        tactical_equipment.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        gun_and_components = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH,'//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"oruzhejnoe")]')))
        gun_and_components.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        optics = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"binokli")]')))
        optics.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        bags = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"chemodanyi")]')))
        bags.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        fish_and_hunt = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"ryibalka")]')))
        fish_and_hunt.click()

        cat_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="mainmenubutton"]')))
        cat_button.click()

        trainers_and_sports = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class,"mainmenu")]/ul[@class="list-unstyled"]/li/a[contains(@href,"trenajeryi")]')))
        trainers_and_sports.click()


