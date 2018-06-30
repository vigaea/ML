import requests
import jieba
from bs4 import BeautifulSoup


res = requests.get("http://news.sina.com.cn/c/zs/2018-03-22/doc-ifysnqkr3697978.shtml")
res.encoding = "utf8"


bs = BeautifulSoup(res.text,"html.parser")
print(bs.title)
print(bs.title.text)


article=bs.select("div.article p")
articles=[]
j=0
k=0
for i in article:
    j+=1;
    articles.append(i.text)
    if(j>2):
        k+=1;
        print("第",k,"段：",i.text)
        

l=0
for i in articles:
    l+=1;
    if(l>2):
        print("/".join(jieba.cut(i)))