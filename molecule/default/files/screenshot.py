import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)
driver.get('http://wordpress/wordpress')

w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_size(w, h)

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./screenshot.png")

driver.save_screenshot(filename)

driver.quit()
