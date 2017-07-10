import requests

from bs4 import BeautifulSoup

payload= {
      'from': '/bbs/Gossiping/index.html',
      'yes': 'yes'}
rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18', verify = False, data = payload)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', verify = False)
soup = BeautifulSoup(res.text)
for entry in soup.select('.r-ent'):
      print (entry.select('.date')[0].text, entry.select('.author')[0].text, entry.select('.title')[0].text)
