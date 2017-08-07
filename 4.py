import urllib2

nothing = [25357]
while nothing != []:

    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    url = url + str(nothing[0])
    page = urllib2.urlopen(url)
    data = page.read()

    current = nothing[0]

    print data

    nothing = [int(s) for s in data.split() if s.isdigit()]
