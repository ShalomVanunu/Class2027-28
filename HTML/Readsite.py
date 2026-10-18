import requests

url = "https://keithgalli.github.io/web-scraping/webpage.html"

url_content = requests.get(url).text
print(url_content)

