str = 'X-DSPAM-Confidence: 0.8475 '
num = str[str.find(':')+1:]
num = float(num)
print(num)
