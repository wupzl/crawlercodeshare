import requests

headers = {
}

data = {
    'prodCatid': '1186',
}

response = requests.post('http://www.xinfadi.com.cn/getCat.html', headers=headers, data=data, verify=False)
print(response.text)