import urllib2
import bz2

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
page = urllib2.urlopen(url)
data = page.read()

start_data = data.find("<!--")
end_data = data.find("-->")
my_data = data[start_data+4:end_data]

print my_data

# Found from the source code of the page
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print "Username:", bz2.decompress(un)
print "Password:", bz2.decompress(pw)
