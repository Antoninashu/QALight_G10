from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

url1 = 'https://test.mensa.no/'
driver.get(url1)
xpath_template = '//div[contains(@id, "question_") and @style = ""]'

age_1850 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "ageselect_1850")]')))
age_1850.click()

start_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'startTest')))
start_button.click()
# time.sleep(1)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q1_a_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_0"]//div[@data-answerid="0"]')))
q1_a_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q2_b_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_1"]//div[@data-answerid="1"]')))
q2_b_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q3_c_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_2"]//div[@data-answerid="2"]')))
q3_c_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q4_f_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_3"]//div[@data-answerid="5"]')))
q4_f_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q5_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_4"]//div[@data-answerid="3"]')))
q5_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q6_e_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_5"]//div[@data-answerid="4"]')))
q6_e_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q7_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_6"]//div[@data-answerid="3"]')))
q7_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q8_a_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_7"]//div[@data-answerid="0"]')))
q8_a_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q9_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_8"]//div[@data-answerid="3"]')))
q9_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q10_c_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_9"]//div[@data-answerid="2"]')))
q10_c_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q11_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_10"]//div[@data-answerid="3"]')))
q11_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q12_f_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_11"]//div[@data-answerid="5"]')))
q12_f_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q13_e_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_12"]//div[@data-answerid="4"]')))
q13_e_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q14_b_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_13"]//div[@data-answerid="1"]')))
q14_b_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q15_e_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_14"]//div[@data-answerid="4"]')))
q15_e_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q16_b_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_15"]//div[@data-answerid="2"]')))
q16_b_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q17_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_16"]//div[@data-answerid="3"]')))
q17_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q18_f_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_17"]//div[@data-answerid="5"]')))
q18_f_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q19_a_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_18"]//div[@data-answerid="0"]')))
q19_a_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q20_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_19"]//div[@data-answerid="3"]')))
q20_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q21_f_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_20"]//div[@data-answerid="5"]')))
q21_f_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q22_e_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_21"]//div[@data-answerid="4"]')))
q22_e_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q23_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_22"]//div[@data-answerid="3"]')))
q23_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q24_b_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_23"]//div[@data-answerid="1"]')))
q24_b_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q25_a_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_24"]//div[@data-answerid="0"]')))
q25_a_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q26_b_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_25"]//div[@data-answerid="1"]')))
q26_b_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q27_f_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_26"]//div[@data-answerid="5"]')))
q27_f_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q28_e_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_27"]//div[@data-answerid="4"]')))
q28_e_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q29_a_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_28"]//div[@data-answerid="0"]')))
q29_a_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q30_d_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_29"]//div[@data-answerid="3"]')))
q30_d_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q31_b_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_30"]//div[@data-answerid="1"]')))
q31_b_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q32_e_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_31"]//div[@data-answerid="4"]')))
q32_e_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q33_f_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_32"]//div[@data-answerid="5"]')))
q33_f_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q34_a_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_33"]//div[@data-answerid="0"]')))
q34_a_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_template)))
q35_c_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="question_34"]//div[@data-answerid="2"]')))
q35_c_button.click()

time.sleep(3)