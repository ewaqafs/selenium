from  selenium import webdriver
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("diasble-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element_by_xpath("/html/body/div[1]/h1[1]")
    return element

print(main())


