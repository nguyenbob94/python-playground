import re

airports = ["YMML", "YSSY", "YPPH", "VVTS", "EGLL", "EGKK", "KLAX"]

for i in airports:
  if re.search('Y.', i):
    print(i)
