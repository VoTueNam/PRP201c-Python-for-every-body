# truy cập n (count) lần vào link thứ (position) từ trên xuống
# http://py4e-data.dr-chuck.net/known_by_Dawson.html

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Đặt một hàm đầu vào cho địa chỉ url và phân tích cú pháp thông qua BeautifulSoup
# Set an input function for the url address and parse it through BeautifulSoup
url = input('Enter URL : ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Thiết lập một hàm đầu vào chứa số lần lặp lại
# Set up an input functions for the repeat
countinp = input('Enter count : ')
count = int(countinp)
# vị trí mà nó truy cập (bắt đầu là 1) theo thứ tự từ trên xuongs dưới
# Set up an input function for the position
positioninp = input('Enter position : ')
position = int(positioninp)

# Initialize currcount to 0
currcount = 0

# Repeat the loop for the required amount of repeats
while currcount < count:

    # Truy xuất url cho vị trí cần thiết và in nó
    # Retrieve the url for the required position and print it
    tags = soup('a')
    for tag in tags:
        tag = tags[position - 1].get('href', None)
    print("Retrieving : " + tag)

    # Cập nhật url và phân tích cú pháp qua BeautifulSoup
    # Update url and parse it through BeautifulSoup
    url = tag
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Cập nhật số lượng giới hạn theo 1 mỗi bước
    # Update currcount by 1 each step
    currcount = currcount + 1
