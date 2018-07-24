from selenium import webdriver
import httplib
import os.path
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import WebDriverException

driver = webdriver.Firefox(executable_path=r'./geckodriver')
com = open('sites_dinamica.txt', 'wa')
sem = open('sites_nao_dinamica.txt', 'wa')
nada = open('sites_nada.txt', 'wa')
error = open('sites_error.txt', 'wa')
driver.set_page_load_timeout(30)

if not os.path.exists("screenshots_dinamica"):
    os.makedirs("screenshots_dinamica")
if not os.path.exists("screenshots_nao_dinamica"):
    os.makedirs("screenshots_nao_dinamica")
if not os.path.exists("screenshots_nada"):
    os.makedirs("screenshots_nada")
if not os.path.exists("screenshots_error"):
    os.makedirs("screenshots_error")

with open('sites.txt', 'rU') as f:
    for line in f:
        lsplit = line.split(';')[0]
        url = 'http://www.'+lsplit+'/'
        print url
        try:
            driver.get(url)
            if ("barra.brasil.gov.br/barra.js" in driver.page_source):
                com.write('%s' % url +'\n')
                com.flush()
                driver.save_screenshot("screenshots_dinamica/site-"+lsplit+".png")
            else:
                if ("wrapper-barra-brasil" in driver.page_source):
                    sem.write('%s' % url +'\n')
                    sem.flush()
                    driver.save_screenshot("screenshots_nao_dinamica/site-"+lsplit+".png")
                else:
                    nada.write('%s' % url +'\n')
                    nada.flush()
                    driver.save_screenshot("screenshots_nada/site-"+lsplit+".png")
        except Exception as e:
            error.write('%s' % str(e) +'\n') 
            error.flush()
            driver.save_screenshot("screenshots_error/site-"+lsplit+".png")
            pass 
    driver.close()

