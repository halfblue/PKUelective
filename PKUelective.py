#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from mail import *
from random import *
#chromePath = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
browser.get('https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=syllabus&appName=%E5%AD%A6%E7%94%9F%E9%80%89%E8%AF%BE%E7%B3%BB%E7%BB%9F&redirectUrl=http://elective.pku.edu.cn:80/elective2008/agent4Iaaa.jsp/../ssoLogin.do')
name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#user_name')))
password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#password')))
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#logon_button')))
yourname = '门户账号'
yourpass = '门户密码'
name.send_keys(yourname)
password.send_keys(yourpass)
submit.click()
butuixuan = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > table:nth-child(2) > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(8) > span > a')))
butuixuan.click()
refreshselector = '#refreshLimit44 > span'
refresh = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,refreshselector)))
# mlnum = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#electedNum44'))).text[6:]

while 1:
	refresh.click()
	time.sleep(0.1)
	result = EC.alert_is_present()(browser)
	time.sleep(0.5)
	if result:
		alerttext = result.text
		result.accept()
	else:
		sendmail()
		exit()
	if(alerttext=="刷新失败，请刷新页面。"):
		# print(alerttext)
		browser.refresh()
	refresh = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,refreshselector)))
	time.sleep(randint(3,4))
