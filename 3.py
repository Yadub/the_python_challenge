import urllib2
url = "http://www.pythonchallenge.com/pc/def/equality.html"
page = urllib2.urlopen(url)
data = page.read()

start_data = data.find("<!--")
my_data = data[start_data+4:-4]

data_list = list(my_data)
u_max = 90
u_min = 65
l_max = 122
l_min = 97

l = len(data_list)

def check_uppercase(character):
    if 65 <= ord(character) <= 90:
        return True
    else:
        return False

sol = []

for n in range(len(data_list)):
    big = True
    char = data_list[n]

    if l_min <= ord(char) <= l_max:

        c = data_list

        if n % 81 > 3 and n % 81 < 78:
            cs = data_list[n-3:n+4]
            for i in range(7):
                if i != 3:
                    if not check_uppercase(cs[i]):
                        big = False
        else:
            big = False

        if big:
            lv = uv = "a"
            if n % 81 > 4:
                lv = data_list[n-4]
            if n % 81 < 77:
                uv = data_list[n+4]
            if check_uppercase(uv):
                big = False
            if check_uppercase(lv):
                big = False
        if big:
            # print n, char, ":", cs
            sol = sol + [char]

print "".join(sol)
