from selenium import webdriver

# download chromedriver from http://chromedriver.chromium.org/downloads
# and replace the path with where you download it
driver = webdriver.Chrome('E:\Python scripts\chromedriver')

driver.get('https://www.linkedin.com/jobs/view/1304372932/')

print(driver.find_element_by_css_selector("div.description__text--rich").text)