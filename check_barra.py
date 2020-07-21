from selenium import webdriver
import http.client
import os.path
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

driver = webdriver.Firefox(executable_path=r'./geckodriver')
com = open('sites_dinamica.txt', 'a')
sem = open('sites_nao_dinamica.txt', 'a')
nada = open('sites_nada.txt', 'a')
error = open('sites_error.txt', 'a')
driver.set_page_load_timeout(300)

if not os.path.exists("screenshots_dinamica"):
    os.makedirs("screenshots_dinamica")
if not os.path.exists("screenshots_nao_dinamica"):
    os.makedirs("screenshots_nao_dinamica")
if not os.path.exists("screenshots_nada"):
    os.makedirs("screenshots_nada")
if not os.path.exists("screenshots_error"):
    os.makedirs("screenshots_error")

with open('sites.txt', 'r', encoding="ISO-8859-1") as f:
    for line in f:
        lsplit = line.split(';')[0]
        url = 'http://www.'+lsplit+'/'
        print(url)
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
            error.write('%s' % str(e))
            try:
                driver.save_screenshot("screenshots_error/site-"+lsplit+".png")
            except:
                error.write(' Não foi possível salvar screenshot de %s' % url)
                pass
            error.write('\n')
            error.flush()
            pass
    driver.close()
