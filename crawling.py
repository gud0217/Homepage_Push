from bs4 import BeautifulSoup as bs
import requests

url = "https://www.hongik.ac.kr/index.do"

response = requests.get(url)
soup = bs(response.text, 'html.parser')

text = soup.find_all('div', class_='tab q1 current')
for element in text:
    notice = element.find_all('tr', class_='new')
    for i in notice:
        text_content = i.get_text()
        link = i.a['href'] if i.a else Nones
        print(text_content)
        print("https://www.hongik.ac.kr/" + link)