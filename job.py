from selenium import webdriver
import json



# Download chromedriver from http://chromedriver.chromium.org/downloads and replace the path with where you download it
driver = webdriver.Chrome('E:\Python scripts\chromedriver')


print("Welcome to Cover Letter Premium!")
print("------------------------------")
job_url = input("please input your URL: ")
# breakpoint()
driver.get(job_url)

print(driver.find_element_by_css_selector("div.description__text--rich").text)



parsed_response = json.loads(response.text)
print(parsed_response.keys())