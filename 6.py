import zipfile

zip_data = zipfile.ZipFile('channel.zip', 'r')

nothing = [90052]
order = []

while nothing != []:
    file_name = str(nothing[0]) + '.txt'
    data = zip_data.read(file_name)
    print data

    order.append(file_name)
    nothing = [int(s) for s in data.split() if s.isdigit()]

print ''.join([zip_data.getinfo(n).comment for n in order])
