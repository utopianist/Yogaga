#
import requests
# import re
#
# data = {
#     'mobile': 'utopia',
#     'password': '023299564b0db47d5f3e476a254d0c21',
# }
#
# doc = requests.post(url='http://wz.yogaga.cn/index/user/login', data=data)
# if doc.status_code == 200:
#     print(doc.text)
#     print(doc.headers)
#     cookie = re.match("(PHPSESSID=(.*?));.*",doc.headers['Set-Cookie']).group(1)
#     print(cookie)
#     headers = {
#
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Cookie': cookie,
#         'Host': 'wz.yogaga.cn',
#         'Referer': 'http://wz.yogaga.cn/index/user/login',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#     }
#     print(headers)
#     doc = requests.get('http://wz.yogaga.cn', headers=headers)
#     if doc.status_code == 200:
#         print(doc.text)


headers = {
    'UserAgent': 'wiki'
}
forbin = {'RetKey': '11', 'LogicRet': '159001', 'Content-Type': 'text/html; charset=UTF-8', 'Strict-Transport-Security': 'max-age=0', 'Content-Encoding': 'deflate', 'Set-Cookie': 'rewardsn=; Path=/', 'MMLAS-VERIFYRESULT': 'CAE=', 'Connection': 'keep-alive', 'Content-Length': '4033'}
gorbin = {'Last-Modified': 'Sat, 23 Mar 2019 09:46:45 +0800', 'Expires': 'Sat, 23 Mar 2019 09:55:05 +0800', 'Content-Security-Policy': "script-src 'self' 'unsafe-inline' 'unsafe-eval' http://*.qq.com https://*.qq.com http://*.weishi.com https://*.weishi.com 'nonce-624081146';style-src 'self' 'unsafe-inline' http://*.qq.com https://*.qq.com;object-src 'self' http://*.qq.com https://*.qq.com;font-src 'self' data: http://*.qq.com https://*.qq.com http://fonts.gstatic.com https://fonts.gstatic.com;frame-ancestors 'self' http://wx.qq.com https://wx.qq.com http://wx2.qq.com https://wx2.qq.com  http://wx8.qq.com https://wx8.qq.com http://web.wechat.com https://web.wechat.com http://web1.wechat.com https://web1.wechat.com http://web2.wechat.com https://web2.wechat.com http://sticker.weixin.qq.com https://sticker.weixin.qq.com http://bang.qq.com https://bang.qq.com http://app.work.weixin.qq.com https://app.work.weixin.qq.com http://work.weixin.qq.com https://work.weixin.qq.com http://finance.qq.com https://finance.qq.com http://gu.qq.com https://gu.qq.com http://wzq.tenpay.com https://wzq.tenpay.com;report-uri https://mp.weixin.qq.com/mp/fereport?action=csp_report", 'Content-Type': 'text/html; charset=UTF-8, text/html; charset=UTF-8', 'Cache-Control': 'public, max-age=500', 'RetKey': '14', 'LogicRet': '0', 'Strict-Transport-Security': 'max-age=0', 'Content-Encoding': 'deflate', 'Set-Cookie': 'rewardsn=; Path=/, payforreadsn=EXPIRED; Path=/; Expires=Fri, 22-Mar-2019 01:46:45 GMT; HttpOnly, wxtokenkey=777; Path=/; HttpOnly', 'MMLAS-VERIFYRESULT': 'CAE=', 'Connection': 'keep-alive', 'Content-Length': '33435'}

url = ' https://mp.weixin.qq.com/s?__biz=MzI2MDAxMzM4NQ==&mid=2650369101&idx=6&sn=436782e00043aeccedab46bdab47955b&chksm=f27de06bc50a697dd9cee7183c0646bad93aa9b8ee32a4af30afc2760251814ff931426cb3d2&scene=0&xtrack=1'
url = 'http://60.205.92.109/api.do?name=3E30E00CFEDCD468E6862270F5E728AF&status=1&type=static'
proxy = requests.get('http://localhost:5555/random').text
if proxy:
    print(proxy)
    proxies = {
        'http': 'http://{proxy}'.format(proxy=proxy),
        'https': 'https://{proxy}'.format(proxy=proxy)
    }
    print(proxies)
    r = requests.get(url, headers=headers, proxies=proxies, )
    # r = requests.get(url, headers=headers, allow_redirects=False)

    print(r.status_code)
    print(r.headers)

    # if r.headers['Content-Security-Policy']:
    #     print(r.text)