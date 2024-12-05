import requests
from bs4 import BeautifulSoup as bs

def key():
    response = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%97%D0%B2')
    soup = bs(response.text, 'html.parser')
    p = soup.find('p', class_='today-temp').text
    cleaned_text = p.replace("+", "").replace("°C", "").replace("*", "").strip()
    number = int(cleaned_text)
    print(number)
    return number

