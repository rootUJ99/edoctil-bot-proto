import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_cmd(url):
  driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
  options = webdriver.ChromeOptions()
  options.headless = True
  driver.get(url)
  time.sleep(10) # Let the user actually see something!
  header = driver.find_element(By.XPATH, "//*[@data-cy='question-title']")
  new_header = '_'.join(header.text.split('.')[-1].split(' '))
  os.chdir('..')
  try:
    os.mkdir(new_header)
  except FileExistsError:
    try:
      os.rmdir(new_header)
      os.mkdir(new_header)
    except OSError:
      l = len(os.listdir())
      os.rmdir(f'{new_header}_{l+1}')

  os.chdir(new_header)
  with open('script.py', 'w'):
    pass

if __name__ == '__main__':
  run_cmd(input('url = ')) 
  '''
  example url https://leetcode.com/problems/two-sum
  '''
  # run_cmd('https://leetcode.com/problems/two-sum') 

