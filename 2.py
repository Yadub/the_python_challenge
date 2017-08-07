import urllib2
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
page = urllib2.urlopen(url)
data = page.read()

start_data = data.find("<!--")
my_data = data[start_data:]

chars = list(my_data)
count = [None] * 128
for n in range(128):
    count[n] = my_data.count(chr(n))
    if count[n] > 100: count[n] = 0
    if count[n] == 0:
        while chr(n) in chars: chars.remove(chr(n))
    # #To see progress of code
    # print n
sol = "".join(chars)
print "".join(chars)
