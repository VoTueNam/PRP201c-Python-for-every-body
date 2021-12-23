# đọc file json và tính tổng
# http://py4e-data.dr-chuck.net/comments_983449.json
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
sum = 0

address = input('Enter location: ')

print('Retrieving ' + address)
data = urllib.request.urlopen(address, context=ctx).read()

info = json.loads(data)

for item in info["comments"]:
    count += 1
    sum += item["count"]

print('Count: ', count)
print('Sum: ', sum)
