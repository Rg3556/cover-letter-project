from selenium import webdriver

# download chromedriver from http://chromedriver.chromium.org/downloads
# and replace the path with where you download it
driver = webdriver.Chrome('E:\Python scripts\chromedriver')
print("Welcome to Cover Letter Premium!")
print("------------------------------")
job_url = input("please input your URL: ")
# breakpoint()
driver.get(job_url)
#driver.get('https://www.linkedin.com/jobs/view/1304372932/')

job_info =  driver.find_element_by_tag_name('title').get_attribute('text')
print(job_info)
breakpoint()
info_list = job_info.split('hiring')
title = info_list[1]
company = info_list[0]
description = driver.find_element_by_css_selector("div.description__text--rich").text

job_dict = {
	'title': title,
	'company': company,
	'description': description
}

print(job_dict)
