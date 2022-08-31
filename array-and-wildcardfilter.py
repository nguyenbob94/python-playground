import re

airports = ["YMML", "YSSY", "YPPH", "VVTS", "EGLL", "EGKK", "KLAX"]

#Return only Australian airports (Beginning with Y)
for i in airports:
  if re.search('Y.', i):
    print(i)
