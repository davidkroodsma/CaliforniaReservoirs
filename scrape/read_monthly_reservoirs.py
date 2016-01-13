import urllib2
from bs4 import BeautifulSoup

url0 = 'http://cdec.water.ca.gov/cgi-progs/queryMonthly?'
url1 = '&d=10-Jan-2016&span=100years'

us = ['ANT', 'BLB', 'BRD', 'BUC', 'BUL', 'CAS', 'CCH', 'CHV', 'CLE', 'CMN', 'COY', 'DAV', 'DNN', 'DNP', 'DON', 'ENG', 'EXC','FOL','FRD','HID','HTH','ICH','INP','INV','ISB','KES','LEW','LON','MIL','NAT','NHG','NML','ORO','PAR','PNF','PRR','PYM','SCC','SHA','SNL','STP','TRM','TUL','UNV','WHI','WRS']
  
thedir = "monthly/"

for u in us:
    filename = thedir + u+".csv"
    f = open(filename, 'w')
    
    html = urllib2.urlopen(url0+u+url1)
    print url0+u+url1
    soup = BeautifulSoup(html)    
    trs = soup.find_all('tr')
  
    for i in range(0, len(trs)):
        t = trs[i]
        text = ''
        for a in t:
            try:
                b = a.text.replace(' ', '')
                b = b.encode('utf-8').strip()
                text += b
            except:
                print b, u, "oh my!"
            text += ","
        text += "\n"
        f.write(text)
    
    f.close()