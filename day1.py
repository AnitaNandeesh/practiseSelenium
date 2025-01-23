from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from time import sleep

opt = Options()
opt.add_argument("--disable-popup-blocking")

driver = WebDriver(options=opt)
wait = WebDriverWait(driver,20)

driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
driver.maximize_window()

search = driver.find_element("xpath","//span[@id='4']")
v = element_to_be_clickable(search)
wait.until(v)

search.send_keys('max')
