# The webpage details
url = "http://www.pythonchallenge.com/pc/return/bull.html"
username = "huge"
password = "file"

# Clicking on the bull gives:
# a = [1, 11, 21, 1211, 111221,
# Need to find a[30].
# 1 = "one ones" -> 11 = "two ones" -> 21 = "one twos, one ones" -> 1211...

a = "1"
for x in range(30):
    anew = ""
    i = 0
    while i < len(a):
        count = 1
        for d in range(i+1,len(a)):
            if a[i] != a[d]:
                anew += str(count) + str(a[i])
                i = d
                break
            count += 1
        else:
            anew += str(count) + str(a[i])
            i = len(a)
    a = anew

print len(a)
