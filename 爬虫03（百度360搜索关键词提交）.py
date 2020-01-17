import requests

#百度搜索全代码
keyword = "Python"
try :
    kv = {'wd' : keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except :
    print("爬取失败")

'''
#360搜索全代码
keyword = "Python"
try :
    kv = {'q' : keyword}
    r = requests.get("http://www.so.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except :
    print("爬取失败")
'''