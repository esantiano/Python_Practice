str = 'X-DSPAM-Confidence: 0.8475'
sPos = str.find(' ')
num = float(str[sPos+1:])
print(num)