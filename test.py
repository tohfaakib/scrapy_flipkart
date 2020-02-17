# GET /api/3/util/pincode/700159 HTTP/1.1
import requests

header = {
    'Host': '1.rome.api.flipkart.com',
    'Connection': 'keep-alive',
    'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36 FKUA/website/42/website/Desktop',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://www.flipkart.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.flipkart.com/puma-breakout-v2-idp-running-shoes-men/p/itmfd99fxhdreers?pid=SHOFD99YVGFH2NER&lid=LSTSHOFD99YVGFH2NERCKPGOT&marketplace=FLIPKART&srno=b_50_1974&otracker=nmenu_sub_Men_0_Sports%20Shoes&fm=organic&iid=2d5af7e0-aa6c-4f9d-8a0a-17a7087b6a0c.SHOFD99YVGFH2NER.SEARCH&ppt=browse&ppn=browse',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

res = requests.get('https://1.rome.api.flipkart.com/api/3/util/pincode/700159', headers=header)
print(res.json())

fetch_headers = {
    'Host': '1.rome.api.flipkart.com',
    'Connection': 'keep-alive',
    'Content-Length': '348',
    'X-user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36 FKUA/website/42/website/Desktop',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://www.flipkart.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.flipkart.com/puma-breakout-v2-idp-running-shoes-men/p/itmfd99fxhdreers?pid=SHOFD99YVGFH2NER&lid=LSTSHOFD99YVGFH2NERCKPGOT&marketplace=FLIPKART&srno=b_50_1974&otracker=nmenu_sub_Men_0_Sports%20Shoes&fm=organic&iid=2d5af7e0-aa6c-4f9d-8a0a-17a7087b6a0c.SHOFD99YVGFH2NER.SEARCH&ppt=browse&ppn=browse',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': str(res.cookies)

}

fetch_url = 'https://1.rome.api.flipkart.com/api/4/page/fetch'

fetch_res = requests.get(fetch_url, headers=fetch_headers)

print(fetch_res.content)
# print(res.status_code)
# print(res.json())
# print(res.is_redirect)