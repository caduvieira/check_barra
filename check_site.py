from selenium import webdriver
import http.client
import os.path
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


import requests
 
def download_file_from_server_endpoint(server_endpoint, local_file_path):
 
    # Send HTTP GET request to server and attempt to receive a response
    response = requests.get(server_endpoint)
     
    # If the HTTP GET request can be served
    if response.status_code == 200:
         
        # Write the file contents in the response to a file specified by local_file_path
        with open(local_file_path, 'wb') as local_file:
            for chunk in response.iter_content(chunk_size=128):
                local_file.write(chunk)

driver = webdriver.Firefox(executable_path=r'./geckodriver')
com = open('sites_ok.txt', 'a')
error = open('sites_error.txt', 'a')
driver.set_page_load_timeout(300)

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
if not os.path.exists("screenshots_error"):
    os.makedirs("screenshots_error")

download_file_from_server_endpoint('http://dominios.governoeletronico.gov.br/dados-abertos/Dominios_GovBR_basico.csv', 'sites.txt')

with open('sites.txt', 'r', encoding="ISO-8859-1") as f:
    for line in f:
        lsplit = line.split(';')[0]
        url = 'http://www.'+lsplit+'/'
        print(url)
        try:
            driver.get(url)
            com.write('%s' % url +'\n')
            com.flush()
            driver.save_screenshot("screenshots/site-"+lsplit+".png")
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
