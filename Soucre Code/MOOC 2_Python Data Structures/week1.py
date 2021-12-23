#lấy số cuối trong dòng sau bằng find và chuyển nó thành float
#text = "X-DSPAM-Confidence:    0.8475";
text = "X-DSPAM-Confidence:    0.8475"
text = text.replace(' ','')
index = text.find(":")+1
print(float(text[index:]))