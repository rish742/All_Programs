text = "X-DSPAM-Confidence:    0.8475";
p = text.find(':')
dis = text[p+1:]
dis = dis.strip()
f = float(dis)
print(f)
