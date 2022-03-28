# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 12:09:49 2022

@author: Lenovo
"""

from anticaptchaofficial.recaptchav2proxyless import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.amazon.com/errors/validateCaptcha"
page = driver.get(url)

time.sleep(10)

sitekey_clean = sitekey.split(" data-callb")
sitekey = driver.find_element(By.XPATH, '//*[/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img]').get_attribute('outerHTML')
sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1]
print(sitekey_clean)

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(os.environ["anticaptcha_api_key"])
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)

g_response = solver.solve_and_return_solution()
if g_response!= 0:
    print("g_response"+g_response)
else:
    print("task finished with error"+solver.error_code)

driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')

driver.find_element(By.XPATH, '//*[/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button]').click()

time.sleep(20)