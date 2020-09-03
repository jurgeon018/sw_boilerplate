import requests 


x = requests.get('http://atlanticexpress.com.ua/')
print(x.content)