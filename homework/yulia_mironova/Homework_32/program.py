from time import sleep
import requests

i = 1
while True:
    requests.get('https://www.google.com/')
    print(f'{i} - {"четное" if i % 2 == 0 else "нечетное"} число')
    i += 1
    sleep(2)
