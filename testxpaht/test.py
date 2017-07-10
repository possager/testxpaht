# import pickle
# from testxpaht import myPageStucture
#
# thisclass=myPageStucture.pageStructure()
#
# pickle1=pickle.dumps(thisclass)
# print pickle1
# pickle2=pickle.loads(pickle1)
#
# print pickle2.name
# print pickle2.num
import requests
from bs4 import BeautifulSoup

session1=requests.session()
response1=session1.request(method='GET',url='http://sn.newssc.org/system/20170418/002159156.html',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
# response1.encoding='utf-8'
# print response1
datasoup=BeautifulSoup(response1.text,'lxml')#'/html[1]/body[1]/div[11]/table[1]/tr[1]/td[1]/p[2]/font'
print datasoup.select('body > div:nth-of-type(11) > table > tr > td:nth-of-type(1) > p:nth-of-type(2) > font')