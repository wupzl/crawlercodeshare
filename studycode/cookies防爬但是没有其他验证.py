import requests

cookies = {
    'Hm_lvt_9c5f07b6ce20e3782eac91ed47d1421c': '1738911846,1738912439',
    'HMACCOUNT': 'D0C5A2CB881AB4BB',
    'Hm_lpvt_9c5f07b6ce20e3782eac91ed47d1421c': '1738912669',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'Hm_lvt_9c5f07b6ce20e3782eac91ed47d1421c=1738911846,1738912439; HMACCOUNT=D0C5A2CB881AB4BB; Hm_lpvt_9c5f07b6ce20e3782eac91ed47d1421c=1738912669',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bq08.cc/book/46080/',
    'sec-ch-ua': '"Chromium";v="9", "Not?A_Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.12181 SLBChan/111 SLBVPV/64-bit',
}
for i in range(1, 100):
    response = requests.get(f'https://www.bq08.cc/book/46080/{i}.html', cookies=cookies, headers=headers)
    print(response.text)
