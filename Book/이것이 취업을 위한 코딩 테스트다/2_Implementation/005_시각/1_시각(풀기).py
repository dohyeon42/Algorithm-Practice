result = 0
n = int(input())
h = 0
m = 0
s = 0
for i in range(1, n * 3600+ 59*60 + 60):
	if "3" in str(h) or "3" in str(m) or "3" in str(s):
		result += 1
	s += 1
	if s == 60:
		s = 0
		m += 1
	if m == 60:
		m = 0
		h+= 1
print(result)