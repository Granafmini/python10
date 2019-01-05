def changed():
	m=int(input())
	l=[]
	for i in range(m):
		l.append(int(input()))
	for i in range(1,m):
		if l[i-1]>l[i]:
			print(l[i-1]);
			break
try:
	changed()
except:
	print('invalid');
