# Requests
import requests
## Basic
response = requests.get('http://example.com')
print(response.text)

data = {'key': 'value'}

header = {'Content-Type': 'application/json'}

cookie = {'cookie_name': 'cookie_value'}

json = {'key': 'value'}
response =  requests.post('http://example.com', data=data)
response1 = requests.post('http://example.com', headers=header)
response2 = requests.post('http://example.com', cookies=cookie)
response3 = requests.post('http://example.com', json=json)
response4 = requests.post('http://example.com', data=data, headers=header, cookies=cookie, json=json)

## Advanced
### part 1
url = "http://www.example.com"
try:
    response = requests.get(url, timeout=5)
    print(response.status_code)
except requests.Timeout:
    print("The request timed out")
except requests.ConnectionError:
    print("There was a connection error")
except requests.RequestException as err:
    print("There was an exception : {err}")

### part 2
session = requests.Session()
login_url = "http://example.com/login"
data = {'username': 'user', 'password': 'pass'}

session.post(login_url, data=data)

dashboard_url = "http://example.com/dashboard"
response = session.get(dashboard_url)

print(response.text)

### part 3
import requests
from concurrent.futures import ThreadPoolExecutor


url_list = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Status code for {url}: {response.status_code}")
    except requests.Timeout:
        print(f"The request to {url} timed out")

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(fetch_url, url_list)

### part 4
import httpx
import asyncio

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(f"Status code for {url}: {response.status_code}")

urls = ["http://www.example.com"] * 10

async def main():
    tasks = [fetch_url(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())

# beautifulsoup4
## Bascic
from bs4 import BeautifulSoup
html = """<html><body><h1>Hello, Security!</h1></body></html>"""
soup = BeautifulSoup(html, "lxml")

print(soup.h1.text)

## Advanced
### part 1
import requests
from bs4 import BeautifulSoup
url = "http://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
print(soup.title.text)

### part 2
for link in soup.find_all('a'):
    print(link.get('href'))

### part 3
import requests
from bs4 import BeautifulSoup

url = "https://example.com/login"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

form = soup.find("form")
data = {}
for input_tag in form.find_all("input"):
    name = input_tag.get("name")
    if name:
        data[name] = "admin" if "user" in name else "password123"

login_url = form.get("action") or url
response = requests.post(login_url, data=data)

print(response.text)

### part 4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式

dirver = webdriver.Chrome(options=chrome_options)
dirver.get("http://example.com")

html = dirver.page_source
soup = BeautifulSoup(html, "lxml")
print(soup.find("h1").text)
dirver.quit()

### part 5
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

admin_paths = ["/admin", "/dashboard", "/manage", "/login"]

for link in soup.find_all("a"):
    href = link.get("href")
    if href and any(path in href for path in admin_paths):
        print(f"发现后台入口: {href}")

### part 6
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

for script in soup.find_all("script"):
    if script.string and "api" in script.string.lower():
        print(f"发现API调用: {script.string}")

# lxml
## Bascic
from lxml import etree

html = """<html><body><h1>Hello, Security!</h1></body></html>"""
tree = etree.HTML(html)

print(tree.xpath("//h1/text()"))

## Advanced
### part 1
import requests
from lxml import etree

url = "http://example.com"
response = requests.get(url)
tree = etree.HTML(response.text)

print(tree.xpath("//h1/text()"))
'''
XPATH : 
//tag : 选择所有tag元素
//tag[@attribute='value'] : 选择所有具有特定属性的tag元素
//tag[@attribute='value'][@attribute='value'] : 选择所有具有多个特定属性的tag元素
//tag[@attribute='value']/tag : 选择具有特定属性的tag元素的子元素
//tag[@attribute='value']/tag[@attribute='value'] : 选择具有特定属性的tag元素的具有特定属性的子元素
//tag[@attribute='value']/tag[@attribute='value']/tag : 选择具有特定属性的tag元素的具有特定属性的子元素的子元素
//tag/text() : 选择tag元素的文本内容
//tag/@attribute : 选择tag元素的属性值
//div[contains(@class, 'active')] : 选择具有特定类名的div元素
'''
# Selenium
## Bascic
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://example.com")

print(driver.title)
driver.quit()

## Advanced
element = driver.find_element("xpath", "//h1")
print(element.text)  # 获取 <h1> 的文本

element = driver.find_element("css selector", "h1")
print(element.text)

driver.find_element("id", "username")
driver.find_element("class name", "login-btn")
driver.find_element("name", "password")

element = driver.find_element("name", "q")
element.send_keys("Selenium Python")

button = driver.find_element("id", "submit")
button.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.switch_to.frame("iframe_id")

alert = driver.switch_to.alert
print(alert.text)  # 获取弹窗内容
alert.accept()  # 点击确定

driver.save_screenshot("screenshot.png")

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # 无头模式（不打开浏览器）
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://example.com")

# 录制页面
driver.save_screenshot("test.png")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com/login")

# 输入用户名
driver.find_element(By.NAME, "username").send_keys("admin")
# 输入密码
driver.find_element(By.NAME, "password").send_keys("password123" + Keys.RETURN)

print("登录成功！")

import time
from PIL import Image
import pytesseract

# 截取验证码
element = driver.find_element(By.ID, "captcha")
element.screenshot("captcha.png")

# 解析验证码
captcha_text = pytesseract.image_to_string(Image.open("captcha.png"))
print("识别出的验证码:", captcha_text)

# 输入验证码并提交
driver.find_element(By.NAME, "captcha").send_keys(captcha_text)
driver.find_element(By.ID, "submit").click()

# Scrapy
'''
项目结构：
myspider/
├── myspider/
│   ├── spiders/        # 爬虫代码
│   │   ├── example.py  # 爬虫逻辑
│   ├── items.py        # 数据结构
│   ├── pipelines.py    # 数据存储
│   ├── settings.py     # 爬虫配置
├── scrapy.cfg          # Scrapy 配置文件
'''

