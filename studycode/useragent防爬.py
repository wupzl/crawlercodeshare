import requests

domain = 'https://www.dy2018.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.8011 SLBChan/111 SLBVPV/64-bit'
}
response = requests.get(domain, headers=headers)
print(response.text)
