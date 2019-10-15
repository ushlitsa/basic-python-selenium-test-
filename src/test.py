from selenium import webdriver
driver = webdriver.Chrome('E:/Studying/QAA/1/chromedriver_win32/chromedriver')
driver.get("https://wikipedia.org")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//*[@id='search-form']/fieldset/button")

search_field.send_keys("Автоматизированное тестирование")
search_button.click()

assert "Автоматизированное тестирование" in driver.title
driver.quit()