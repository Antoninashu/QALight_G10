from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://qalight.ua/'
driver.get(url)

php = driver.find_element('xpath', '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/a')
php.click()
time.sleep(3)

about = driver.find_element('xpath', '/html/body/div[3]/div/div[2]/div/div[3]/ul/li[1]/a')
about.click()
time.sleep(3)

base = driver.find_element('xpath', '/html/body/div[3]/div/div[2]/div/div[3]/ul/li[4]/a')
base.click()
time.sleep(3)

url1 = 'https://dou.ua/'
driver.get(url1)

main = driver.find_element('xpath', '/html/body/div[1]/header/ul/li[2]/a')
main.click()
time.sleep(3)

salary = driver.find_element('xpath', '/html/body/div[1]/header/ul/li[5]/a')
salary.click()
time.sleep(3)

work = driver.find_element('xpath', '/html/body/div[2]/div[1]/header/ul/li[6]/a')
work.click()
time.sleep(3)

url2 = 'https://www.w3schools.com/'
driver.get(url2)

python = driver.find_element('xpath', '/html/body/div[3]/a[5]')
python.click()
time.sleep(3)

java = driver.find_element('xpath', '/html/body/div[3]/a[6]')
java.click()
time.sleep(3)

php = driver.find_element('xpath', '/html/body/div[3]/a[7]')
php.click()
time.sleep(3)

url3 = 'https://www.youtube.com/'
driver.get(url3)

music = driver.find_element('xpath',
                            '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[1]/ytd-feed-filter-chip-bar-renderer/div/div/div[3]/iron-selector/yt-chip-cloud-chip-renderer[4]/yt-formatted-string')
music.click()
time.sleep(3)

history = driver.find_element('xpath',
                              '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[1]/ytd-feed-filter-chip-bar-renderer/div/div/div[3]/iron-selector/yt-chip-cloud-chip-renderer[5]/yt-formatted-string')
history.click()
time.sleep(3)

gaming = driver.find_element('xpath',
                                  '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[1]/ytd-feed-filter-chip-bar-renderer/div/div/div[3]/iron-selector/yt-chip-cloud-chip-renderer[8]/yt-formatted-string')
gaming.click()
time.sleep(3)

url4 = 'https://www.rada.gov.ua/'
driver.get(url4)

lawmakind = driver.find_element('xpath', '/html/body/div[1]/div[1]/nav/div[1]/ul/li[2]/a')
lawmakind.click()
time.sleep(5)

legislation = driver.find_element('xpath', '/html/body/div[1]/div[1]/nav/div[1]/ul/li[3]/a')
legislation.click()
time.sleep(5)

activities = driver.find_element('xpath', '/html/body/div[1]/div[1]/nav/div[1]/ul/li[4]/a')
activities.click()
time.sleep(5)

url5 = 'https://www.unian.ua/'
driver.get(url5)

war = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/nav/div[2]/div[1]/ul/li[2]/a')
war.click()
time.sleep(5)

ukraine = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/nav/div[2]/div[1]/ul/li[3]/a')
ukraine.click()
time.sleep(5)

politics = driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/nav/div[2]/div[1]/ul/li[4]/a')
politics.click()
time.sleep(5)

url6 = 'https://audi.vipos.ua/'
driver.get(url6)

servise = driver.find_element('xpath', '/html/body/div[1]/header/div[2]/nav/div/div[3]/ul/li[2]/a')
servise.click()
time.sleep(5)

news = driver.find_element('xpath', '/html/body/div[1]/header/div[2]/nav/div/div[3]/ul/li[4]/a')
news.click()
time.sleep(5)

accessoriese = driver.find_element('xpath', '/html/body/div[1]/header/div[2]/nav/div/div[3]/ul/li[5]/a')
accessoriese.click()
time.sleep(3)

url7 = 'https://dance-school.kiev.ua/'
driver.get(url7)

style = driver.find_element('xpath', '/html/body/div[1]/div[2]/header/div[1]/div[4]/div[2]/div/nav[1]/ul/li[2]/a/span')
style.click()
time.sleep(5)

teachers = driver.find_element('xpath', '/html/body/div[1]/div[2]/header/div[1]/div[4]/div[2]/div/nav[1]/ul/li[5]/a/span')
teachers.click()
time.sleep(5)

comtacts = driver.find_element('xpath', '/html/body/div[1]/div[2]/header/div[1]/div[4]/div[2]/div/nav[1]/ul/li[8]/a/span')
comtacts.click()
time.sleep(3)

url8 = 'https://bi.ua/ukr/'
driver.get(url8)

heroes = driver.find_element('xpath', '/html/body/header/div[3]/nav/div[1]/div/div/a[2]')
heroes.click()
time.sleep(3)

brands = driver.find_element('xpath', '/html/body/header/div[3]/nav/div[1]/div/div/a[3]')
brands.click()
time.sleep(3)

stocks = driver.find_element('xpath', '/html/body/header/div[3]/nav/div[1]/div/div/a[4]')
stocks.click()
time.sleep(3)

url9 = 'https://masterzoo.ua/ua/'
driver.get(url9)

dogs = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div[3]/div/div/div/div/div/ul/li[3]/div[1]/a')
dogs.click()
time.sleep(5)

cats = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div[3]/div/div/div/div/div/ul/li[4]/div[1]/a')
cats.click()
time.sleep(5)

rodents = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div[3]/div/div/div/div/div/ul/li[6]/div[1]/a')
rodents.click()
time.sleep(3)
driver.quit()


