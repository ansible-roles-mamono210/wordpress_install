import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Reading the public IP address from /tmp/ip_address.txt
with open('/tmp/ip_address.txt', 'r') as file:
    public_ip = file.read().strip()

# Constructing the URL for WordPress
target_url = f"http://{public_ip}/wordpress"

# Setting up headless Firefox options
options = Options()

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

driver.get(target_url)

w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_rect(width=w, height=h)

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./screenshot.png")

driver.save_screenshot(filename)

driver.quit()
