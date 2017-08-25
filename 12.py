# The webpage details
url = "http://www.pythonchallenge.com/pc/return/evil.html"
username = "huge"
password = "file"

# Source code says image is called evil1.jpg. Check for evil2.jpg
url2 = "http://www.pythonchallenge.com/pc/return/evil2.jpg"

# Leads to downloading the file evil2.gfx. A file of characters. Normally multiple images?
data = open('evil2.gfx').read()
print len(data)

# The size of the file is divisible by 5. Multiple of 5 images?
img = {}
for i in range(5):
    img[i] = open("12." + str(i+1) + ".jpg", "w" )

for i in range(len(data)):
    i_img = i % 5
    img[i_img].write(data[i])
