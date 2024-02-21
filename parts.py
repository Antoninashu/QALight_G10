from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def base_waits(driver, xpath):
    waiers = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    waiers.click()

