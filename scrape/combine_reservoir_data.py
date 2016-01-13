import urllib2
from bs4 import BeautifulSoup
from datetime import datetime, timedelta



us = ['ANT','BLB','BRD','BUC','BUL','CAS','CCH','CHV','CLE','CMN','COY','DAV','DNN','DNP','DON','ENG','EXC','FOL','FRD','HID','HTH','ICH','INP','INV','ISB','KES','LEW','LON','MIL','NAT','NHG','NML','ORO','PAR','PNF','PRR','PYM','SCC','SHA','SNL','STP','TRM','TUL','UNV','WHI','WRS']
#get rid of the ones that have bad values
us = ['ANT','BLB','BRD','BUC','BUL','CHV','CLE','CMN','COY','DAV','DNN','DNP','DON','ENG','EXC','FOL','FRD','HID','HTH','ICH','INV','ISB','KES','LEW','LON','MIL','NAT','NHG','NML','ORO','PAR','PNF','SCC','SHA','SNL','TRM','TUL','UNV','WHI','WRS']

#ordered by largest to smallest
us = ['SHA','ORO','CLE','NML','SNL','DNP','EXC','PNF','FOL','BUL','ISB','MIL','CMN','WRS','HTH','NHG','INV','CHV','UNV','WHI','PAR','TRM','BUC','BLB','COY','BRD','HID','DAV','SCC','ENG','LON','TUL','DON','FRD','ICH','KES','ANT','LEW','NAT']
print us

day0 = '09/29/2003'
day = datetime(2003, 9, 30)
print day.strftime('%m/%d/%Y')
today = datetime.now()

#a is a a list of lists
a = []
a.append([])

for u in us:
    a.append([])

dates = []


while day<today+timedelta(days=1):
    a[0].append(day.strftime('%m/%d/%Y'))
    dates.append(day)
    #print day.strftime('%m/%d/%y')
    day = day + timedelta(days=1)
    for i in range(1, len(us)+1):
        a[i].append('')



thedir = '/Users/David/Desktop/temp/'

k = 0
for u in us:
    #print u
    k+=1

    f = open(thedir+u+".csv")
    lines = f.readlines()
    ls = lines[0].split(',')
    j = 0
    for i in range(len(ls)):
        if 'STORAGE' in ls[i]:
            j = i
            if j > 1:
                j-=1

    if j == 0:
        ls = lines[1].split(',')
        for i in range(len(ls)):
            if 'STORAGE' in ls[i]:
                j = i
                if j > 1:
                    j-=1
    if j == 0:
        ls = lines[2].split(',')
        for i in range(len(ls)):
            if 'STORAGE' in ls[i]:
                j = i
                if j > 1:
                    j-=1
    start = 0

    if u == "CAS":
        print j, "CAS"
    day = datetime(2003, 9, 30)
    for line in lines:
        l = line.split(',')[0]
        if l in a[0]:# day.strftime('%m/%d/%Y'):
            #print line.split(',')[j]
            #day = day + timedelta(days=1)
            #print k,m,j
            m = a[0].index(l)
            #print u
            #print k,m
            if u =='CAS':
                print line.split(',')[j]
            try:
                a[k][m] = line.split(',')[j].replace("\n","").replace("\t",'')
            except:
                a[k][m] = ''


f = open(thedir+"all.csv",'w')

f.write("date,")
for u in us:
    f.write( u+",")
f.write("\n")

for i in range(len(a[0])):
    f.write(a[0][i])
    for j in range(1,len(us)+1):
        #print j, i
        f.write(","+a[j][i])
    f.write("\n")

    #print j, u

f.close()

for i in range(1, len(a)):
    for j in range(len(a[i])):
        try:
            a[i][j] = int(a[i][j])
        except:
            a[i][j] = 0

for j in range(len(a[0])):
    a[0][j] = dates[j]


import cPickle
cPickle.dump(a, open(thedir+'list.p', 'wb'))
#obj = cPickle.load(open(thedir+'list.p', 'rb'))
print "all done"

#
# all_values = []



