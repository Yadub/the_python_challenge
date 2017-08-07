import urllib2
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
page = urllib2.urlopen(url)
data = page.read()

my_data = pickle.loads(data)

print my_data[1][1]

for i in range(len(my_data)):
    txt = ""
    for j in range(len(my_data[i])):
        txt = txt + my_data[i][j][0] * my_data[i][j][1]
    print txt
